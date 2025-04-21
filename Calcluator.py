import sympy as sp
Calc_choice=input("Enter the calcluator you want (basic, finction, calclus): ")

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


