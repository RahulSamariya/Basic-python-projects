# Save as demo_keys.py and run:
# python "c:\Users\DELL\Desktop\Project Files\Basic python projects\Python calculator\demo_keys.py"

import tkinter as tk

root = tk.Tk()
root.title("Key binding demo")

def on_root_key(event):
    print("root.bind: keysym=", event.keysym, " char=", repr(event.char))

def on_all_key(event):
    print("bind_all: keysym=", event.keysym, " char=", repr(event.char))

# bind to root (only active when root has focus)
root.bind('<Key>', on_root_key)

# bind to whole app (always receives keys)
root.bind_all('<Key>', on_all_key)

tk.Label(root, text="Click the Entry or click the buttons to change focus.\n"
         "Press keys and watch the console output.").pack(padx=10, pady=10)

entry = tk.Entry(root)
entry.pack(padx=10, pady=5)
entry.insert(0, "Click me then type")

btn_focus_root = tk.Button(root, text="Focus root (root.focus_set())",
                           command=lambda: root.focus_set())
btn_focus_root.pack(fill='x', padx=10, pady=2)

btn_focus_entry = tk.Button(root, text="Focus entry (entry.focus_set())",
                            command=lambda: entry.focus_set())
btn_focus_entry.pack(fill='x', padx=10, pady=2)

root.mainloop()