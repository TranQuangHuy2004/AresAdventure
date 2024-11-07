from tkinter import *
from GUI.set_up_window import setup_window


class home:
    def __init__(self, root, switch_to_view2, switch_to_view3):
        self.root = root
        self.switch_to_view2 = switch_to_view2
        self.switch_to_view3 = switch_to_view3
        self.canvas = None
        self.tile_size = 30
        self.width = 510
        self.height = 300

    def display(self):
        # Clear the window and show the content of home
        for widget in self.root.winfo_children():
            widget.destroy()
        setup_window(self.root, self.width, self.height, "white")

        self.canvas = Canvas(self.root, width=self.width,
                             height=self.height, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.decorate_bg()
        self.add_button()

    def decorate_bg(self):
        row = int(self.height/self.tile_size)
        col = int(self.width/self.tile_size)
        for i in range(row):
            for j in range(col):
                if (i % 2 == 0):
                    x1 = 2 * j * self.tile_size
                    x2 = x1 + 2 * self.tile_size
                else:
                    x1 = 2 * j * self.tile_size - self.tile_size
                    x2 = x1 + 2 * self.tile_size

                y1 = i * self.tile_size
                y2 = y1 + self.tile_size

                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="maroon", outline="black", width=2)

        self.canvas.create_text(
            250, 55, text="Ares's", fill="gray", font=("Algerian", 30, "bold"))
        self.canvas.create_text(
            255, 50, text="Ares's", fill="yellow", font=("Algerian", 30, "bold"))
        self.canvas.create_text(
            250, 110, text="Adventure", fill="gray", font=("Algerian", 30, "bold"))
        self.canvas.create_text(
            255, 105, text="Adventure", fill="yellow", font=("Algerian", 30, "bold"))

    def add_button(self):
        visual_button = Button(self.root,
                               text="Visualization",
                               command=self.switch_to_view3,
                               activebackground="darkgray",
                               activeforeground="yellow",
                               anchor="center",
                               bd=4,
                               bg="gray",
                               cursor="hand2",
                               disabledforeground="gray",
                               fg="black",
                               font=("Bell MT", 12, "bold"),
                               height=1,
                               width=12,
                               justify="center",
                               overrelief="raised",
                               wraplength=200)

        visual_button.place(x=180, y=160)

        run_alg_button = Button(self.root,
                                text="Run algorithm",
                                command=self.switch_to_view2,
                                activebackground="darkgray",
                                activeforeground="yellow",
                                anchor="center",
                                bd=4,
                                bg="gray",
                                cursor="hand2",
                                disabledforeground="gray",
                                fg="black",
                                font=("Bell MT", 12, "bold"),
                                height=1,
                                width=12,
                                justify="center",
                                overrelief="raised",
                                wraplength=200)

        run_alg_button.place(x=180, y=220)
