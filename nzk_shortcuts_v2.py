import threading
import keyboard
import queue
import time

cmd_queue = queue.Queue()

def help():
    print("""
# Usage Example coz im hella forgetfull
def test():
    print("test")
def start():
    print("start")
shortcuts = {
    "ctrl+shift+alt+r": start,
    "z": test,
}
nzksk.start_listener(shortcuts)
start_listener(shortcuts)
stop_listener()  # Stops all listeners
""")
    
def command_worker():
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
        keyboard.add_hotkey(hotkey, enqueue_command, args=(command_function,))
    keyboard.wait()

def start_listener(shortcuts):
    threading.Thread(target=command_worker, daemon=True).start()
    hotkey_listener(shortcuts)

def stop_listener(shortcuts=None):
    if shortcuts is None or shortcuts == {}:
        keyboard.unhook_all()
    else:
        for hotkey in shortcuts.keys():
            keyboard.remove_hotkey(hotkey)
