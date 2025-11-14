import tkinter as tk
from tkinter import filedialog, simpledialog
import json
with open('config.json', 'r') as f:
    config_data = json.load(open('config.json'))


def update_config():
    global config_data
    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=4)
        
def update_variables_from_config():
    global author
    global config_date
    global desmume_movie_down_arrow_default
    global movie_offset
    global Pokefinder_date_and_Time
    global month
    global day
    global year
    global hours
    global minutes
    global seconds
    global movie_down_presses
    global emulator_path
    global game_rom_path
    global gamesave_path
    global record_movie_position
    global config_data
    global roms
    global counting_from_0_offset
    config_data = json.load(open('config.json'))
    cf = config_data
    counting_from_0_offset = cf["counting_from_0_offset"]
    author = cf["author"]
    config_date = cf["date_time_pokefinder"]
    desmume_movie_down_arrow_default = cf["desmume_movie_down_arrow_default"]
    movie_offset = config_data['movie_down_arrow_offset']
    Pokefinder_date_and_Time = config_data['date_time_pokefinder']
    month = int(Pokefinder_date_and_Time[5:7])
    day = int(Pokefinder_date_and_Time[8:10])
    year = int(Pokefinder_date_and_Time[0:4])
    hours = int(Pokefinder_date_and_Time[11:13]) 
    minutes = int(Pokefinder_date_and_Time[14:16])
    seconds = int(Pokefinder_date_and_Time[17:19])
    movie_down_presses = int(movie_offset) + int(desmume_movie_down_arrow_default) + int(counting_from_0_offset)
    emulator_path = '' #must be a .exe file prefill with config if exists keep option to change
    game_rom_path = '' #must be a .nds file prefill with config if exists keep option to change
    gamesave_path = '' #must be a .dsv file prefill with config if exists keep option to change
    record_movie_position = cf["record_movie_position"]
    roms = cf["NDS_ROMS"]
update_variables_from_config()

def select_rom():
    update_variables_from_config()
    rom_name = simpledialog.askstring("Input", "What is the name of the rom?")
    rom_path = get_file_path("Select ROM", [("NDS ROM", "*.nds"), ("All Files", "*.*")])
    rom_id = simpledialog.askstring("Input", "What is the ID of the rom?")
    rom_title = simpledialog.askstring("Input", "What is the title of the rom?")
    rom_region = simpledialog.askstring("Input", "What is the region of the rom?")
    rom_nick_name = simpledialog.askstring("Input", "What is the nickname of the rom?")
    rom_lang = simpledialog.askstring("Input", "What is the language of the rom?")
    add_rom_to_config(rom_name, rom_path, rom_id, rom_title, rom_region, rom_nick_name, rom_lang)
    
def add_rom_to_config(rom_name, path, id, title, region, rom_nick_name, lang):
    global config_data
    config_data['NDS_ROMS'][rom_name] = {
        'path': path,
        'extras': {
            'id': id,
            'title': title,
            'region': region,
            'rom_nick_name': rom_nick_name,
            'lang': lang
        }
    }

    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=4)

def add_save_to_rom(rom_name, save_path):
    update_variables_from_config()

    if rom_name in config_data['NDS_ROMS']:
        config_data['NDS_ROMS'][rom_name]['saves'] = save_path
    else:
        print(f"ROM {rom_name} does not exist in the config file.")
        exit("something went wrong it should exist")
           
    update_config()

def get_file_path(title, filetypes):
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

def add_new_rom():
    rom_name = name_entry.get()
    rom_path = path_entry.get()
    rom_id = id_entry.get()
    rom_title = title_entry.get()
    rom_region = region_entry.get()
    rom_nick_name = nickname_entry.get()
    rom_lang = language_entry.get()
    add_rom_to_config(rom_name, rom_path, rom_id, rom_title, rom_region, rom_nick_name, rom_lang)

def get_file_path(title, filetypes):
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

# Initialize Tkinter root window
root = tk.Tk()
root.title("ROM Selector")

# Forward declare widgets to avoid reference issue
name_entry = tk.Entry(root)
path_entry = tk.Entry(root)
id_entry = tk.Entry(root)
title_entry = tk.Entry(root)
region_entry = tk.Entry(root)
nickname_entry = tk.Entry(root)
language_entry = tk.Entry(root)

def add_new_rom():
    rom_name = name_entry.get()
    rom_path = path_entry.get()
    rom_id = id_entry.get()
    rom_title = title_entry.get()
    rom_region = region_entry.get()
    rom_nick_name = nickname_entry.get()
    rom_lang = language_entry.get()
    add_rom_to_config(rom_name, rom_path, rom_id, rom_title, rom_region, rom_nick_name, rom_lang)

def select_rom_path():
    rom_path = get_file_path("Select ROM", [("NDS ROM", "*.nds"), ("All Files", "*.*")])
    path_entry.delete(0, tk.END)
    path_entry.insert(0, rom_path)
    
    
    
# Initialize Tkinter root window
root = tk.Tk()
root.title("ROM Selector")

# Frames
button_frame = tk.Frame(root)
add_frame = tk.Frame(root)

# Forward declare widgets to avoid reference issue
name_entry = tk.Entry(add_frame)
path_entry = tk.Entry(add_frame)
id_entry = tk.Entry(add_frame)
title_entry = tk.Entry(add_frame)
region_entry = tk.Entry(add_frame)
nickname_entry = tk.Entry(add_frame)
language_entry = tk.Entry(add_frame)

# [Your existing function definitions]

# Define and layout widgets
use_default_button = tk.Button(button_frame, text="Use Default ROM", command=lambda: root.quit())
add_new_button = tk.Button(button_frame, text="Add New ROM", command=lambda: add_frame.pack())

name_label = tk.Label(add_frame, text="*Name:")
path_label = tk.Label(add_frame, text="*Path:")
browse_button = tk.Button(add_frame, text="Browse", command=select_rom_path)
id_label = tk.Label(add_frame, text="ID:")
title_label = tk.Label(add_frame, text="*Title:")
region_label = tk.Label(add_frame, text="*Region:")
nickname_label = tk.Label(add_frame, text="*Nickname:")
language_label = tk.Label(add_frame, text="Language:")
submit_button = tk.Button(add_frame, text="Submit", command=add_new_rom)

# Layout
button_frame.pack(pady=10)
use_default_button.pack(side=tk.LEFT, padx=5)
add_new_button.pack(side=tk.LEFT, padx=5)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
path_label.grid(row=1, column=0)
path_entry.grid(row=1, column=1)
browse_button.grid(row=1, column=2)
id_label.grid(row=2, column=0)
id_entry.grid(row=2, column=1)
title_label.grid(row=3, column=0)
title_entry.grid(row=3, column=1)
region_label.grid(row=4, column=0)
region_entry.grid(row=4, column=1)
nickname_label.grid(row=5, column=0)
nickname_entry.grid(row=5, column=1)
language_label.grid(row=6, column=0)
language_entry.grid(row=6, column=1)
submit_button.grid(row=7, column=1, pady=10)

# Start the main loop
root.mainloop()