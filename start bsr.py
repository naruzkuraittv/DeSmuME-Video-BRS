import json
import os
import subprocess
import threading
import keyboard
import queue
from tkinter import messagebox, filedialog
import time
import pygetwindow as gw


    
cmd_queue = queue.Queue()
config_data = {}
on_emulator = False
emulator_window_title = None
first_time = True
counting_from_0_offset = -1
movie_offset = 2
desmume_movie_down_arrow_default = 17
movie_down_presses = movie_offset + desmume_movie_down_arrow_default + counting_from_0_offset
### things to get from user on start up with a window that asks to fill in numbers and select file### 
month = 3
day = 20
year = 2000
hours = 8 # must convert to 12 hour clock
minutes = 58
seconds = 59
#ampm = 1 # AM or PM if pm will be 1 arrow down default is am (0)
emulator_path = '' #must be a .exe file prefill with config if exists keep option to change
game_rom_path = '' #must be a .nds file prefill with config if exists keep option to change
gamesave_path = '' #must be a .dsv file prefill with config if exists keep option to change
striped_game_save_path = game_rom_path
### positioning args ###
nav_file_box = 0 # initial tab from start recording
nav_file_box_file_explorer_button = 1 # 1 tab from file box do not ever press this
nav_author_box = 1 # 1 tab from file box explorer button
nav_date_box = 3 # 1 tab from author box
nav_date_box_month_arrow_right = 0 # default month = january aka we use numbers 1 for jan 2 for feb etc
nav_date_box_day_arrow_right = 1 # set date via typing in numbers (must be real day of month no feb 31st) 
nav_date_box_year_arrow_right = 1 # set year via typing in numbers (must be real year on ds clock aka 2000 - 2099)
nav_time_box = 1 #1tab after date box
nav_time_box_hours_arrow_right = 0 # uses 12 hour clock aka max 12 
nav_time_box_minutes_arrow_right = 1 # in 00-59 format
nav_time_box_seconds_arrow_right = 1
nav_time_box_milliseconds_am_pm_right = 1 # default am pm = down arrow 
nav_sram_box = 1 # 1 tab after time box only exist if startfromsram is checked only needs to be checked once still exists if checked
nav_sram_box_file_explorer_button = 1 # 1 tab after sram box do not ever press this, it only exists if startfromsram is checked
nav_start_from_power_on_box = 1 # 1 tab after sram box exporer button
nav_ok_box = 1 # 1 tab after start from power on box
nav_cancel_box = 1 # 1 tab after ok box
# after cancel box loops to file box
#every time we click tab we need to change the position, we can keep tracj of the position via array. and if in date box or time box we need sub tracker to know if we are on month day year or hours minutes seconds based on the arrow right, jsut to be safe we need to move cursor back to the left on position month and hours after we are done with them]
# Positioning arguments
record_movie_position = {
    'nav_file_box': 0,
    'nav_file_box_file_explorer_button': 1,
    'nav_author_box': 1,
    'nav_date_box': 1,
    'nav_date_box_month_arrow_right': 0,
    'nav_date_box_day_arrow_right': 1,
    'nav_date_box_year_arrow_right': 1,
    'nav_date_box_month_arrow_left': 1,
    'nav_time_box': 1,
    'nav_time_box_hours_arrow_right': 0,
    'nav_time_box_minutes_arrow_right': 1,
    'nav_time_box_seconds_arrow_right': 1,
    'nav_time_box_milliseconds_am_pm_right': 1,
    'nav_sram_box': 1,
    'nav_sram_box_file_explorer_button': 1,
    'nav_start_from_sram_box': 1,
    'nav_start_from_power_on_box': 1,
    'nav_ok_box': 1,
    'nav_cancel_box': 1
}



def navigate_record_box():
    global hours
    global ampm
    global gamesave_path
    global game_rom_path
    global striped_game_save_path
    global striped_game_rom_path
    striped_game_rom_path = game_rom_path.split('/')[-1].split('.')[0]
    striped_game_save_path = gamesave_path.split('/')[-1].split('.')[0]
    # Starting at nav_file_box
    current_position = 'nav_file_box'
    
    # Navigate to nav_date_box
    keyboard.write(striped_game_rom_path)
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
    press_key('enter')  # Confirm the settings
    return

def get_file_path(title, filetypes):
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

def does_config_exist():
    global config_data
    if not os.path.exists('config.json'):
        config_data = {'emulator_path': '', 'game_roms': {}}
    else:
        with open('config.json', 'r') as f:
            config_data = json.load(f)


# Call the function to execute the navigation
def set_rng_init_time():
    open_movie()
    navigate_record_box()
    

def update_config():
    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=4)

def does_file_still_exist(file_path):
    return os.path.exists(file_path)


def press_key(key, times=1, delay=0.01):
    for _ in range(times):
        keyboard.press_and_release(key)
        time.sleep(delay)
        
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
                if messagebox.askyesno("Set as Default", f"Do you want to set this as the default {item}?"):
                    config_data[default_key] = path
                    update_config()
                return path
            else:
                messagebox.showwarning("Invalid File", f"The selected file does not have the {extension} extension.")
        else:
            messagebox.showwarning("No File Selected", f"No {item} file selected.")

def start_game():
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

def start_logic():
    global emulator_path, game_rom_path, gamesave_path
    does_config_exist()
    emulator_path = set_path("emulator", "emulator_path", [("Emulator Executable", "*.exe")], ".exe")
    print(emulator_path)
    game_rom_path = set_path("game ROM", "default_rom", [("NDS ROM", "*.nds")], ".nds")
    print(game_rom_path)
    gamesave_path = set_path("game save", "default_save", [("Game Save", "*.dsv")], ".dsv")
    print(gamesave_path)
    threading.Thread(target=command_worker, daemon=True).start()
    print("started thread worker starting hotkey listener")

def press_multiple(number_of_times, button, delay=0.001, button2=None):
    for i in range(number_of_times):
        keyboard.press(button)
        if button2:
            keyboard.press(button2)
        time.sleep(delay)
        keyboard.release(button)
        if button2:
            keyboard.release(button2)

down_presses = 18 - 1

def open_movie():
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
            check_how_many_times_to_press_down()
            messagebox.showinfo("SRAM Check", "Please make sure the SRAM check box is checked, click cancel when done.\n Press ctrl+alt+shift+r again to to start the rng manipulation process")
            first_time = False
        else:
            keyboard.press_and_release('alt+f')
            print("alt f")
            press_multiple(movie_down_presses, 'down', 0.01)
            print(f"down {movie_down_presses}x times")
            keyboard.press_and_release('enter')
            print("enter")
    time.sleep(0.01)

def command_worker():
    while True:
        cmd = cmd_queue.get()
        if cmd == "set_rng_init_time":
            print("ctrl+alt+shift+r was pressed")
            set_rng_init_time()
            time.sleep(4)
        elif cmd == "get_emulator_title":
            print("ctrl+alt+shift+s was pressed")
            get_emulator_title()
            time.sleep(0.5)
        elif cmd == "open_new_emulator":
            print("ctrl+alt+shift+e was pressed")
            start_game()
            time.sleep(0.5)
        cmd_queue.task_done()

def enqueue_command(command):
    if command not in list(cmd_queue.queue):
        cmd_queue.put(command)

def hotkey_listener():
    keyboard.add_hotkey('ctrl+alt+shift+r', enqueue_command, args=["set_rng_init_time"])
    keyboard.add_hotkey('ctrl+alt+shift+s', enqueue_command, args=["get_emulator_title"])
    keyboard.add_hotkey('ctrl+alt+shift+e', enqueue_command, args=["open_new_emulator"])
    keyboard.wait()

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

def check_how_many_times_to_press_down():
    global movie_down_presses
    global first_time
    keyboard.press_and_release('alt+f')
    time.sleep(0.1)
    print("alt f")
    press_multiple(movie_down_presses, 'down', 0.1)
    print(f"down {movie_down_presses}x times")
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    global desmume_movie_down_arrow_default
    movie_down = movie_offset + desmume_movie_down_arrow_default 
    press_multiple(movie_down_presses, 'tab', 0.01)
    if messagebox.askyesno("Movie Button", "Is the record movie window up? Press no to try calibrating again") == False:
        movie_down_presses = movie_down_presses - 1
        first_time = True        
    first_time = False

start_logic()
threading.Thread(target=command_worker, daemon=True).start()
start_game()
hotkey_listener()
time.sleep(2)
