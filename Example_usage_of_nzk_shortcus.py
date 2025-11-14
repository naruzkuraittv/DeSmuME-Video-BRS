import nzk_shortcuts as nzksk

def set_rng_init_time():
    print("Reset RNG")

def open_new_emulator():
    print("Open New Emulator")

def get_emulator_title():
    print("Get Emulator Title")

# Map hotkeys directly to functions
shortcuts = {
    "ctrl+shift+alt+r": set_rng_init_time,
    "ctrl+shift+alt+e": open_new_emulator,
    "ctrl+alt+shift+s": get_emulator_title
}
nzksk.start_listener(shortcuts)
