import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")





if __name__ == "__main__":
    root = tk.TK()
    App = ParentWindow(root)
    root.mainloop()