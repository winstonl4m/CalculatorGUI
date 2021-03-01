from tkinter import *
from math import sqrt
from decimal import Decimal


base = Tk()
base.title('Calculator')
base.geometry("500x700")

output = Entry(base, width = 70, borderwidth=10)
output.grid(row = 0, column = 0, columnspan = 4, padx =10, pady = 10)

arith_stack =[]
number_stack =[]


# functions
def button_click(number):
    current = output.get()
    output.delete(0,END)
    num = str(current) + str(number)
    #number_stack.append(num)
    #print(number_stack)
    output.insert(0,num)

def button_add():
    first_num = output.get()
    global f_num
    global ma
    ma = "add"
    f_num = Decimal(first_num)
    arith_stack.append(ma)
    number_stack.append(f_num)
    print(number_stack)
    print(arith_stack)
    output.delete(0,END)



def button_subtract():
    first_num = output.get()
    global f_num
    global ma
    ma = "sub"
    f_num = Decimal(first_num)
    number_stack.append(f_num)
    print(number_stack)
    arith_stack.append(ma)
    print(arith_stack)
    output.delete(0, END)

def button_multiply():
    first_num = output.get()
    global f_num
    global ma
    ma = "multiply"
    f_num = Decimal(first_num)
    number_stack.append(f_num)
    print(number_stack)
    arith_stack.append(ma)
    print(arith_stack)
    output.delete(0, END)

def button_divide():
    first_num = output.get()
    global f_num
    global ma
    ma = "div"
    f_num = Decimal(first_num)
    number_stack.append(f_num)
    print(number_stack)
    arith_stack.append(ma)
    print(arith_stack)
    output.delete(0, END)

def button_clear():
    arith_stack.clear()
    number_stack.clear()
    output.delete(0,END)

def button_equals():
    second_num = output.get()
    output.delete(0,END)
    number_stack.append(second_num)
    arith_stack_str = [str(a) for a in arith_stack]
    print(arith_stack_str)
    number_stack_int = [Decimal(a) for a in number_stack]
    print(number_stack_int)

    
    #while number_stack_int:
    while arith_stack_str and number_stack_int:
        for y in number_stack_int:
            for x in arith_stack_str:
                last_num = number_stack_int.pop()
                x = arith_stack_str.pop()
                y = number_stack_int.pop()
                if x == "add":
                    number_stack_int.clear()
                    number_stack_int.append(y+ last_num)
                    output.insert(0,y+ last_num)
                if x == "sub":
                    number_stack_int.clear()
                    number_stack_int.append(y- last_num)
                    output.insert(0, y - last_num)
                if x == "multiply":
                    number_stack_int.clear()
                    number_stack_int.append(y * last_num)
                    output.insert(0, y * last_num)
                if x == "sqr":
                    output.insert(0,y)
                if x == "sqrt":
                    output.insert(0,y)
                if x == "div":
                    try:
                        number_stack_int.clear()
                        number_stack_int.append(last_num/y)
                        output.insert(0,y / last_num)
                    except ZeroDivisionError:
                        output.insert(0, "ERROR: cannot divide by 0")

def button_posneg():
    first_num = output.get()
    global f_num2
    f_num2 = -1* Decimal(first_num)
    output.delete(0, END)
    #number_stack.append(f_num2)
    output.insert(0,f_num2)


def button_dec():
    current = output.get()
    output.delete(0,END)
    #dec_num = str(current)+ "."
    #number_stack.append(dec_num)
    #print(number_stack)
    output.insert(0,str(current)+ ".")


def button_sqr():
    first_num = output.get()
    global f_num
    global ma
    ma = "sqr"
    f_num = Decimal(first_num)*Decimal(first_num)
    print(f_num)
    #number_stack.append(f_num)
    print(number_stack)
    output.delete(0, END)
    #number_stack.append(f_num)
    output.insert(0, f_num)

def button_sqrt():
    first_num = output.get()
    global f_num
    global ma
    ma = "sqrt"
    try:
        f_num = sqrt(Decimal(first_num))
        print(f_num)
        #number_stack.append(f_num)
        print(number_stack)
        output.delete(0, END)
        #number_stack.append(f_num)
        output.insert(0, f_num)
    except ValueError:
        output.delete(0, END)
        output.insert(0, "ERROR: Cannot take the square root of a negative number")

# Creating the buttons and positioning them
button_1 = Button(base, text="1", padx = 40, pady =20, command = lambda :button_click(1))
button_2 = Button(base, text="2", padx = 40, pady =20, command = lambda :button_click(2))
button_3 = Button(base, text="3", padx = 40, pady =20, command = lambda :button_click(3))
button_4 = Button(base, text="4", padx = 40, pady =20, command = lambda :button_click(4))
button_5 = Button(base, text="5", padx = 40, pady =20, command = lambda :button_click(5))
button_6 = Button(base, text="6", padx = 40, pady =20, command = lambda :button_click(6))
button_7 = Button(base, text="7", padx = 40, pady =20, command = lambda :button_click(7))
button_8 = Button(base, text="8", padx = 40, pady =20, command = lambda :button_click(8))
button_9 = Button(base, text="9", padx = 40, pady =20, command = lambda :button_click(9))
button_0 = Button(base, text="0", padx = 40, pady =20, command = lambda :button_click(0))


button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=1)

button_add = Button(base, text ="+", padx =40, pady=20, command = button_add)
button_subtract = Button(base, text ="-", padx =40, pady=20, command = button_subtract)
button_multiply = Button(base, text ="*", padx =40, pady=20, command = button_multiply)
button_divide = Button(base, text ="/", padx =40, pady=20, command = button_divide)
button_equals = Button(base, text ="=", padx =40, pady=20, command = button_equals)
button_clear = Button(base, text ="C", padx =40, pady=20, command = button_clear)

button_clear.grid(row=1, column=0)
button_add.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)
button_equals.grid(row=5,column=3)

button_posneg = Button(base, text ="+/-", padx= 40, pady =20, command = button_posneg)
button_posneg.grid(row=5, column=0)

button_dec = Button(base, text =".", padx= 40, pady =20, command = button_dec)
button_dec.grid(row=5, column=2)

button_sqr = Button(base, text ="x^2", padx= 40, pady =20, command = button_sqr)
button_sqr.grid(row=1, column=2)

button_sqrt = Button(base, text ="sqrt(x)", padx= 40, pady =20, command = button_sqrt)
button_sqrt.grid(row=1, column=1)



base.mainloop()