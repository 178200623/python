import tkinter as tk

class APP:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT,    padx=10,pady=20)

        self.hi_there = tk.Button(frame,    text="button",  fg="blue",  bg="red",command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print("hello everyone!!!")


root = tk.Tk()
root.title("tkinter02")
app = APP(root)

root.mainloop()
