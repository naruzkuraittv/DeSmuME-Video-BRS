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
emulator_path = ''
game_rom_path = ''
gamesave_path = ''
config_data = {}
on_emulator = False
emulator_window_title = None
first_time = True

def does_config_exist():
    global config_data
    if not os.path.exists('config.json'):
        config_data = {'emulator_path': '', 'game_roms': {}}
    else:
        with open('config.json', 'r') as f:
            config_data = json.load(f)

def update_config():
    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=4)

def does_file_still_exist(file_path):
    return os.path.exists(file_path)

def get_file_path(title, filetypes):
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

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
    stripped_game_rom_path = game_rom_path.split('/')[-1].split('.')[0]
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
            press_multiple(down_presses, 'down', 0.01)
            print(f"down {down_presses}x times")
            keyboard.press_and_release('enter')
            print("enter")
            keyboard.write(stripped_game_rom_path)
            print("wrote rom name")
            press_multiple(2, 'tab', 0.01)
            print("tab 2x")
            keyboard.write('nzk-script')
            print("wrote nzk-script as author")
            press_multiple(3, 'tab')
            print("tab 3x")
            keyboard.write(gamesave_path)
            keyboard.press_and_release('enter')
    time.sleep(2)

def command_worker():
    while True:
        cmd = cmd_queue.get()
        if cmd == "open_movie":
            print("ctrl+alt+shift+r was pressed")
            open_movie()
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
    keyboard.add_hotkey('ctrl+alt+shift+r', enqueue_command, args=["open_movie"])
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
    global down_presses
    keyboard.press_and_release('alt+f')
    time.sleep(0.1)
    print("alt f")
    press_multiple(down_presses, 'down', 0.1)
    print(f"down {down_presses}x times")
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    press_multiple(7, 'tab', 0.01)
    if messagebox.askyesno("Movie Button", "Is the record movie window up? Press no to try calibrating again") == False:
        down_presses = down_presses - 1
        first_time = True        
    first_time = False

start_logic()
threading.Thread(target=command_worker, daemon=True).start()
start_game()
hotkey_listener()
