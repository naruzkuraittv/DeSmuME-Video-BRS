#tas emerald
import keyboard
import time
import nzk_shortcuts as nzksk
import pyautogui

# must wait for 2 frames to pass to register input
# sweet scent costs 261 frames if not in cave, 269 if in cave

keybinds = { "a": "space", "b": "x", "l": "q", "r": "e", "start": "f", "select": "r", "up": "w", "down": "s", "left": "a", "right": "d" }
number_of_party_members = 5
sweet_scent_slot = 1
glitch_mon_slot = 5
sweet_scent_move_hm_slot = 1
game_start_party_slot = 1
delay = 0
frames_passed = 0
current_slot = game_start_party_slot
shiny_frame = 3672
offset = 492 - 447
location_offset = 0
def start():
############# things you might change :D ################

    global shiny_frame, offset, sweet_scent_move_hm_slot, game_start_party_slot, delay, frames_passed, current_slot, start_time
    #if ctrl shift alt or r is pressed wait .1 seconds then run start, else run main
    if keyboard.is_pressed("ctrl+shift+alt+r"):
        time.sleep(.1)
        start()
    else:
        #mouseclick
        pyautogui.click()
        time.sleep(1)
        main()
        
def test():
    print("test")
def main():
    global shiny_frame, offset, sweet_scent_move_hm_slot, game_start_party_slot, delay, frames_passed, current_slot, start_time

    start_time = time.time()
    restart()
    open_save()
    open_menu()
    goto_party()
    party_member_hms_menu()
    goto_sweetscent()
    sweet_scent()

    #GET input how many frames off were you? + or - 1
    last_encountered = int(input("what frame did you hit")) 
    offset = shiny_frame - last_encountered
    print(f"offset is {offset}")
    input("want to do it again? y/n")
    if input == "y":
        print("doing it again, in 2 seconds")
    else:
        return

def press_controller(key):
    #presses a key on the controller 
    global frames_passed
    print("pressing " + key)
    keyboard.press(key)
    advance_frame(4)
    keyboard.release(key)
    print("released " + key)
    return frames_passed
def open_menu():
    print("opening menu")
    keyboard.press(keybinds["start"])
    advance_frame(8)
    keyboard.release(keybinds["start"])
    print("menu opened")
    
def goto_party():
    print("going to party in the menu")
    advance_frame(20)
    press_controller(keybinds["down"])
    advance_frame(20)
    press_controller(keybinds["a"])
    print("party opened") 
    

def advance_frame(frames_to_pass):
    global frames_passed
    frames_to_pass = int(frames_to_pass)

    for i in range(frames_to_pass):
        n = frames_to_pass / 60 
        time.sleep(n)
        print(frames_passed)
        
    return frames_passed

def pause():
    keyboard.press("p")
    time.sleep(1)
    keyboard.release("p")
    time.sleep(1)
    print("paused")
    
def restart(): #passes 60 frames aswell
    keyboard.press(keybinds["start"])
    keyboard.press(keybinds["select"])
    keyboard.press(keybinds["a"])
    keyboard.press(keybinds["b"])
    time.sleep(1) # 60 frames passed
    keyboard.release(keybinds["start"])
    keyboard.release(keybinds["select"])
    keyboard.release(keybinds["a"])
    keyboard.release(keybinds["b"])
    print("restarted")

    
def open_save():
    print("opening save")
    advance_frame(290)
    press_controller(keybinds["start"])
    advance_frame(40)
    press_controller(keybinds["start"])
    advance_frame(40)
    press_controller(keybinds["start"])
    advance_frame(90)
    press_controller(keybinds["a"])
    advance_frame(90)
    print("save opened")
def what_time_is_it():
    print("what time is it")
    print(time.time())
    start_time = time.time()


def party_member_hms_menu():
    print("opening party member hms menu")
    advance_frame(90)
    keyboard.press(keybinds["a"])
    advance_frame(10)
    keyboard.release(keybinds["a"])
    
def goto_sweetscent():
    print("going to sweet scent in the hms menu")
    advance_frame(25)
    press_controller(keybinds["down"])
    
def sweet_scent():
    global frames_passed
    global shiny_frame
    global current_time
    global start_time
    global delay
    global offset
    global location_offset
    #get current time in seconds
    current_time = time.time()
    time_passed = current_time - start_time
    time_passed_in_frames = time_passed * 60
    shiny_frame = shiny_frame - location_offset
    remaining_frames = shiny_frame - time_passed_in_frames
    delay = remaining_frames - offset

    print(f"delay is {delay}, target frame is {shiny_frame} and current frame is {frames_passed}")
    advance_frame(delay)
    press_controller(keybinds["a"])
    

def start():
    #if ctrl shift alt or r is pressed wait .1 seconds then run start, else run main
    if keyboard.is_pressed("ctrl+shift+alt+r"):
        time.sleep(.1)
        start()
    else:
        #mouseclick
        pyautogui.click()
        time.sleep(1)
        main()
def test():
    print("test")

shortcuts = {
    "ctrl+shift+alt+r": start,
    "z": test,
}
nzksk.start_listener(shortcuts)
