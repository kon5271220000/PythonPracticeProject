from tkinter import *

wd = Tk()

wd.title("Calculator")

e = Entry(width=30, border=10, font="Arial 18") #Create a text input 


btn_7 = Button(text="7", width="10", height="3", background="pink", font="Helvetica")
btn_8 = Button(text="8", width="10", height="3", background="pink", font="Helvetica")
btn_9 = Button(text="9", width="10", height="3", background="pink", font="Helvetica")
btn_divide = Button(text="/", width="10", height="3", background="pink", font="Helvetica")

btn_4 = Button(text="4", width="10", height="3", background="pink", font="Helvetica")
btn_5 = Button(text="5", width="10", height="3", background="pink", font="Helvetica")
btn_6 = Button(text="6", width="10", height="3", background="pink", font="Helvetica")
btn_multi = Button(text="*", width="10", height="3", background="pink", font="Helvetica")

btn_1 = Button(text="1", width="10", height="3", background="pink", font="Helvetica")
btn_2 = Button(text="2", width="10", height="3", background="pink", font="Helvetica")
btn_3 = Button(text="3", width="10", height="3", background="pink", font="Helvetica")
btn_substract = Button(text="-", width="10", height="3", background="pink", font="Helvetica")

btn_clear = Button(text="clear", width="10", height="3", background="pink", font="Helvetica")
btn_0 = Button(text="0", width="10", height="3", background="pink", font="Helvetica")
btn_equal = Button(text="=", width="10", height="3", background="pink", font="Helvetica")
btn_add = Button(text="+", width=10, height="3", background="pink", font="Helvetica")

e.grid(row = 0, column=0, columnspan=4, pady=10) #put the text input on the window

#put button on the window
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_divide.grid(row=1, column=3)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_multi.grid(row=2, column=3)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_substract.grid(row=3, column=3)

btn_clear.grid(row=4, column=0)
btn_0.grid(row=4, column=1)
btn_equal.grid(row=4, column = 2)
btn_add.grid(row=4, column=3)

wd.mainloop()