from tkinter import *

wd = Tk()

wd.title("Calculator")

e = Entry(width=30, border=10, font="Arial 18") #Create a text input 


btn_7 = Button(text="7", width="10", height="3", background="pink", font="Helvetica")
btn_8 = Button(text="8", width="10", height="3", background="pink", font="Helvetica")
btn_9 = Button(text="9", width="10", height="3", background="pink", font="Helvetica")
btn_divide = Button(text="/", width="10", height="3", background="pink", font="Helvetica")

e.grid(row = 0, column=0, columnspan=4, pady=10) #put the text input on window
btn_7.grid(row=1, column=0);
btn_8.grid(row=1, column=1);
btn_9.grid(row=1, column=2);
btn_divide.grid(row=1, column=3);

wd.mainloop()