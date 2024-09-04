# Tkinter standard library
import tkinter as tk

from constants import MIN_APP_WIDTH, MIN_APP_HEIGHT, BLACK, LIGHT_WHITEBOARD_COLOR

# Creating the application window
def create_app():
  root = tk.Tk()
  root.title("Whiteboard")

  # Initialize window
  root.geometry("800x600")

  # Allow user to resize the window
  root.resizable(True, True)

  # Stop user from making window smaller than this size
  root.minsize(MIN_APP_WIDTH, MIN_APP_HEIGHT)

  # Create canvas
  canvas = tk.Canvas(root, bg=LIGHT_WHITEBOARD_COLOR)
  canvas.pack(expand=True, fill=tk.BOTH)

  toolbar(root)

  root.mainloop()

# create toolbar
def toolbar(root): 
  # Create toolbar container
  toolbar_frame = tk.Frame(root)
  toolbar_frame.pack(side="bottom", fill="x")

  #color_button = tk.Button(toolbar_frame, text="Change Color")
  #color_button.pack(side="left", padx=5, pady=5)

  #clear_button = tk.Button(controls_frame, text="Clear Canvas")
  #clear_button.pack(side="left", padx=5, pady=5)