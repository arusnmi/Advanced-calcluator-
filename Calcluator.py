import sympy as sp
import math
Calc_choice=input("Enter the calcluator you want (basic, function, calclus): ")

if Calc_choice == "basic":
    print(eval(input("Enter the calcluation: ")))


if Calc_choice=="calclus":
    print("Welcome to the calclus calculator, select the number for the function you want to input")
    print("1. Derivative")
    print("2. Integral")
    function_choice = input("Enter the function you want(converth the function varible to x): ")
    x = sp.symbols('x')
    if function_choice == "1":
        function = input("Enter the function you want to derivate: ")
        derivative = sp.diff(function, x)
        print(f"The derivative of {function} is {derivative}")
    elif function_choice == "2":
        function = input("Enter the function you want to integrate: ")
        integral = sp.integrate(function, x)
        print(f"The integral of {function} is {integral}")
    else:
        print("Invalid choice")


if Calc_choice=="function":
    print("Welcome to the function calculator, select the number for the function you want to input")
    print ("1.linear")
    print ("2.quadratic")
    function_choice = input("Enter the function you want(converth the function varible to x): ")
    x = sp.symbols('x')
    if function_choice=="1":
        a=float(input("enter the value of a(coffecant of x):" ))
        c_input= float(input("enter the value of c:" ))
        if a!=0:
            soloution= -c_input/a
            print("Soloution for x: ",soloution)
    elif function_choice=="2":
        a=float(input("enter the value of a(coffecant of x^2):" ))
        b=float(input("enter the value of b(coffecant of x):" ))
        c_input= float(input("enter the value of c:" ))
        d=b**2-4*a*c_input
        if a!=0:
            
            if d>0:
                soloution1=(-b+math.sqrt(d))/(2*a)
                soloution2=(-b-math.sqrt(d))/(2*a)
                print("Soloution1: ",soloution1)
                print("Soloution2: ",soloution2)
            elif d==0:
                soloution=-b/(2*a)
                print("Soloution: ",soloution)
            else:
                print("No real soloution")
        else :
            print("Invalid input")