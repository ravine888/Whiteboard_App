import tkinter as tk

root = tk.Tk()
root.title("TEST")
root.geometry("800x800")

def callback():
    print("TESTING BUTTON")

test_b = tk.Button(root, 
                    text="OK",
                    padx=20, 
                    command=callback)
test_b.pack(padx=100)

root.mainloop()