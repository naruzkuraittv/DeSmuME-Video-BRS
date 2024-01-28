import tkinter as tk
from tkinter import simpledialog
import keyboard
import time

# Mapping of DS buttons to keyboard keys
ds_k= {
    'up': 'w',
    'left': 'a',
    'down': 's',
    'right': 'd',
    'b': 'tab',
    'a': 'space',
    'y': 'q',
    'x': 'e',
    'start': 'r',
    'select': 'f',
    'L': 't',
    'R': 'g'
}
def next_seed(current_seed):
    a = (0x41C6 * (current_seed % 65536) + (current_seed >> 16) * 0x4E6D) & 0xFFFFFFFF
    b = (0x4E6D * (current_seed % 65536) + (a % 65536) * 65536 + 0x6073) & 0xFFFFFFFF
    next_seed = b % 4294967296
    return next_seed
# print the value of up in ds_k
#print(f"up: {ds_k['up']}")
#number of advances 
no_advances = 2912 - 1647
#if i do ds_pres("up", 101, 0.001) this will press the keybord value related to the ds button up 101 times with a delay of 0.001 seconds
def ds_press(key, times, delay=0.05, delay2=0.05):  # Adjusted delay
    for _ in range(times):
        # keyboard press and hold for delay
        keyboard.press(ds_k[key])
        time.sleep(delay)
        keyboard.release(ds_k[key])
        time.sleep(delay)
        print(f"ds_press: {ds_k[key]}")

def flipflop(no_advances):
    count = 0
    for _ in range(no_advances):
        if count < no_advances:
            ds_press("down", 1)
            count = count + 1
            time.sleep(0.05)  # Adjusted delay
            if count < no_advances:
                ds_press("up", 1)
                count = count + 1
time.sleep(4)
flipflop(no_advances)
