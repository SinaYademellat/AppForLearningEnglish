import tkinter as tk

COUNT = 0

def count():
    global COUNT
    COUNT += 1
    label.configure(text=f"Count: {COUNT}")

root = tk.Tk()

label = tk.Label(root, text="Count: 0")
button = tk.Button(root, text="Count", command=count)
enable_btn = tk.Button(root, text="Enable Count", command=lambda: button.configure(state="normal"))
disable_btn = tk.Button(root, text="Disable Count", command=lambda: button.configure(state="disabled"))

label.pack(side="top", fill="x", pady=20)
button.pack(side="left", padx=(0,10))
disable_btn.pack(side="right")
enable_btn.pack(side="right")

root.bind_all("<Return>", lambda event: button.invoke())

root.mainloop()