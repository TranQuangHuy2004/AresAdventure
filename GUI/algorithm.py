from maze import Maze
from output_file import output
from GUI.set_up_window import setup_window

from tkinter import *
from tkinter import messagebox
import glob
import os
import time


class alg:
    def __init__(self, root, switch_to_view1):
        self.root = root
        self.switch_to_view1 = switch_to_view1
        self.text_box = None
        self.canvas = None
        self.tile_size = 30
        self.width = 510
        self.height = 300

    def display(self):
        # Clear the window and show the content of alg
        for widget in self.root.winfo_children():
            widget.destroy()
        setup_window(self.root, self.width, self.height, "white")

        self.canvas = Canvas(self.root, width=self.width,
                             height=self.height, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.decorate_bg()
        self.add_text()
        self.add_text_box()
        self.add_button()

    def decorate_bg(self):
        row = int(self.height/self.tile_size)
        col = int(self.width/self.tile_size)
        for i in range(row):
            for j in range(col):
                if i % 2 == 0:
                    x1 = 2 * j * self.tile_size
                    x2 = x1 + 2 * self.tile_size
                else:
                    x1 = 2 * j * self.tile_size - self.tile_size
                    x2 = x1 + 2 * self.tile_size

                y1 = i * self.tile_size
                y2 = y1 + self.tile_size

                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="maroon", outline="black", width=2)

    def add_text(self):
        self.canvas.create_text(
            125, 73, text="Enter your file name:", fill="yellow", font=("Bell MT", 13))
        self.canvas.create_text(
            250, 250, text="*This will write the results of 4 search algorithms to output file .txt", fill="yellow", font=("Bell MT", 11, "italic"))
        self.canvas.create_text(
            250, 270, text="*And please be patient", fill="yellow", font=("Bell MT", 11, "italic"))

    def add_text_box(self):
        inputtxt = Entry(self.root, width=20, bg="gray",
                         fg="yellow", font=("Bell MT", 13))
        inputtxt.place(x=240, y=60)
        inputtxt.bind("<Return>", self.run_button_click)
        self.text_box = inputtxt

    def add_button(self):
        run_button = Button(self.root,
                            text="Run",
                            command=lambda: self.run_button_click(""),
                            activebackground="darkgray",
                            activeforeground="yellow",
                            anchor="center",
                            bd=3,
                            bg="gray",
                            cursor="hand2",
                            disabledforeground="gray",
                            fg="black",
                            font=("Bell MT", 12, "bold"),
                            height=1,
                            width=6,
                            justify="center",
                            overrelief="raised",
                            wraplength=200)
        run_button.place(x=213, y=130)

        back_button = Button(self.root,
                             text="Exit",
                             command=self.switch_to_view1,
                             activebackground="darkgray",
                             activeforeground="yellow",
                             anchor="center",
                             bd=3,
                             bg="gray",
                             cursor="hand2",
                             disabledforeground="gray",
                             fg="black",
                             font=("Bell MT", 12, "bold"),
                             height=1,
                             width=6,
                             justify="center",
                             overrelief="raised",
                             wraplength=200)
        back_button.place(x=213, y=180)

    def run_button_click(self, event):
        filename = self.text_box.get()
        if filename == "":
            messagebox.showwarning("Error", "Please enter a file's name")
            return

        # Check the existence of files with input-XX.txt format
        files = glob.glob("input/input-*.txt")
        list_filenames = [os.path.splitext(os.path.basename(file))[
            0] for file in files]

        if filename not in list_filenames:
            messagebox.showwarning("Error", "File not found")
            return

        filename = "input/" + filename + ".txt"

        maze = Maze()
        maze.read_from_file(filename)
        outputname = filename.replace("input", "output")
        solutionname = filename.replace("input", "solution")
        output(maze, outputname, solutionname)

        messagebox.showinfo("Notification", "Finished")
