    
def activate_rng_glitch():
    press_controller(keybinds["a"])
    advance_frame(120)
    press_controller(keybinds["b"])
    advance_frame(30)
    press_controller(keybinds["b"])
    advance_frame(30)
    press_controller(keybinds["left"])
    advance_frame(30)
    press_controller(keybinds["a"])
    advance_frame(30)
    press_controller(keybinds["down"])
    advance_frame(30)
    press_controller(keybinds["a"])
    
def goto_party_slot(current_slot, target_slot, number_of_party_members):
    if current_slot == target_slot:
        print("current slot is the target slot")
    elif current_slot != target_slot:
        print(f"current slot {current_slot} is not target slot {target_slot}")
        if current_slot < target_slot and current_slot <= number_of_party_members:
            print(f"current slot {current_slot} is less than target slot {target_slot}")
            advance_frame(30)
            press_controller(keybinds["down"])
            goto_party_slot(current_slot + 1, target_slot, number_of_party_members)
        elif current_slot > target_slot and current_slot > 1:
            print(f"current slot {current_slot} is greater than target slot {target_slot}")
            advance_frame(30)
            press_controller(keybinds["up"])
            goto_party_slot(current_slot - 1, target_slot, number_of_party_members)
        elif current_slot == number_of_party_members + 1 and target_slot != number_of_party_members + 1:
            print(f"current slot {current_slot} is the exit slot")
            advance_frame(30)
            press_controller(keybinds["up"])
            goto_party_slot(number_of_party_members, target_slot, number_of_party_members)
        else:
            print(f"current slot {current_slot} target slot {target_slot}")
            print("if the current slot is not the target slot something went wrong im not sure why")
    print(f"current slot {current_slot} target slot {target_slot}")
    print("if the current slot is not the target slot something went wrong im not sure why")
    return
def go_to_exit(current_slot, number_of_party_members):
    advance_frame(30)
    exit_slot = number_of_party_members + 1
    go_to_exit(current_slot, exit_slot , number_of_party_members)
    
def leave_party_menu(party_slot, number_of_party_members):
    advance_frame(30)
    leave_party_menu(party_slot + 1, number_of_party_members)