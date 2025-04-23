import sympy as sp
import math
from tkinter import *
from tkinter import ttk
root=Tk()


root.title("Calcluator")

root.geometry("800x600")
def calc_choice(event):
    if Calc_selected.get() == 'basic':
        Calc_choice_lbl.grid_remove()
        calc_drop.grid_remove()
        def equ_solve():
            equ_solver=eval(basic_enter.get())
            solvedlbl=Label(root, text="The answer is: " + str(equ_solver))
            solvedlbl.grid(column=0,row=5)
            if basic_enter.get() =="/" and basic_enter.get()=="0":

                solvedlbl=Label(root, text="You cannot devide by 0")
                solvedlbl.grid(column=0,row=5)
            if basic_enter.get() != "0" or basic_enter.get() != "1"or basic_enter.get() != "2"or basic_enter.get() != "3"or basic_enter.get() != "4"or basic_enter.get() != "5"or basic_enter.get() != "6"or basic_enter.get() != "7"or basic_enter.get() != "8"or basic_enter.get() != "9"or basic_enter.get() != "+"or basic_enter.get() != "-"or basic_enter.get() != "*"or basic_enter.get() != "/":
                solvedlbl=Label(root, text="please enter a valid charecter")
                solvedlbl.grid(column=0,row=5)
        basiclbl=Label(root, text="welcome to the basic calcluator, please input your equation into the text box with +=add,-=subtract, *=multply, /=divide: ")
        basiclbl.grid(column=0,row=2)
        basic_enter=Entry(root, width=50)
        basic_enter.grid(column=0,row=3)
        basicbtn=Button(root, text="solve", command=equ_solve)
        basicbtn.grid(column=0,row=4)



    if Calc_selected.get() == 'function':
        Calc_choice_lbl.grid_remove()
        calc_drop.grid_remove()
        functionlbl=Label(root, text="welcome to the function calcluator, which functions do you want to input: ")
        functionlbl.grid(column=0,row=2)
        function_select=StringVar()
        function_drop=ttk.Combobox(root, values=['linear', 'quadratic'], textvariable=function_select)
        function_drop.grid(column=0,row=3)
        if function_select.get() == 'linear':
            def linear_func():
                x = sp.symbols('x')
                a = float(a_enter.get())
                b = float(b_enter.get())
                f = a*x + b
                solvedlbl=Label(root, text="The answer is: " + str(f))
                solvedlbl.grid(column=0,row=9)
            functionlbl.grid_remove()
            function_drop.grid_remove()
            albl=Label(root,text="please enter the value of a(coffeceant of x): ")
            albl.grid(column=0,row=4)
            a_enter=Entry(root, width=50)
            a_enter.grid(column=0,row=5)
            blbl=Label(root, text="please enter the value for b(the thing that gets added to ax):")
            blbl.grid(column=0,row=6)
            b_enter=Entry(root, width=50)
            b_enter.grid(column=0,row=7)
            linearbtn=Button(root, text="solve", command=linear_func)
            linearbtn.grid(column=0,row=8)

        if function_select.get() == 'quadratic':
            def quad_func():
                x = sp.symbols('x')
                a = float(a_enter.get())
                b = float(b_enter.get())
                c = float(c_enter.get())
                f = a*x**2 + b*x + c
                solvedlbl=Label(root, text="The answer is: " + str(f))
                solvedlbl.grid(column=0,row=10)
            functionlbl.grid_remove()
            function_drop.grid_remove()
            albl=Label(root,text="please enter the value of a(coffeceant of x^2): ")
            albl.grid(column=0,row=4)
            a_enter=Entry(root, width=50)
            a_enter.grid(column=0,row=5)
            blbl=Label(root, text="please enter the value for b(coffeceant of x):")
            blbl.grid(column=0,row=6)
            b_enter=Entry(root, width=50)
            b_enter.grid(column=0,row=7)
            clbl=Label(root, text="please enter the value for c(the thing that gets added to ax^2+bx):")
            c_enter=Entry(root, width=50)
            c_enter.grid(column=0,row=8)
            quadbtn=Button(root, text="solve", command=quad_func)
            quadbtn.grid(column=0,row=9)




    if Calc_selected.get() == 'calclus':
        calclbl=Label(root, text="welcome to the calclus calcluator, please select a calclus function: ")
        calclbl.grid(column=0,row=3)
        calclus_select=StringVar()
        calclus_drop=ttk.Combobox(root, values=['integral', 'derivative'], textvariable=calclus_select)
        if calclus_select.get() == 'integral':
            def integral_func():
                x = sp.symbols('x')
                f = inter_enter.get()
                integral = sp.integrate(f, x)
                solvedlbl=Label(root, text="The answer is: " + str(integral))
                solvedlbl.grid(column=0,row=7)
            calclbl.grid_remove()
            calclus_drop.grid_remove()
            integrallbl=Label(root,text="please enter the function you want to integrate(for exponents, input x**n): ")
            integrallbl.grid(column=0,row=4)
            inter_enter=Entry(root, width=50)
            inter_enter.grid(column=0,row=5)
            integralbtn=Button(root, text="solve", command=integral_func)
            integralbtn.grid(column=0,row=6)    
        if calclus_select.get() == 'derivative':
            def derivative_func():
                x = sp.symbols('x')
                f = deriv_enter.get()
                derivative = sp.diff(f, x)
                solvedlbl=Label(root, text="The answer is: " + str(derivative))
                solvedlbl.grid(column=0,row=7)
            derivativelbl=Label(root,text="please enter the function you want to find the derivative of(for exponents, input x**n): ")
            derivativelbl.grid(column=0,row=4)
            deriv_enter=Entry(root, width=50)
            deriv_enter.grid(column=0,row=5)
            derivativebtn=Button(root, text="solve", command=derivative_func)
            derivativebtn.grid(column=0,row=6)


root.config(bg="black")
Calc_selected=StringVar()
Calc_choice_lbl=Label(root,text="Welcome to the calcluator, please choose a function: ")
Calc_choice_lbl.grid(column=0,row=0)
calc_choices=['basic', 'function', 'calclus']
calc_drop=ttk.Combobox(root, values=calc_choices, textvariable=Calc_selected)
calc_drop.bind("<<ComboboxSelected>>", calc_choice)
calc_drop.grid(column=0,row=1)


root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.rowconfigure(6,weight=1)
root.rowconfigure(7,weight=1)
root.rowconfigure(8,weight=1)
root.rowconfigure(9,weight=1)
root.rowconfigure(10,weight=1)
root.mainloop()