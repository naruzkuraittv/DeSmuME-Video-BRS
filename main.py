import json
import os
import subprocess

import keyboard

from tkinter import messagebox, filedialog
import time
import pygetwindow as gw
import nzk_shortcuts as nzksk
from tkinter import simpledialog
#first beep counter = soft reset
#2nd counter = cya later oak

############################## SETUP CONFIG ##############################

################## end of default config ##################


default_config = {
    "defaults": {
        "emulator_path": "", 
        "default_rom": "",  
        "default_save": ""  
    },
    "author": "NZK_scripts",
    "Movie_record_box_auto_start_y_n_qm": "yes",
    "date_time_pokefinder": "2000-01-01 08:07:00",
    "target_frame_offset": 0,
    "target_frame": 0,
    "desmume_movie_down_arrow_default": 17,
    "movie_down_arrow_offset": 2,
    "counting_from_0_offset": -1,
    "comment": "4th letter in region rom code is language, e = english j = japanese p = pal, D = german(doichland), F = french, I = italian, S = spanish, K = korean, N = chinese, im not sure about other",  
    "NDS_ROMS": {
        "ADAE01": {
            "Game_Name": "Pokémon Diamond",
            "region": "ENG",
            "rom_nick_name": "",
            "lang": "ENG"
        },
        "ADAJ01": {
            "Game_Name": "Pokémon Diamond",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "ADAP01": {
            "Game_Name": "Pokémon Diamond",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "APAE01": {
            "Game_Name": "Pokémon Pearl",
            "region": "ENG",
            "rom_nick_name": "",
            "lang": "ENG"
        },
        "APAJ01": {
            "Game_Name": "Pokémon Pearl",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "APAP01": {
            "Game_Name": "Pokémon Pearl",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "CPUE01": {
            "Game_Name": "Pokémon Platinum",
            "region": "ENG",
            "rom_nick_name": "",
            "lang": "ENG"
        },
        "CPUJ01": {
            "Game_Name": "Pokémon Platinum",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "CPUP01": {
            "Game_Name": "Pokémon Platinum",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IPKE01": {
            "Game_Name": "Pokémon HeartGold",
            "region": "ENG",
            "rom_nick_name": "",
            "lang": "ENG"
        },
        "IPKJ01": {
            "Game_Name": "Pokémon HeartGold",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "IPKP01": {
            "Game_Name": "Pokémon HeartGold",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IPGE01": {
            "Game_Name": "Pokémon SoulSilver",
            "region": "ENG",
            "rom_nick_name": "",
            "lang": "ENG"
        },
        "IPGJ01": {
            "Game_Name": "Pokémon SoulSilver",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "IPGP01": {
            "Game_Name": "Pokémon SoulSilver",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IRBE01": {
            "Game_Name": "Pokémon Black",
            "region": "ENG",
            "rom_nick_name": "",
            "lang": "ENG"
        },
        "IRBJ01": {
            "Game_Name": "Pokémon Black",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        
        "IRBF01": {
            "Game_Name": "Pokémon Black",
            "region": "FR",
            "rom_nick_name": "",
            "lang": "FR"
        }
        },
        "IRBP01": {
            "Game_Name": "Pokémon Black",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IRAE01": {
            "Game_Name": "Pokémon White",
            "region": "ENG",
            "rom_nick_name": "",
            "lang": "ENG"
        },
        "IRAJ01": {
            "Game_Name": "Pokémon White",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "IRAP01": {
            "Game_Name": "Pokémon White",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IREJ01": {
            "Game_Name": "Pokémon Black 2",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "IREP01": {
            "Game_Name": "Pokémon Black 2",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IREO01": {
            "Game_Name": "Pokémon Black 2",
            "region": "Other",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IRDJ01": {
            "Game_Name": "Pokémon White 2",
            "region": "JP",
            "rom_nick_name": "",
            "lang": "JP"
        },
        "IRDP01": {
            "Game_Name": "Pokémon White 2",
            "region": "PAL",
            "rom_nick_name": "",
            "lang": "Other"
        },
        "IRDO01": {
            "Game_Name": "Pokémon White 2",
            "region": "Other",
            "rom_nick_name": "",
            "lang": "Other"
        },
    

    "record_movie_position": {
        "nav_file_box": 0,
        "nav_file_box_file_explorer_button": 1,
        "nav_author_box": 1,
        "nav_date_box": 1,
        "nav_date_box_month_arrow_right": 0,
        "nav_date_box_day_arrow_right": 1,
        "nav_date_box_year_arrow_right": 1,
        "nav_date_box_month_arrow_left": 1,
        "nav_time_box": 1,
        "nav_time_box_hours_arrow_right": 0,
        "nav_time_box_minutes_arrow_right": 1,
        "nav_time_box_seconds_arrow_right": 1,
        "nav_time_box_milliseconds_am_pm_right": 1,
        "nav_sram_box": 1,
        "nav_sram_box_file_explorer_button": 1,
        "nav_start_from_sram_box": 1,
        "nav_start_from_power_on_box": 1,
        "nav_ok_box": 1,
        "nav_cancel_box": 1
    }
}

 # yes i realy need one for readablity coz in dumb lol
########################################################### set default config so it doesnt sugest defeaults in editior ############################## 
config_data = default_config
if os.path.exists('config.json'): #check if config.json exists if not create it with default_config, if it does exist load it into config_data
    config_data = json.load(open('config.json'))
else:
    with open('config.json', 'w') as f:
        json.dump(default_config, f, indent=4)
    config_data = json.load(open('config.json')) #redundent but its just so its easier for me to wrap my head around
########################################################### end of set default config so it doesnt sugest defeaults in editior ##############################


# Load the current configuration
#if config.json does not exist create it with default_config, else load it into config_data
if os.path.exists('config.json'):
    config_data = json.load(open('config.json'))
else:
    with open('config.json', 'w') as f:
        json.dump(default_config, f, indent=4)
    config_data = json.load(open('config.json')) # dont even try to inject stuff in python scrtipts lol
########################################################### non config variables ##############################
on_emulator = False
emulator_window_title = None
first_time = True
########################################################### set variables from config ##############################

def update_variables_from_config():
    global author
    global config_date
    global on_emulator
    global emulator_window_title
    global first_time
    global counting_from_0_offset
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

def update_config():
    global config_data
    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=4)

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



###################### end of after reading config set all variables ######################
################# read region coded #################
def get_region(full_path):
    filename = full_path.split("/")[-1]
    if "Europe" in filename or "EUR" in filename:
        Region = "Europe"
    elif "USA" in filename:
        Region = "USA"
    elif "JPN" in filename or "Japan" in filename:
        Region = "Japan"
    elif "GER" in filename or "Germany" in filename or "DE" in filename or "DOI" in filename:
        Region = "Germany"
    elif "SPA" in filename or "Spain" in filename or "ESP" in filename:
        Region = "Spain"  # Corrected variable name
    elif "KOR" in filename or "Korea" in filename:
        Region = "Korea"
    elif "FRA" in filename or "France" in filename:
        Region = "France"
    elif "ITA" in filename or "Italy" in filename:
        Region = "Italy"
        if "Edition" in filename:
            filename = filename.replace("Edition", "")
            if "Italy" in filename:
                Region = "Italy"
    else:
        Region = "Unknown"
    return Region

def get_language(header_data):
    t = header_data[12:28].decode("utf-8").rstrip('\x00')  # Title of the game
    print_title = header_data[0:18].decode("utf-8")  # Title of the game
    print(f"get language: {print_title}, the 3rd character and ideally the language indicator in this is {t[3]}")
    if t[3] == "E":
        Language = "English"
    elif t[3] == "F":
        Language = "French"
    elif t[3] == "D":
        Language = "German"
    elif t[3] == "I":
        Language = "Italian"
    elif t[3] == "J":
        Language = "Japanese"
    elif t[3] == "K":
        Language = "Korean"
    elif t[3] == "S":
        Language = "Spanish"
    elif t[3] == "C":
        Language = "Chinese"
    else:
        Language = "Unknown"
    return Language
def read_title_from_rom_header(rom): 
    full_path = os.path.join(rom)
    with open(rom, "rb") as rom_file:
        header_data = rom_file.read(512)  # NDS header is typically 512 bytes
    title = header_data[12:15].decode("utf-8").rstrip('\x00')  # Title of the game
    print(title)
    #TAKE FIRST 3 LETTERS OF TITLE AND MAKE IT UPPERCASE
    title = title[0:8].upper()
    title = title.replace(" ", "")
    title = title.strip()  # Remove trailing spaces
    for i in title:
        #a = getvalue of i
        a = title.index(i)
        print(title[a])
    print(title)
    #check if title is in list1

    list1 = ["ADA", "APA", "CPU", "IPK", "IPG", "IRB", "IRA", "IRE", "IRD" ]
    list2 = ["diamond", "pearl", "platinum", "heartgold", "soulsilver", "black", "white", "black2", "white2"]
    print(f"list1:{list1}, list2:{list2}")
    # is title in list1?
    if title in list1:
        print("yes")
        #if yes, get index of title in list1
        index = list1.index(title)
        print(index)
        #get value of index in list2
        print(list2[index])
        #if no, print error


###################### start of definitions ######################

#### simple functions ####

def get_file_path(title, filetypes):
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

def strip_file_path(input_file_path):
    return input_file_path.split('/')[-1].split('.')[0]
    




def does_file_still_exist(file_path):
    return os.path.exists(file_path)


def press_key(key, times=1, delay=0.01):
    for _ in range(times):
        keyboard.press_and_release(key)
        time.sleep(delay)
        
def press_multiple(number_of_times, button, delay=0.001, button2=None):
    for i in range(number_of_times):
        keyboard.press(button)
        if button2:
            keyboard.press(button2)
        time.sleep(delay)
        keyboard.release(button)
        if button2:
            keyboard.release(button2)
    
############### missing functions ################


############### shortcut ctrl + alt + shift + r ################
# Call the function to execute the navigation
def set_rng_init_time():
    go_to_record_movie_and_open_record_movie_box()
    navigate_record_box()
    if_we_pres_enter_for_movie_date_time_for_rng_press_enter_else_stop()
    
############### define set_rng_init_time ################
def go_to_record_movie_and_open_record_movie_box():
    global first_time
    global on_emulator
    time.sleep(0.2)
    check_if_on_emulator()
    if on_emulator == False:
        print("not on emulator")
        on_emulator = False
        return
    else:
        print("on emulator")
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('alt') or keyboard.is_pressed('shift') or keyboard.is_pressed('r'):
            print("ctrl or alt or shift or r is pressed")
            print("waiting 0.1 seconds")
            time.sleep(0.1)
        if first_time == True:
            if messagebox.askyesno("did the record movie box show up?") == False:
                #ask if we want to increase or decrease by 1 or 2 or 3
                messageboxresponse = simpledialog.askinteger("Input", "Do you want to increase or decrease by 1, 2 or 3?")
                #edit config
                config_data['movie_offset'] = config_data['movie_offset'] + messageboxresponse
                #update config
                update_config()
                first_time = True
                go_to_record_movie_and_open_record_movie_box()
            else:
                is_check_box_selected()
                keyboard.press_and_release('esc')
                first_time = False
                go_to_record_movie_and_open_record_movie_box()
        else:
            keyboard.press_and_release('alt+f')
            print("alt f")
            press_multiple(movie_down_presses, 'down', 0.01)
            print(f"down {movie_down_presses}x times")
            keyboard.press_and_release('enter')
            print("enter")
    time.sleep(0.01)
def is_check_box_selected():
    if messagebox.askyesno("check the sram box", "is the sram box selected?") == False:
        print("sram box not selected")
        is_check_box_selected()
    else:
        print("sram box selected")
        
        return
#def altf_go_movie_down_presses_times():
def if_we_pres_enter_for_movie_date_time_for_rng_press_enter_else_stop():
    striped_game_rom_path = strip_file_path(game_rom_path)
    striped_game_save_path = strip_file_path(gamesave_path)
    if config_data.get('Movie_record_box_auto_start_y_n_qm', 'no') == 'yes':
        keyboard.press_and_release('enter')
        print (f"movie started with {striped_game_rom_path} and {striped_game_save_path}, at {month}/{day}/{year} {hours}:{minutes}:{seconds}, with aurthor {author}")
    else:
        pass
    print("competed navigation of record box for rng")
       
def navigate_record_box():
    update_variables_from_config()
    global month
    global day
    global year
    global hours
    global minutes
    global seconds
    global ampm
    global gamesave_path
    global game_rom_path
    global minutes
    srp = strip_file_path(game_rom_path)
    sfp = strip_file_path(gamesave_path)

    # Starting at nav_file_box
    keyboard.write(sfp)
    press_key('tab', record_movie_position['nav_file_box_file_explorer_button'])
    press_key('tab', record_movie_position['nav_author_box'])
    keyboard.write('nzk-script')
    press_key('tab', record_movie_position['nav_date_box'])
    # Enter Date
    press_key('right', record_movie_position['nav_date_box_month_arrow_right']) # doesnt move cursor
    keyboard.write(str(month))
    press_key('right', record_movie_position['nav_date_box_day_arrow_right'])
    keyboard.write(str(day))
    press_key('right', record_movie_position['nav_date_box_year_arrow_right'])
    keyboard.write(str(year))
    press_key('left', record_movie_position['nav_date_box_month_arrow_left']) # doesnt move cursor
    press_key('left', record_movie_position['nav_date_box_month_arrow_left'])
    # Navigate to nav_time_box
    press_key('tab', record_movie_position['nav_time_box'])
    # Enter Time
    press_key('right', record_movie_position['nav_time_box_hours_arrow_right']) # doesnt move cursor
    ampm = 0
    if hours >= 12:
        hours = hours - 12
        ampm = 1
        keyboard.write(str(hours))
    keyboard.write(str(hours)) # max 12
    press_key('right', record_movie_position['nav_time_box_minutes_arrow_right'])
    if minutes == 0:
        keyboard.write(str(minutes))
        keyboard.write(str(minutes))
    else:
        keyboard.write(str(minutes))
    press_key('right', record_movie_position['nav_time_box_seconds_arrow_right'])
    keyboard.write(str(seconds))
    if ampm == 1:  # If PM, press down once
        press_key('down')
    #move to sram box
    press_key('tab', record_movie_position['nav_sram_box'])

    keyboard.write(gamesave_path)
    # Navigate to nav_ok_box to confirm
    press_key('tab', record_movie_position['nav_ok_box'])
    press_key('tab', record_movie_position['nav_start_from_sram_box'])
    press_key('tab', record_movie_position['nav_start_from_power_on_box'])
    press_key('tab', record_movie_position['nav_ok_box'])




def first_time_setup_for_start_rng():
    global movie_down_presses
    global first_time
    keyboard.press_and_release('alt+f')
    time.sleep(0.1)
    print("alt f")
    press_multiple(movie_down_presses, 'down', 0.1)
    print(f"down {movie_down_presses}x times")
    time.sleep(0.5)
    keyboard.press_and_release('enter')

    press_multiple(movie_down_presses, 'tab', 0.01)
    if messagebox.askyesno("Movie Button", "Is the record movie window up? Press no to try calibrating again") == False:
        movie_down_presses = movie_down_presses - 1
        first_time = True        
    first_time = False
############### end of shortcut ctrl + alt + shift + r ################

def set_path(item, default_key, filetypes, extension):
    global config_data
    default_path = config_data.get(default_key, '')
    if default_path and does_file_still_exist(default_path):
        use_default = messagebox.askyesno("Use Default", f"The current default {item} is: {default_path}\nDo you want to use this default?")
        if use_default:
            return default_path
    while True:
        path = get_file_path(f"Select {item}", filetypes)
        if path:
            if path.endswith(extension):
                default_item =  messagebox.askyesno("Set as Default", f"Do you want to set this as the default {item}?")
                if default_item == True:
                    # defualt path = defaults: {"emulator_path": "", "default_rom": "", "default_save": ""} so defualts = key emulator path = value
                    config_data[default_key] = default_item
                    update_config()
                return path
            else:
                if messagebox.askyesno("Invalid File", f"The selected file does not have the {extension} extension.\nDo you want to continue using this file?"):
                    return path
        else:
            messagebox.showwarning("No File Selected", f"No {item} file selected.")
################################# shortcut ctrl + alt + shift + e ##############################
def start_emulator():
    global emulator_path, game_rom_path, gamesave_path
    if emulator_path and game_rom_path and gamesave_path:
        command = [emulator_path, game_rom_path]
        print(f"Executing command: {command}")
        try:
            subprocess.Popen(command)
            print("Game Started")
        except Exception as e:
            print(f"Failed to start the game: {e}")
    else:
        print("Missing game settings. Please set the emulator, ROM, and save paths.")
################################# end of shortcut ctrl + alt + shift + e ##############################



################################## ctrl + alt + shift + s ##############################
# lock the usage of ctrl + alt + shift + r to only when on emulator

def get_emulator_title():
    global emulator_window_title
    emulator_window_title = gw.getActiveWindow().title
    print(emulator_window_title)

def check_if_on_emulator():
    global on_emulator
    active_window_title = gw.getActiveWindow().title
    if active_window_title == emulator_window_title:
        print("on emulator")
        print(active_window_title)
        on_emulator = True
        return
    else:
        print("not on emulator")
        print(active_window_title)
        on_emulator = False
        return




################## next thign to do is calc next see based on start time and find current delay and also click the a button when the time is right ##################



################### script start ###################
def start_logic():
    global emulator_path, game_rom_path, gamesave_path
    emulator_path = set_path("emulator", "emulator_path", [("Emulator Executable", "*.exe"), ("All Files", "*.*")], ".exe")
    print(emulator_path)
    game_rom_path = set_path("game ROM", "default_rom", [("NDS ROM", "*.nds"), ("All Files", "*.*")], ".nds")
    print(game_rom_path)
    #dsv or sav files or *.* for all files
    gamesave_path = set_path("game save", "default_save", [("DSV Save", "*.dsv"), ("SAV Save", "*.sav"), ("All Files", "*.*")], ".dsv")
    print(gamesave_path)
    
    shortcuts = {
    "ctrl+shift+alt+r": set_rng_init_time,
    "ctrl+shift+alt+e": start_emulator,
    "ctrl+alt+shift+s": get_emulator_title
}
    nzksk.start_listener(shortcuts)
    
    if messagebox.askyesno("do you want to start emulator?") == True:
        start_emulator()
    print("started thread worker starting hotkey listener")
    



start_logic()



