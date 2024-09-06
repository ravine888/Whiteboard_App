import tkinter as tk

# class function for easier inheiritance
class Whiteboard:
    def __init__(self, master):
        # Allow user to resize the window
        master.resizable(True, True)

        # Setup the minimum window size
        master.minsize(100, 100)

        self.master = master

        # Create canvas thats the size of the window
        self.canvas = tk.Canvas(self.master, bg="black")
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Setup variable
        self.drawing = False
        self.prev_x = 0
        self.prev_y = 0
        self.color = "white"
        self.line_width = 5

        # call class function
        self.mouse_event()

    # define actions for mouse events
    def mouse_event(self):
        self.master.bind("<Button-1>", self.start_line)
        self.master.bind("<B1-Motion>", self.draw_line)
        self.master.bind("<ButtonRelease-1>", self.end_line)

    # intialize a line when mouse is pressed
    def start_line(self, event):
        self.drawing = True
        self.prev_x = event.x
        self.prev_y = event.y
        # if mouse is clicked, leave a dot on the canvas
        self.canvas.create_line(event.x, 
                                event.y, 
                                event.x, 
                                event.y, 
                                fill=self.color, 
                                width=self.line_width, 
                                capstyle=tk.ROUND, 
                                smooth=True)
    
    # draw a line when mouse is moved
    def draw_line(self, event):
        if self.drawing: 
            self.canvas.create_line(self.prev_x, 
                self.prev_y, 
                event.x, 
                event.y, 
                fill=self.color, 
                width=self.line_width, 
                capstyle=tk.ROUND, 
                smooth=True)

            self.prev_x, self.prev_y = event.x, event.y

    # End the line being drawn
    def end_line(self, event):
        self.drawing = False


def main():
    # Initialize the Tkinter application
    root = tk.Tk()
    root.title("Whiteboard")
    root.geometry("800x600")

    # Create class instance
    Whiteboard(root)

    # Tkinter event loop to make GUI responsive and interactive
    root.mainloop()


if __name__ == "__main__":
    main()