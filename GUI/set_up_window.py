def center_window(window, width, height):
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position x, y for the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set window size and position
    window.geometry(f'{width}x{height}+{x}+{y}')


def setup_window(root, w, h, color):
    window_width = w
    window_height = h

    # Center the window
    center_window(root, window_width, window_height)

    root.title("Ares's Adventure")  # Change window title
    root.iconbitmap('image/logo.ico')  # Change window icon
    root.configure(bg=color)  # Set background color to gray
    root.resizable(False, False)  # Disable window resize
