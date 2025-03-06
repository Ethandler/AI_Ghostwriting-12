import pyautogui
import time
import random
import string
import sys
import pyperclip
import os

# Constants
FAILSAFE_ENABLED = True
TYPING_DELAY_MIN = 0.004
TYPING_DELAY_MAX = 0.018
TYPO_PROBABILITY = 0.03
TYPO_CORRECTION_DELAY_MIN = 0.004
TYPO_CORRECTION_DELAY_MAX = 0.010
TYPO_RETYPE_DELAY_MIN = 0.047
TYPO_RETYPE_DELAY_MAX = 0.098
FOCUS_DELAY = 2  # Short delay for right-click menu actions

# Enable the failsafe: move your mouse to a corner to abort.
pyautogui.FAILSAFE = FAILSAFE_ENABLED

# Storage file for the text to be typed
TEXT_FILE = os.path.expanduser("~\\autotype_text.txt")

def get_wrong_character(correct_char):
    if correct_char.isalpha():
        letters = list(string.ascii_lowercase)
        try:
            letters.remove(correct_char.lower())
        except ValueError:
            pass
        return random.choice(letters)
    elif correct_char.isdigit():
        digits = list(string.digits)
        try:
            digits.remove(correct_char)
        except ValueError:
            pass
        return random.choice(digits)
    else:
        return random.choice(string.punctuation)

def type_text(text):
    for char in text:
        if char.strip() and random.random() < TYPO_PROBABILITY:
            wrong_char = get_wrong_character(char)
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(TYPO_CORRECTION_DELAY_MIN, TYPO_CORRECTION_DELAY_MAX))
            pyautogui.press('backspace')
            time.sleep(random.uniform(TYPO_RETYPE_DELAY_MIN, TYPO_RETYPE_DELAY_MAX))
            pyautogui.write(char)
        else:
            pyautogui.write(char)
        time.sleep(random.uniform(TYPING_DELAY_MIN, TYPING_DELAY_MAX))

def copy_text():
    # Retrieve text from clipboard and store it
    text = pyperclip.paste()
    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Copied text saved: {text}")

def start_typing():
    print("AutoType will start in 2 seconds. Focus the target window now...")
    time.sleep(FOCUS_DELAY)
    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            text_to_type = f.read()
        type_text(text_to_type)
        print("Finished AutoTyping.")
    else:
        print("No text found to type.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "copy":
            copy_text()
        elif sys.argv[1] == "type":
            start_typing()
