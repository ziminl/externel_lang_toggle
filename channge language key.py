import pyautogui
import time
import keyboard  # Import the keyboard library

def change_keyboard_language_to_english():
    # Send Alt+Shift to switch keyboard language
    pyautogui.keyDown('alt')
    pyautogui.press('shift')
    pyautogui.keyUp('alt')

# Define a function to be called when the F9 key is pressed
def on_f9_pressed(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'f9':
            change_keyboard_language_to_english()

# Register the F9 key press event
keyboard.on_press(on_f9_pressed)

# You may need to add a time delay to allow the language switch to take effect
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the script when you press Ctrl+C
    pass

# Unregister the F9 key press event when done
keyboard.unhook_all()

