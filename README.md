# PRODIGY_CS_04
Created a basic keylogger program that record and logs keystrokes. Focused on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

## Disclaimer

## This keylogger script is provided for educational purposes only. I do not endorse or encourage any unauthorized or malicious use of keyloggers. The users assume full responsibility for their actions while using this script.

## Ethical Considerations

It's important to use this keylogger script responsibly and ethically. Keyloggers can be used for various purposes, including debugging, personal use, or monitoring computer activity with proper consent. However, using keyloggers without authorization or for malicious purposes can violate privacy laws and regulations.

Always obtain proper authorization before deploying keyloggers on any system. Ensure that users are aware of the keylogger's presence and its purpose, and respect their privacy rights.

# Simple Keylogger

This is a basic Python keylogger program that records and logs keystrokes. It uses the `pynput` library to monitor keyboard inputs and saves the keystrokes to a log file.

## Usage

1. Install the required library:

    ```
    pip install pynput
    ```

2. Run the `keylogger.py` script.

3. The program will start logging keystrokes and save them to a file named `keystroke_log.txt`.

4. Press the 'Escape' key to stop the keylogger.

## Requirements

- Python 3.x
- `pynput` library

## How it Works

The keylogger program consists of the following components:

- **`keylogger.py`**: This is the main Python script that contains the keylogger implementation.

    - It imports the necessary modules, including `pynput.keyboard.Key` and `pynput.keyboard.Listener`.
    
    - The program defines two functions: `on_press` and `on_release`.
    
    - `on_press`: This function gets called when a key is pressed. It writes the pressed key to the log file.
    
    - `on_release`: This function gets called when a key is released. If the 'Escape' key is pressed, it stops the listener.
    
    - The script sets up a listener to monitor keystrokes using `pynput.keyboard.Listener`.
    
    - The listener runs until the 'Escape' key is pressed, at which point the program terminates.

- **`keystroke_log.txt`**: This is the log file where the keystrokes are recorded. Each keystroke is appended to this file as it is pressed.
