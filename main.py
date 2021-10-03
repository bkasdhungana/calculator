from tkinter import *
from tkmacosx import Button
import tkinter.messagebox

root = Tk()
root.title("Simple Calculator")
root.configure(background="blue")
root.resizable(width=False, height=False)
root.geometry('500x700')


# functions

def button_click(number):
    current_num = user_display.get()
    user_display.delete(0, END)
    user_display.insert(0, str(current_num) + str(number))


def clear_button():
    user_display.delete(0, END)


def clear():
    user_display.delete(0, END)


def add():
    first_number = user_display.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    user_display.delete(0, END)


def subtract():
    first_number = user_display.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(first_number)
    user_display.delete(0, END)


def multiply():
    first_number = user_display.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    user_display.delete(0, END)


def division():
    first_number = user_display.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    user_display.delete(0, END)


def square_root():
    first_number = user_display.get()
    global f_num
    f_num = float(first_number)
    user_display.delete(0, END)
    user_display.insert(0, f_num ** 0.5)


def sign_change():
    first_number = user_display.get()
    global f_num
    f_num = float(first_number)
    user_display.delete(0, END)
    user_display.insert(0, f_num * (-1))


def equal():
    second_number = user_display.get()
    user_display.delete(0, END)
    if math == "addition":
        user_display.insert(0, f_num + float(second_number))

    if math == "subtract":
        user_display.insert(0, f_num - float(second_number))

    if math == "multiplication":
        user_display.insert(0, f_num * float(second_number))

    if math == "division":
        user_display.insert(0, f_num / float(second_number))


def close():
    tkinter.messagebox.showinfo("Command", "Are you sure?")
    root.destroy()


# top_frame


tops = Frame(root, bg="blue", pady=2, width=500, height=100, relief=RIDGE)
tops.grid(row=0, column=0)

tops = Frame(root, bg="blue", pady=2, width=500, height=100, relief=RIDGE)
tops.grid(row=0, column=0)

btnquit = Button(tops, text='Quit', bg='white', fg='red', height=68, width=80, command=close)
btnquit.grid(row=0, column=1)

lblTitle = Label(tops, font=('arial', 20, 'bold'), text="Calculator", width=28, bd=21, bg="white", fg="blue")
lblTitle.grid(row=0, column=0)

upperFrame = Frame(root, bg='White', bd=10, width=500, height=600, relief=RIDGE)
upperFrame.grid(row=1, column=0)

user_display = Entry(upperFrame, font=('arial', 20, 'bold'), bg="white", width=39,
                     justify=RIGHT)
user_display.grid(row=1, column=1)


calframe = Frame(root, bg='White', bd=10, width=500, height=600, relief=RIDGE)
calframe.grid(row=2, column=0)

buttonCE = Button(calframe, text='CE', bg='white', fg='black', borderless=1, height=100, width=110,
                  command=clear_button).grid(row=1, column=0)

buttonC = Button(calframe, text='C', bg='white', fg='#00203F', borderless=1, height=100, width=110, command=clear)
buttonC.grid(row=1, column=1)

buttonroot = Button(calframe, text='√ ', bg='white', fg='black', borderless=1, height=100, width=110, command=square_root)
buttonroot.grid(row=1, column=2)

buttonminus = Button(calframe, text='-', bg='white', fg='black', borderless=1, height=100, width=110, command=subtract)
buttonminus.grid(row=1, column=3)

button1 = Button(calframe, text="1", bg='white', fg='black', borderless=1, height=100, width=110, command=lambda: button_click(1))
button1.grid(row=4, column=0)

button2 = Button(calframe, text='2', bg='white', fg='#00203F', borderless=1, height=100,width=110, command=lambda: button_click(2))
button2.grid(row=4, column=1)

button3 = Button(calframe, text='3', bg='white', fg='black', borderless=1, height=100,width=110, command=lambda: button_click(3))
button3.grid(row=4, column=2)

buttonmul = Button(calframe, text='*', bg='white', fg='#00203F', borderless=1, height=100, width=110, command=multiply)
buttonmul.grid(row=2, column=3)

button4 = Button(calframe, text='4', bg='white', fg='black', borderless=1, height=100, width=110, command=lambda: button_click(4))
button4.grid(row=3, column=0)

button5 = Button(calframe, text='5', bg='white', fg='#00203F', borderless=1, height=100,width=110, command=lambda: button_click(5))
button5.grid(row=3, column=1)

button6 = Button(calframe, text='6', bg='white', fg='black', borderless=1, height=100,width=110, command=lambda: button_click(6))
button6.grid(row=3, column=2)

buttondiv = Button(calframe, text='/', bg='white', fg='black', borderless=1, height=100,width=110, command=division)
buttondiv.grid(row=3, column=3)

button7 = Button(calframe, text='7', bg='white', fg='black', borderless=1, height=100, width=110, command=lambda: button_click(7))
button7.grid(row=2, column=0)

button8 = Button(calframe, text='8', bg='white', fg='#00203F', borderless=1, height=100,width=110,
                 command=lambda: button_click(8))
button8.grid(row=2, column=1)

button9 = Button(calframe, text='9', bg='white', fg='#00203F', borderless=1, height=100,width=110, command=lambda: button_click(9))
button9.grid(row=2, column=2)

buttonplus = Button(calframe, text='+', bg='white', fg='black', borderless=1, height=100,width=110, command=add)
buttonplus.grid(row=4, column=3)

buttonz = Button(calframe, text='0', bg='white', fg='black', borderless=1, height=100, width=110, command=lambda: button_click(0))
buttonz.grid(row=5, column=0)

buttondot = Button(calframe, text='.', bg='white', fg='#00203F', borderless=1, height=100,width=110,
                   command=lambda: button_click('.'))
buttondot.grid(row=5, column=1)

buttonS = Button(calframe, text='±', bg='white', fg='black', borderless=1, height=100,width=110, command=sign_change)
buttonS.grid(row=5, column=2)

buttoneql = Button(calframe, text='=', bg='white', fg='black', borderless=1, height=100,width=110, command=equal)
buttoneql.grid(row=5, column=3)







root.mainloop()
