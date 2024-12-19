import tkinter as tk

# create a login interface
# store user in database
class myGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.title("Login")

        self.label = tk.Label(self.root, text="Name ")
        self.label.pack(padx=5,pady=5)
        self.label.place(x=1,y=1)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10)
        


        self.root.mainloop()

myGUI()