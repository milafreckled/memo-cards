from tkinter import *
from tkinter import messagebox
Window = Tk()
Window.title("Home task")
Window.geometry('300x200')
Window["bg"]='#ededed'

btn=Button(text='Друга кнопка',
           background='#006400',
           foreground='#FFBC00',
           padx='20',
           pady='8',
           font='18',
           width='10',
           height='4',
           )
def change(event):
    Window.title("Python")
    Window.geometry('300x400')
    Window["bg"]='green'
    messagebox.showinfo('Python')
    
btn.pack()
Window.bind('<Double Button-1>', change)
Window.mainloop()
           