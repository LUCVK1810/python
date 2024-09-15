from tkinter import *
def change():
    print('Station = ' , var.get())
    
root = Tk()
stations = 'WAAL' , 'WSKG' , 'WSQX' , 'WNBF'
f = Frame(relief=RAISED , borderwidth=5) 
var = StringVar()

for station in stations:
    radio = Radiobutton(f, text=station, variable=var ,value=station)
    radio.pack(side=TOP)
    
f.pack(pady=10)
Button(root,text='New' , command=(lambda: change())).pack(pady=10) 
var.set('WAAL') #initalize the set of radio buttons
mainloop()
