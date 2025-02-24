import pyautogui
import time
import random

def auto_type(text):
    """Waits 5 seconds to focus the screen, then simulates typing."""
    print("\nSwitch to the target window... Typing will start in 5 seconds.")
    time.sleep(5)  # Pause to allow screen focus

    print("\nAuto-typing text...")
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.02, 0.1))  # Random delay for natural typing
