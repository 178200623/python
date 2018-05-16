import tkinter as tk

#创建窗口对象的背景色
app = tk.Tk()   
app.title("Ilove you ")

#创建个小部件
theLabel = tk.Label(app,    text="我的窗口！")
#将小部件放置到主窗口中
theLabel.pack() 

#进去消息循环
app.mainloop()

