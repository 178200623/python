from tkinter import *

root = Tk()

Label(root,text="用户名:").grid(row=0,column=0)
Label(root,text="密   码:").grid(row=1,column=0)

v1 = StringVar()
v2 = StringVar()
txt = StringVar()
plab = Label(root,textvariable=txt).grid(row=4,column=0)
e1 = Entry(root,textvariable=v1)
e2 = Entry(root,textvariable=v2,show="*")
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    re = str(e1.get()) + str(e2.get())
    print(re)
    txt.set(str(re))
    print("用户名：" +e1.get())
    print("密码："+e2.get())
def delall():
    e1.delete(0,END)
    e2.delete(0,END)

Button(root,text="打印",width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root,text="清空",width=10,command=delall).grid(row=3,column=1,sticky=E,padx=10,pady=5)

root.mainloop()
