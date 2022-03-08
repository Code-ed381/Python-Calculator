import tkinter
from tkinter import *
equation_output = ""

root = tkinter.Tk()

root.geometry('500x500')
root.resizable(False, False)

root.title('Calculator')

root.configure(bg='#36454F')

def keyPress(num):
    global equation_output
    equation_entry = output.get()
    if equation_entry == "":
        equation_output = equation_output + str(num)
    else:
        equation_output = equation_entry + str(num)

    output_list = list(equation_output)
    print(output_list)
    output.set(equation_output)


def Reset():
    global equation_output
    equation_output = ""
    output.set(equation_output)
    input_val.set(equation_output)

def Negative(num):
    global equation_output
    neg_sign = input_field.get()

    if "-" in neg_sign:
        equation_output = ""
        output.set(equation_output)
    else:
        equation_output = equation_output + str(num)
        output.set(equation_output)

def Clear():
    global equation_output
    equation_output = ""
    if output.get() != "":
        input_field.delete(len(input_field.get())-1)
    else:
        output.set(equation_output)

def Equal():
    global equation_output
    total = str(eval(equation_output))
    InputValue = input_field.get()
    input_val.set(InputValue)

    equation_output = ""
    output.set(total)
    



output = StringVar()
input_val = StringVar()

output_field = tkinter.Entry(root, font="Arial 20",justify=tkinter.RIGHT, textvariable=input_val)
output_field.place(x=90, y=10)
input_field =  tkinter.Entry(root, font="Arial 20", justify=tkinter.RIGHT,textvariable=output)
input_field.place(x=90, y=45)


#Buttons  
nine = tkinter.Button(root,text=9, font="Arial 20",bg='#F4BB44', width='3',command=lambda: keyPress(9) )
nine.place(x=125, y=150)
eight = tkinter.Button(root,text=8,font="Arial 20",bg='#F4BB44', width='3', command=lambda:keyPress(8) )
eight.place(x=185, y=150)
seven = tkinter.Button(root,text=7, font="Arial 20",bg='#F4BB44', width='3', command=lambda:keyPress(7) )
seven.place(x=245, y=150)
six = tkinter.Button(root,text=6,font="Arial 20",bg='#F4BB44', width='3', command=lambda:keyPress(6))
six.place(x=125, y=210)
five = tkinter.Button(root,text=5,font="Arial 20",bg='#F4BB44', width='3', command=lambda:keyPress(5) )
five.place(x=185, y=210)
four = tkinter.Button(root,text=4,font="Arial 20",bg='#F4BB44', width='3', command=lambda:keyPress(4))
four.place(x=245, y=210)
three = tkinter.Button(root,text=3,font="Arial 20",bg='#F4BB44', width='3', command=lambda:keyPress(3))
three.place(x=125, y=270)
two = tkinter.Button(root,text=2,font="Arial 20",bg='#F4BB44', width='3', command=lambda:keyPress(2))
two.place(x=185, y=270)
one = tkinter.Button(root,text=1,font="Arial 20",bg='#F4BB44',width='3', command=lambda:keyPress(1) )
one.place(x=245, y=270)
zero = tkinter.Button(root,text=0, font="Arial 20",bg='#F4BB44', width='3',command=lambda:keyPress(0) )
zero.place(x=185, y=330)
dot = tkinter.Button(root,text=".",bg='#93C572',fg='white', font="Arial 20", width='3',command=lambda:keyPress(".") )
dot.place(x=125, y=330)
negative = tkinter.Button(root,text="-/+",bg='#93C572',fg='white', font="Arial 20", width='3',command=lambda:Negative("-") )
negative.place(x=245, y=330)
modulo = tkinter.Button(root,text="%",bg='#93C572',fg='white', font="Arial 20", width='3',command=lambda:keyPress("%") )
modulo.place(x=245, y=90)
reset = tkinter.Button(root,text="CE", bg='#AB3131',fg='white', font="Arial 20", width='3',command=Clear )
reset.place(x=185, y=90)
clear = tkinter.Button(root,text="C", bg='#FF3160',fg='white', font="Arial 20", width='3',command=Reset )
clear.place(x=125, y=90)
add = tkinter.Button(root,text="+",bg='#93C572',fg='white', font="Arial 20", width='3',command=lambda:keyPress("+") )
add.place(x=305, y=150)
subtract = tkinter.Button(root,text="-",bg='#93C572',fg='white', font="Arial 20", width='3',command=lambda:keyPress("-") )
subtract.place(x=305, y=210)
divide = tkinter.Button(root,text="/",bg='#93C572',fg='white', font="Arial 20", width='3',command=lambda:keyPress("/") )
divide.place(x=305, y=90)
multiply = tkinter.Button(root,text="x",bg='#93C572',fg='white', font="Arial 20", width='3',command=lambda:keyPress("*") )
multiply.place(x=305, y=270)
equal = tkinter.Button(root,text="=",bg='#93C572',fg='white', font="Arial 20", width='3', command=Equal )
equal.place(x=305, y=330)

credit = tkinter.Label(root,text="Made by Edwin",bg='#36454F', fg='white', font=('chiller', 15, 'italic'))
credit.place(x=200,y=450)



root.mainloop()
