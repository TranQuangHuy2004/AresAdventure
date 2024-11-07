from GUI.home import home
from GUI.algorithm import alg
from GUI.visualization import visual

from tkinter import *
from ctypes import windll


def show_home():
    view1 = home(root, show_alg, show_visual)
    view1.display()


def show_alg():
    view2 = alg(root, show_home)
    view2.display()


def show_visual():
    view3 = visual(root, show_home)
    view3.display()


def main():
    windll.shcore.SetProcessDpiAwareness(1)
    global root
    root = Tk()

    show_home()

    root.mainloop()


if __name__ == "__main__":
    main()
