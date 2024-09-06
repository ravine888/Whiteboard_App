
import tkinter as tk

root = tk.Tk()
root.title("Custom Menubar")
root.geometry("1000x1000")

# Create a frame at the top of the window
top_frame = tk.Frame(root, bg="#20232A", height=50)
top_frame.pack(fill=tk.X)

# Add buttons to the frame
file_button = tk.Button(top_frame, text="File", bg="#20232A", fg="white")
file_button.pack(side=tk.LEFT, padx=10)

edit_button = tk.Button(top_frame, text="Edit", bg="#20232A", fg="white")
edit_button.pack(side=tk.LEFT, padx=10)

help_button = tk.Button(top_frame, text="Help", bg="#20232A", fg="white")
help_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()

'''
import tkinter as tk

root = tk.Tk()
root.title("TEST")
root.geometry("1000x1000")

def hello():
    print("hello!")


###cascade menu

menubar = tk.Menu(root)

t = tk.Menu(menubar, tearoff=0)
t.add_command(label="Hello!", command=hello)
t.add_command(label="Quit!", command=root.quit)

menubar.add_cascade(label="thing", menu=t)
root.config(menu=menubar)


#### popup menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Hello!", command=hello)
menu.add_command(label="Quit!", command=root.quit)

frame = tk.Frame(root, width=512, height=512)
frame.pack()

def popup(event): 
    menu.post(event.x_root, event.y_root)

frame.bind("<Button-3>", popup)

root.mainloop()
'''