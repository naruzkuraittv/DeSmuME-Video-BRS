def next_seed(current_seed):
    a = (0x41C6 * (current_seed % 65536) + (current_seed >> 16) * 0x4E6D) & 0xFFFFFFFF
    b = (0x4E6D * (current_seed % 65536) + (a % 65536) * 65536 + 0x6073) & 0xFFFFFFFF
    next_seed = b % 4294967296
    return next_seed

def do_you_want_to_calc_next_seed_qm():
    global current_seed
    global next_seed_value
    global next_seed
    response = input("Do you want to calculate the next seed? (y/n)")
    if response == "y":
        next_seed(current_seed)
        do_you_want_to_calc_next_seed_qm()
    else:
        do_you_want_to_calc_next_seed_qm()
def get_init_seed():  
    current_seed = input("Current Seed: ")
    current_seed = int(current_seed, 16)  # Convert the input to an integer
    next_seed_value = next_seed(current_seed)
    print(f"Next Seed: {next_seed_value:08X}")
current_seed = 0
next_seed_value = 0

get_init_seed()

