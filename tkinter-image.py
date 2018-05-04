from  tkinter  import *

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

text_label = Label(frame1,textvariable="this is null", justify=LEFT)
text_label.pack(side=LEFT)

photo = PhotoImage(file="py.gif")
imglabel = Label(frame1,  image=photo)
imglabel.pack(side=RIGHT)

hebutton = Button(frame2,   text="button")
hebutton.pack()

frame1.pack()
frame2.pack()

root.mainloop()
