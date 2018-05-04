import tkinter as tk

root = tk.Tk()

person = ["one","two","three"]


v=[]
lab = tk.Label(root,text="null")
lab.pack()

def print_select():
    for i in range(len(v)):
        print(v[i].get())
        if v[i].get()==1:
            lab.config(text=person[i])

for gril in person:
    v.append(tk.IntVar())
    checkbt = tk.Checkbutton(root,text=gril,variable=v[-1],command=print_select)
    checkbt.pack()

tk.mainloop()
