from tkinter import *
def cb():
    print("MATHEMATICS IS",var1.get())
    print("CALCULUS",var2.get())
    print("QUANTUM COMPUTING",var3.get())
    
win =Tk()
f = Frame(relief=RAISED , borderwidth=5) 
var1 =IntVar()
var2 =IntVar() 
var3 =IntVar()
c1 = Checkbutton( 
f, text="MATHEMATICS", 
variable=var1,
command= (lambda:cb())) 
c1.pack(side=TOP)
c2 = Checkbutton( 
f, text="CALCULUS", 
variable=var2,
command= (lambda:cb())) 
c2.pack(side=TOP)
c3 = Checkbutton(
f, text="QUANTUM COMPUTING",
variable=var3,
command= (lambda: cb()))
c3.pack(side=TOP)
f.pack()
mainloop()
