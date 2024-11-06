from tkinter import *
from tkinter import messagebox
import glob
import os
from GUI.set_up_window import setup_window
from maze import Maze


class visual():
    def __init__(self, root, switch_to_view1):
        self.root = root
        self.switch_to_view1 = switch_to_view1
        self.animation_id = None  # To keep track of the after() event
        self.canvas = None
        self.maze = None
        self.tile_size = 30
        self.scrollable_frame = None
        self.input = "input-01"
        self.list_solutions = None
        self.solution = None
        self.counter = []
        self.background = None

    def display(self):
        # Clear the window and show the content of visual
        for widget in self.root.winfo_children():
            widget.destroy()

        self.maze = Maze()
        filename = "input/" + self.input + ".txt"
        self.maze.read_from_file(filename)

        self.list_solutions = read_solution_file(self.input)
        self.solution = self.list_solutions[0]

        # max width and max height of the maze itself
        w, h = self.maze.max_width_max_height()

        # max width and height for window
        window_width = max(630, w * self.tile_size + 180)
        window_height = h * self.tile_size + 300
        setup_window(self.root, int(window_width),
                     int(window_height), "white")

        # Set up background
        background = Canvas(self.root, width=int(window_width),
                            height=int(window_width), bg="white", highlightthickness=0)
        background.place(x=0, y=0)
        self.decorate_bg(background, int(window_width), int(window_height))

        # Create a canvas and set up the maze
        self.canvas = Canvas(self.root, width=w * self.tile_size, height=h * self.tile_size,
                             bg="white", highlightthickness=0)
        self.canvas.place(x=int((window_width - w*self.tile_size)/2),
                          y=150)

        # Display the initial maze
        self.maze.display_maze(self.canvas, self.tile_size)
        # Display label and button
        self.counter = self.add_label(window_width // 2)
        self.add_button(window_width, window_height)

    def decorate_bg(self, background, width, height):
        row = height // self.tile_size
        col = width // self.tile_size
        for i in range(row):
            for j in range(col // 2 + 1):
                if i <= 2 or i >= row - 3:
                    if i % 2 == 0:
                        x1 = 2 * j * self.tile_size
                        x2 = x1 + 2 * self.tile_size
                    else:
                        x1 = 2 * j * self.tile_size - self.tile_size
                        x2 = x1 + 2 * self.tile_size
                    y1 = i * self.tile_size
                    y2 = y1 + self.tile_size
                    background.create_rectangle(
                        x1, y1, x2, y2, fill="maroon", outline="black", width=2)
                elif col % 2 == 1 and (j == 0 or j == (col // 2)):
                    if i % 2 == 0:
                        x1 = 2 * j * self.tile_size
                        x2 = x1 + 2 * self.tile_size
                    else:
                        x1 = 2 * j * self.tile_size - self.tile_size
                        x2 = x1 + 2 * self.tile_size

                    y1 = i * self.tile_size
                    y2 = y1 + self.tile_size
                    background.create_rectangle(
                        x1, y1, x2, y2, fill="maroon", outline="black", width=2)
                elif col % 2 == 0 and (j == 0 or j == (col // 2)):
                    if i % 2 == 0:
                        if j == 0:
                            x1 = 2 * j * self.tile_size
                            x2 = x1 + 2 * self.tile_size
                        else:
                            x1 = 2 * (j - 1) * self.tile_size
                            x2 = x1 + 2 * self.tile_size
                    else:
                        x1 = 2 * j * self.tile_size - self.tile_size
                        x2 = x1 + 2 * self.tile_size

                    y1 = i * self.tile_size
                    y2 = y1 + self.tile_size
                    background.create_rectangle(
                        x1, y1, x2, y2, fill="maroon", outline="black", width=2)

    def add_label(self, x_coor):
        step = Label(self.root,
                     text="Steps:",
                     anchor=CENTER,
                     bg="gray",
                     height=1,
                     width=5,
                     bd=3,
                     font=("Bell MT", 15, "bold"),
                     fg="black",
                     justify="center",
                     relief=RAISED,
                     wraplength=100
                     )
        step.place(x=x_coor - 240, y=26)

        step_counter = Label(self.root,
                             text="0",
                             bg="gray",
                             height=1,
                             width=7,
                             bd=3,
                             font=("Bell MT", 15, "bold"),
                             fg="black",
                             justify="center",
                             relief=RAISED,
                             wraplength=100
                             )
        step_counter.place(x=x_coor - 140, y=26)

        cost = Label(self.root,
                     text="Costs: ",
                     anchor=CENTER,
                     bg="gray",
                     height=1,
                     width=5,
                     bd=3,
                     font=("Bell MT", 15, "bold"),
                     fg="black",
                     justify="center",
                     relief=RAISED,
                     wraplength=100
                     )
        cost.place(x=x_coor + 30, y=26)

        cost_counter = Label(self.root,
                             text="0",
                             bg="gray",
                             height=1,
                             width=7,
                             bd=3,
                             font=("Bell MT", 15, "bold"),
                             fg="black",
                             justify="center",
                             relief=RAISED,
                             wraplength=100
                             )
        cost_counter.place(x=x_coor + 130, y=26)

        return [step_counter, cost_counter]

    def add_button(self, w2, h2):
        x_coordinate = int((w2-577)/2)
        input_button = Button(self.root,
                              text=self.input,
                              command=lambda: self.show_input_options(
                                  input_button),
                              activebackground="darkgray",
                              activeforeground="yellow",
                              anchor="center",
                              bd=3,
                              bg="gray",
                              cursor="hand2",
                              disabledforeground="lightgray",
                              fg="black",
                              font=("Bell MT", 12, "bold"),
                              height=1,
                              width=10,
                              justify="center",
                              overrelief="raised",
                              wraplength=200)
        input_button.place(x=x_coordinate, y=h2-60)

        alg_button = Button(self.root,
                            text="BFS",
                            command=lambda: self.show_alg_options(alg_button),
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
                            width=10,
                            justify="center",
                            overrelief="raised",
                            wraplength=200)
        alg_button.place(x=x_coordinate + 150, y=h2-60)

        start_button = Button(self.root,
                              text="START",
                              command=lambda: self.animate_solution(
                                  start_button, input_button),
                              activebackground="darkgray",
                              activeforeground="yellow",
                              anchor="center",
                              bd=3,
                              bg="gray",
                              cursor="hand2",
                              disabledforeground="lightgray",
                              fg="black",
                              font=("Bell MT", 12, "bold"),
                              height=1,
                              width=10,
                              justify="center",
                              overrelief="raised",
                              wraplength=200)
        start_button.place(x=x_coordinate + 300, y=h2-60)

        back_button = Button(self.root,
                             text="Exit",
                             command=self.stop_animation,
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
                             width=10,
                             justify="center",
                             overrelief="raised",
                             wraplength=200)
        back_button.place(x=x_coordinate + 450, y=h2-60)

    def show_alg_options(self, alg_button):
        # Remove existing scrollable frame if present
        if self.scrollable_frame:
            self.scrollable_frame.destroy()

        # Create a new frame for the list of buttons
        self.scrollable_frame = Frame()
        self.scrollable_frame.place(
            x=alg_button.winfo_x(), y=alg_button.winfo_y()-alg_button.winfo_height()*4)

        # Create a canvas widget to make it scrollable
        canvas = Canvas(self.scrollable_frame, width=130, height=170)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(self.scrollable_frame,
                              orient="vertical", command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        list_frame = Frame(canvas)
        list_frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=list_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)

        # List of options (buttons)
        options = ["BFS", "DFS", "UCS", "A*"]

        for option in options:
            button = Button(list_frame,
                            text=option,
                            command=lambda opt=option: self.select_alg_option(
                                opt, alg_button),
                            activebackground="darkgray",
                            activeforeground="yellow",
                            anchor="center",
                            bd=3,
                            bg="gray",
                            cursor="hand2",
                            disabledforeground="gray",
                            fg="black",
                            font=("Bell MT", 12, "underline"),
                            height=1,
                            width=10,
                            justify="center",
                            overrelief="raised",
                            wraplength=200)
            button.pack(side=TOP)

    def select_alg_option(self, option, alg_button):
        # Update the main button text with the selected option
        alg_button.config(text=option)

        if option == "BFS":
            self.solution = self.list_solutions[0]
        elif option == "DFS":
            self.solution = self.list_solutions[1]
        elif option == "UCS":
            self.solution = self.list_solutions[2]
        else:
            self.solution = self.list_solutions[3]

        # Hide the options frame after selection
        if self.scrollable_frame:
            self.scrollable_frame.destroy()

    def show_input_options(self, input_button):
        # Remove existing scrollable frame if present
        if self.scrollable_frame:
            self.scrollable_frame.destroy()

        # Create a new frame for the list of buttons
        self.scrollable_frame = Frame()
        self.scrollable_frame.place(
            x=input_button.winfo_x(), y=input_button.winfo_y()-input_button.winfo_height()*4)

        # Create a canvas widget to make it scrollable
        canvas = Canvas(self.scrollable_frame, width=130, height=170)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(self.scrollable_frame,
                              orient="vertical", command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        list_frame = Frame(canvas)
        list_frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=list_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)

        # List of options (buttons)
        options = count_file_input()

        for option in options:
            button = Button(list_frame,
                            text=option,
                            command=lambda opt=option: self.select_input_option(
                                opt, input_button),
                            activebackground="darkgray",
                            activeforeground="yellow",
                            anchor="center",
                            bd=3,
                            bg="gray",
                            cursor="hand2",
                            disabledforeground="gray",
                            fg="black",
                            font=("Bell MT", 12, "underline"),
                            height=1,
                            width=10,
                            justify="center",
                            overrelief="raised",
                            wraplength=200)
            button.pack(side=TOP)

    def select_input_option(self, option, input_button):
        # Update the main button text with the selected option
        input_button.config(text=option)

        self.input = option
        self.display()

        # Hide the options frame after selection
        if self.scrollable_frame:
            self.scrollable_frame.destroy()

    def move_ares(self, ares_id, ares_pos, direction, cost):
        # Current position of Ares
        x, y = ares_pos

        # Movement directions (dx, dy)
        if direction == 'u':
            ares_pos = (x - 1, y)
        elif direction == 'd':
            ares_pos = (x + 1, y)
        elif direction == 'l':
            ares_pos = (x, y - 1)
        elif direction == 'r':
            ares_pos = (x, y + 1)

        # Erase the old Ares
        self.canvas.delete(ares_id)

        # Draw the new Ares
        x1, y1 = ares_pos[1] * self.tile_size, ares_pos[0] * self.tile_size
        x2, y2 = x1 + self.tile_size, y1 + self.tile_size

        ares_id = self.canvas.create_rectangle(x1 + 5, y1 + 5, x2 - 5,
                                               y2 - 5, fill="green", outline="black")

        cost += 1

        return (ares_id, ares_pos, cost)

    def push_stone(self, ares_id, stones_id, weights_id, ares_pos, stones_pos, stone_weight, direction, cost):
        # Current position of Ares
        x, y = ares_pos

        # Movement directions (dx, dy)
        if direction == 'U':
            ares_pos = (x - 1, y)
            new_stone_pos = (x - 2, y)
        elif direction == 'D':
            ares_pos = (x + 1, y)
            new_stone_pos = (x + 2, y)
        elif direction == 'L':
            ares_pos = (x, y - 1)
            new_stone_pos = (x, y - 2)
        elif direction == 'R':
            ares_pos = (x, y + 1)
            new_stone_pos = (x, y + 2)

        # Find stone that has been pushed
        stone_index = stones_pos.index(ares_pos)
        # Erase it
        self.canvas.delete(stones_id[stone_index])
        self.canvas.delete(weights_id[stone_index])
        self.canvas.delete(ares_id)
        # Draw new one
        x1, y1 = ares_pos[1] * self.tile_size, ares_pos[0] * self.tile_size
        x2, y2 = x1 + self.tile_size, y1 + self.tile_size
        ares_id = self.canvas.create_rectangle(x1 + 5, y1 + 5, x2 - 5,
                                               y2 - 5, fill="green", outline="black")

        x1, y1 = new_stone_pos[1] * \
            self.tile_size, new_stone_pos[0] * self.tile_size
        x2, y2 = x1 + self.tile_size, y1 + self.tile_size
        stone_id = self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5,
                                           y2 - 5, fill="dimgray", outline="black")
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        weight_id = self.canvas.create_text(center_x, center_y, text=str(
            self.maze.weights[stone_index]), fill="yellow", font="Aptos 10")
        # Update
        stones_pos[stone_index] = new_stone_pos
        stones_id[stone_index] = stone_id
        weights_id[stone_index] = weight_id

        cost += (1 + stone_weight[stone_index])

        return (ares_id, stones_id, ares_pos, stones_pos, cost)

    def animate_solution(self, start_button, input_button):
        """ Animate the solution step-by-step """
        if self.scrollable_frame:
            self.scrollable_frame.destroy()
        # Disable start button while animating
        start_button.config(state="disabled")
        input_button.config(state="disabled")

        ares_id = int(self.maze.ares_id)
        ares_pos = tuple(self.maze.Ares_position)
        stones_id = list(self.maze.stones_id)
        stones_pos = list(self.maze.stones_positions)
        weights_id = list(self.maze.weights_id)

        # Check if solution is found or not
        sol = str(self.solution)
        if sol == "Not Found" or sol == "":
            messagebox.showinfo("Error", "No Solution Found")
            start_button.config(state="normal")
            input_button.config(state="normal")
            return

        # Animation speed
        v = min(500, int((12 / len(sol)) * 1000))

        def make_move(step, ares_id, ares_pos, stones_id, stones_pos, cost):
            if step < len(sol):
                action = sol[step]
                if action.islower():
                    # Move without pushing a stone
                    ares_id, ares_pos, cost = self.move_ares(ares_id,
                                                             ares_pos, action, cost)
                else:
                    ares_id, stones_id, ares_pos, stones_pos, cost = self.push_stone(ares_id, stones_id, weights_id, ares_pos, stones_pos,
                                                                                     self.maze.weights, action, cost)  # Move and push a stone
                # Update counter
                self.counter[0].config(text=str(step + 1))
                self.counter[1].config(text=str(cost))
                self.animation_id = self.canvas.after(v, make_move, step + 1, ares_id,
                                                      ares_pos, stones_id, stones_pos, cost)
            else:
                messagebox.showinfo("Notification", "Animation Finished")
                start_button.config(state="normal")
                input_button.config(state="normal")
                self.maze.display_maze(self.canvas, self.tile_size)
                self.animation_id = None
                self.counter[0].config(text="0")
                self.counter[1].config(text="0")

        make_move(0, ares_id, ares_pos, stones_id, stones_pos, 0)

    def stop_animation(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.animation_id is not None:
            # Cancel any scheduled animation
            self.root.after_cancel(self.animation_id)
            self.animation_id = None

        self.switch_to_view1()


def read_solution_file(input):
    filename = input.replace("input", "solution")
    filename = "Solution/" + filename + ".txt"
    solution = []
    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip('\n\r')
            if not line:
                break
            solution.append(line)
    file.close()
    return solution


def count_file_input():
    files = glob.glob("input/input-*.txt")
    list_filenames = [os.path.splitext(os.path.basename(file))[
        0] for file in files]

    return list_filenames
