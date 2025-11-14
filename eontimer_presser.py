#ask for delay time. 60 frames per second, delay time = #of frames to wait. wait 2 secodns after asking then press space wait 2 seconds, then press shift then wait 1 second then shift then a then space then s then wait untill the rest of the frames have passed then press space again
import time
import keyboard
import time
import keyboard

def press_and_wait(key, wait_frames):
    print(f"Pressing {key}")
    keyboard.press(key)
    minimum_key_press_time_frames = 10
    time.sleep(minimum_key_press_time_frames / 60)  # Convert frames to seconds
    keyboard.release(key)
    time.sleep(wait_frames / 60)  # Convert frames to seconds
    print(f"{key} pressed and waited for {wait_frames} frames")
    return minimum_key_press_time_frames + wait_frames

def main():
    delay_frames = int(input("Enter the delay time in frames: "))
    
    if delay_frames < 120:
        print("The delay time is too short, it needs to be at least 120 frames for a 2-second wait.")
        return

    print("Waiting for a few seconds to make sure you are on the game")
    time.sleep(2)  # Initial wait before starting the sequence

    total_frames = 0  # Initialize total frames

    # Sequence of actions based on your description
    total_frames += press_and_wait("space", 120)  # Press space and wait 120 frames
    print(f"Total frames passed: {total_frames}")
    total_frames += press_and_wait("shift", 120)  # Wait 120 frames, then press shift
    print(f"Total frames passed: {total_frames}")
    total_frames += press_and_wait("shift", 60)  # Wait 60 frames, then press shift again
    print(f"Total frames passed: {total_frames}")
    total_frames += press_and_wait("a", 0)      # Immediately press 'a'
    print(f"Total frames passed: {total_frames}")
    total_frames += press_and_wait("space", 0)  # Immediately press space
    print(f"Total frames passed: {total_frames}")

    remaining_frames = delay_frames - total_frames
    if remaining_frames < 0:
        print("Error: The total frames spent pressing keys and waiting has exceeded the delay frames.")
        return

    total_frames += press_and_wait("s", remaining_frames)  # Wait until the rest of the frames have passed, then press 's'
    print(f"Total frames passed: {total_frames}")
    total_frames += press_and_wait("space", 0)  # Finally, press space again
    print(f"Total frames passed: {total_frames}")

main()