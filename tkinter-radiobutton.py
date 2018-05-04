import tkinter as tk

root = tk.Tk()


group = tk.LabelFrame(root, text="编程语言",    padx=5,  pady=5)
group.pack()
LANGS =[("python",  1),("C++",  2),("JAVA", 3)]

v=tk.IntVar()
v.set(1)
for name,num in LANGS:
    print(name,num)
    radiobt = tk.Radiobutton(group,  text=name,  value=num,  variable=v)
                             #,indicatoron=False)
    radiobt.pack(anchor="w")

tk.mainloop()
