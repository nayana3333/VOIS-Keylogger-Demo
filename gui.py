import tkinter as tk
import threading
import keylogger

def start():
    t = threading.Thread(target=keylogger.start_keylogger)
    t.start()

root = tk.Tk()
root.title("Keylogger Page")
root.geometry("250x300")
root.configure(bg="lightgreen")

label = tk.Label(
    root,
    text="Keylogger Project",
    font=("Verdana", 12, "bold"),
    bg="lightgreen"
)
label.pack(pady=30)

button = tk.Button(
    root,
    text="Start Keylogger",
    command=start
)
button.pack(pady=20)

root.mainloop()
