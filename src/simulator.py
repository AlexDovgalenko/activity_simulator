import pyautogui
import random
import time
import platform
from pynput import keyboard

# Safety feature
pyautogui.FAILSAFE = True

# Set to False to stop the script
running = True

# Define the key proces termination Key combination (e.g. Ctrl+Shift)
EXIT_KEYS = {
    keyboard.Key.shift,
    keyboard.Key.esc, 
}

MOVEMENT_DURATION = 0.2  # seconds
SLEEP_INTERVAL = 0.2  # seconds

# Track currently pressed keys
current_keys = set()

def on_press(key):
    current_keys.add(key)
    if all(k in current_keys for k in EXIT_KEYS):
        global running
        print("Exit key combination detected! Stopping simulation...")
        running = False
        # Return False to stop the listener
        return False

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass

def setup_keyboard_listener():
    # Start the keyboard listener in a separate thread
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.daemon = True
    listener.start()
    return listener

def activity_simulator():
    print("Activity simulation started.")
    interrupt_key_combination = " + ".join([key.name.upper() for  key in EXIT_KEYS])
    print(f"Press {interrupt_key_combination} to stop the simulation...")
    
    while running:
        try:
            # Get current mouse position
            current_x, current_y = pyautogui.position()
            action = random.choice(['move', 'scroll'])
            
            if action == 'move':
                # Move mouse slightly and return to original position
                offset_x = random.randint(-10, 10)
                offset_y = random.randint(-10, 10)
                
                pyautogui.moveRel(offset_x, offset_y, duration=MOVEMENT_DURATION)
                time.sleep(SLEEP_INTERVAL)
                pyautogui.moveTo(current_x, current_y, duration=MOVEMENT_DURATION)
                
            else:  # scroll
                pyautogui.scroll(-1)  # Scroll down slightly
                time.sleep(SLEEP_INTERVAL)
                pyautogui.scroll(1)   # Scroll back up
            
            # Wait between actions
            wait_time = random.uniform(30, 60)
            print(f"Performed {action}. Next action in {wait_time:.1f} seconds")
            
            # Check for exit conditions while waiting
            for _ in range(int(wait_time)):
                if not running:
                    break
                time.sleep(1)
                
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)  # Wait a bit and try again

if __name__ == "__main__":
    # Show platform info
    current_os = platform.system()
    print(f"Running on {current_os}")
    
    # Setup keyboard listener
    kb_listener = setup_keyboard_listener()
    
    # Run the main simulation
    try:
        activity_simulator()
    except KeyboardInterrupt:
        running = False
        print("\nScript stopped by user.")
    
    print("Keep-awake script has stopped.")