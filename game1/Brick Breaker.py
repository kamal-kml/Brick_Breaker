from tkinter import *

window= Tk()
window.geometry("1000x600")
window.resizable(0,0)
window.title("BRICK BREAKER")

#Canvas

canvas = Canvas(bg='black',width=1000,height=600)
canvas.pack()


window.mainloop()