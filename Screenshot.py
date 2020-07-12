import pyautogui
import time
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    img = pyautogui.screenshot(f"{name}.png")
    img.show()

if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(
        frame,
        text = "Take Screenshot",
        command = screenshot)
    button.pack(side = tk.LEFT)
    close = tk.Button(
        frame,
        text = "Close",
        command = quit)
    close.pack(side=tk.LEFT)

    root.mainloop()
