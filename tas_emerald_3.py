import keyboard
import time
import nzk_shortcuts as nzksk
import pyautogui

keybinds = {"a": "space", "b": "x", "l": "q", "r": "e", "start": "f", "select": "r", "up": "w", "down": "s", "left": "a", "right": "d", "advance_frame": "n"}
counter = 0

def advance_frame(frames_to_pass):
    global counter
    for _ in range(frames_to_pass):
        keyboard.press(keybinds["advance_frame"])
        time.sleep(0.02)
        keyboard.release(keybinds["advance_frame"])
        counter += 1
        time.sleep(0.0)
        print(f"{counter} frames have passed")
        if counter % 5 == 0:
            time.sleep(0.01)
            print(f"quick pause, {counter} frames have passed")
        if counter % 60 == 0:
            time.sleep(0.01)
            print(f"quick pause, {counter} frames have passed")

def start():
    location_offset = 0
    first_start_press = 290
    second_start_press = 40
    third_start_press = 40
    save_press = 60
    opening_save_delay = 80
    location_offset = "cave"
    calibration = int(0)
    target_or_shiny_frame = 6943
    if keyboard.is_pressed("ctrl") or keyboard.is_pressed("alt") or keyboard.is_pressed("shift") or keyboard.is_pressed("r"):
        time.sleep(1)
        start()
    else:
        main(target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)

def main(target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay):
    counter = 0
    start_time = time.time()
    restart()
    open_save(first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)
    open_menu()
    goto_party_menu(20, 20)
    party_member_hms_menu(74, 10)
    sweet_scent(target_or_shiny_frame, calibration, location_offset, start_time)
    ask_again(target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)

def restart():
    keyboard.press(keybinds["start"])
    keyboard.press(keybinds["select"])
    keyboard.press(keybinds["a"])
    keyboard.press(keybinds["b"])
    advance_frame(60)
    keyboard.release(keybinds["start"])
    keyboard.release(keybinds["select"])
    keyboard.release(keybinds["a"])
    keyboard.release(keybinds["b"])

def open_save(first_start_press, second_start_press, third_start_press, save_press, opening_save_delay):
    advance_frame(first_start_press)
    press_controller(keybinds["start"])
    advance_frame(second_start_press)
    press_controller(keybinds["start"])
    advance_frame(third_start_press)
    press_controller(keybinds["start"])
    advance_frame(save_press)
    press_controller(keybinds["a"])
    advance_frame(opening_save_delay)

def open_menu(frames_to_pass=8):
    keyboard.press(keybinds["start"])
    advance_frame(frames_to_pass)
    keyboard.release(keybinds["start"])

def goto_party_menu(t1, t2):
    advance_frame(t1)
    press_controller(keybinds["down"])
    advance_frame(t2)
    press_controller(keybinds["a"])

def party_member_hms_menu(t1, t2):
    advance_frame(t1)
    keyboard.press(keybinds["a"])
    advance_frame(t2)
    keyboard.release(keybinds["a"])
    advance_frame(30)
    keyboard.press(keybinds["down"])
    advance_frame(20)
    keyboard.release(keybinds["down"])

def sweet_scent(shiny_frame, calibration, location_offset, start_time=0):
    global counter
    start_time = start_time
    if location_offset == "grass":
        location_offset = 261
    elif location_offset == "cave":
        location_offset = 269
    calibrated_shiny_frame = shiny_frame - calibration
    target_frame = calibrated_shiny_frame - location_offset
    frames_to_wait = target_frame - counter
    frames_to_wait = frames_to_wait - 0
    print(f"delay is {frames_to_wait}, target frame is {target_frame} and current frame is {counter}")
    if frames_to_wait > 0:
        advance_frame(frames_to_wait)
        print("alegid frame reached, pressing a to sweet scent")
        print(f"{counter} frames have passed sweetscent location offset is {location_offset} and calibration is {calibration} that added up equals {location_offset + calibration + counter - 4}")
    press_controller(keybinds["a"])
    


def ask_again(target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay):
    answer = input("Do you want to do it again? ")
    if answer in ["yes", "y", "Yes"]:
        init_cal = calibration
        calibration += float(input("We were off by how many frames? + or - how many frames? "))
        time.sleep(5)
        main(target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)
    else:
        ask_again(target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)

def press_controller(key):
    keyboard.press(key)
    advance_frame(4)
    keyboard.release(key)

shortcuts = {"ctrl+shift+alt+r": start}
nzksk.start_listener(shortcuts)
