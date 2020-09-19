import tkinter as tk
import _tkinter
from tkinter import ttk

class HelloApp:

    def __init__(self, root):
        self.label = tk.Label(root, text='Hello user')
        self.label.grid(row=0, column=0, columnspan=2)
        self.button_texas = ttk.Button(root, text='Texas', command=self.texas_hello)
        self.button_texas.grid(row=1, column=0)
        self.button_hawaii = ttk.Button(root, text='Hawaii', command=self.hawaii_hello)
        self.button_hawaii.grid(row=1, column=1)

####################### command hendler ###############################
    def texas_hello(self):
        self.label['text'] = 'Howdy, user'

    def hawaii_hello(self):
        self.label.config(text='Aloha, user')
########################################################################


def main():
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__": main()
