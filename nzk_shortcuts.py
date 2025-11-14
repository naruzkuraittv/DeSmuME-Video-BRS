import threading
import keyboard
import queue
import time

cmd_queue = queue.Queue()

def command_worker(shortcut_functions):
    while True:
        cmd = cmd_queue.get()
        if callable(cmd):
            cmd()
        cmd_queue.task_done()

def enqueue_command(command_function):
    if command_function not in list(cmd_queue.queue):
        cmd_queue.put(command_function)

def hotkey_listener(shortcuts):
    for hotkey, command_function in shortcuts.items():
        keyboard.add_hotkey(hotkey, enqueue_command, args=[command_function])
    keyboard.wait()

def start_listener(shortcuts):
    threading.Thread(target=command_worker, args=(shortcuts,), daemon=True).start()
    hotkey_listener(shortcuts)

def stop_listener(shortcuts.*):
    #if no shortcuts set to stop, stop all
    if shortcuts == {}:
        keyboard.unhook_all()
    else:
        for hotkey, command_function in shortcuts.items():
            keyboard.remove_hotkey(hotkey)    
    
    """"_summary_
    #defining shortcuts, asume the function is coded in the file untill the last line, then call nzksk.start_listener(shortcuts)
    shortcuts = {
    "ctrl+shift+alt+r": start,
    "z": test,
    }
    nzksk.start_listener(shortcuts)
    nzksk.stop_listener("start", "test") # shouls work with nzksk.stop_listener() or nzksk.stop_listener({}) or nzksk.stop_listener()
    
    """