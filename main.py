# main.py

from tkinter import Tk
from scr1.interfaces.gui import BibliotecaApp

if __name__ == "__main__":
    root = Tk()
    app = BibliotecaApp(root)
    root.mainloop()
