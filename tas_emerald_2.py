#tas emerald
import keyboard
import time
import nzk_shortcuts as nzksk
import pyautogui
##########################################################################################
#                               things end user might edit                               #
##########################################################################################
keybinds = { "a": "space", "b": "x", "l": "q", "r": "e", "start": "f", "select": "r", "up": "w", "down": "s", "left": "a", "right": "d" }
counter = 0
def start(): # takes all teh variables and passes to everything that "would" br global
    
    location_offset = 0
    first_start_press = 290  
    second_start_press = 40
    third_start_press = 40
    save_press = 60
    opening_save_delay= 80
    #location_offset = "grass"
    location_offset = "cave"
    ##############################################
    calibration = int(-66) #the bigger the target the bigger the calibration need math equiasion for auto cal but for now manual
    # if 1180 math ??? = -46 or -45 lets try to use -45.5? in regular grass / surfing
    # if 1180 math ??? = -60 = surfing
    target_or_shiny_frame = 6943
    ##############################################
    # if ctrl alt shift or r is pressed run sart
    if keyboard.is_pressed("ctrl") or keyboard.is_pressed("alt") or keyboard.is_pressed("shift") or keyboard.is_pressed("r"):
       time.sleep(1)
       start()
    else:    
        main( target_or_shiny_frame,calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)

##########################################################################################
#                                           main                                         #
##########################################################################################

def main(target_or_shiny_frame,calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay):
    counter = 0
    start_time = time.time()
    #add our target frames in 1/60ths of a second to second to get our target time
    restart() # done 60 frames passed
    #if not emerland delay open save press()
    open_save(first_start_press, second_start_press, third_start_press, save_press, opening_save_delay) #done
    open_menu() #done
    goto_party_menu(20, 20) #done
    party_member_hms_menu(74, 10) #done
    #goto_sweetscent()
    sweet_scent(target_or_shiny_frame, calibration, location_offset, start_time) #
    ask_again( target_or_shiny_frame,calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)

##########################################################################################
#                               definitions of main                                      #
##########################################################################################
def restart(): #passes 60 frames aswell
    keyboard.press(keybinds["start"])
    keyboard.press(keybinds["select"])
    keyboard.press(keybinds["a"])
    keyboard.press(keybinds["b"])
    advance_frame(60)
    keyboard.release(keybinds["start"])
    keyboard.release(keybinds["select"])
    keyboard.release(keybinds["a"])
    keyboard.release(keybinds["b"])
    print("restarted")
    
def open_save(first_start_press, second_start_press, third_start_press, save_press, opening_save_delay= 90):
    print("opening save")
    advance_frame(first_start_press)
    press_controller(keybinds["start"])
    advance_frame(second_start_press)
    press_controller(keybinds["start"])
    advance_frame(third_start_press)
    press_controller(keybinds["start"])
    advance_frame(save_press)
    press_controller(keybinds["a"])
    advance_frame(opening_save_delay)
    print("save opened")
    total_time_passed = first_start_press + second_start_press + third_start_press + save_press + opening_save_delay
    print(f"total frames passed is {total_time_passed}")
    
def open_menu(frames_to_pass=8):
    print("opening menu")
    keyboard.press(keybinds["start"])
    advance_frame(frames_to_pass)
    keyboard.release(keybinds["start"])
    print("menu opened")
    
def goto_party_menu(t1, t2):
    print("going to party in the menu")
    advance_frame(t1)
    press_controller(keybinds["down"])
    advance_frame(t2)
    press_controller(keybinds["a"])
    print("party opened") 
    
def party_member_hms_menu(t1, t2):
    print("opening party member hms menu")
    advance_frame(t1)
    keyboard.press(keybinds["a"])
    advance_frame(t2)
    keyboard.release(keybinds["a"])
    advance_frame(30)
    keyboard.press(keybinds["down"])
    advance_frame(20)
    keyboard.release(keybinds["down"])

def sweet_scent(shiny_frame, calibration, location_offset, start_time):
    if location_offset == "grass":
        location_offset = 261
    elif location_offset == "cave":
        location_offset = 269
    print
    current_time = time.time()
    how_many_seconds_have_passed = current_time - start_time
    how_many_frames_have_passed = how_many_seconds_have_passed + 1
    how_many_frames_have_passed = how_many_seconds_have_passed * 60
    calibrated_shiny_frame = float(shiny_frame) - float(calibration)
    target_frame = float(calibrated_shiny_frame) - float(location_offset)
    time_to_wait = float(target_frame) - float(how_many_frames_have_passed)

    print(f"delay is {calibration}, target frame is {shiny_frame} and current frame is {how_many_frames_have_passed}\n, {how_many_frames_have_passed} is how many frames have passed, now waiting {time_to_wait} frames to use sweet scent")
    advance_frame(time_to_wait)
    press_controller(keybinds["a"])
    print("sweet scent used")

def ask_again( target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay):
    print("do you want to do it again?")
    answer = input()
    if answer == "yes" or answer == "y" or answer == "Yes":
            init_cal = calibration
            calibration = float(calibration) + float(input(" we were off by how many frames? \n+ or - how many frames? \n"))
            print(f"cool, delay is now ({calibration}) Original was ({init_cal}) to the delay")
            time.sleep(5)
            main( target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)

    else:
        ask_again( target_or_shiny_frame, calibration, location_offset, first_start_press, second_start_press, third_start_press, save_press, opening_save_delay)



##########################################################################################
#                               definitions of QOL functions                             #
##########################################################################################
def pause():
    keyboard.press("p")
    advance_frame(60)
    keyboard.release("p")
    advance_frame(60)
    print("paused")

def press_controller(key):
    #presses a key on the controller 
    print("pressing " + key)
    keyboard.press(key)
    advance_frame(4)
    keyboard.release(key)
    print("released " + key)

def wait_for_frames(frames, fps=60):
    duration = frames / fps
    busy_wait(duration)


        
def advance_frame(frames_to_pass, fps=60):
    duration = frames_to_pass / fps
    start_time = time.perf_counter()
    while (time.perf_counter() - start_time) < duration:
        pass


def press_controller(key):
    #presses a key on the controller 
    print("pressing " + key)
    keyboard.press(key)
    advance_frame(4)
    keyboard.release(key)
    print("released " + key)
import time

def busy_wait(duration):
    # Capture the start time
    start_time = time.time()
    
    # Continue looping until the current time - start time is less than the duration
    while (time.time() - start_time) < duration:
        pass  # Do nothing, just loop



def test ():
    print("test")
    
shortcuts = { #figure out how to add variables to shortcuts in the future
    "ctrl+shift+alt+r": start,
    "z": test,
}
nzksk.start_listener(shortcuts)
