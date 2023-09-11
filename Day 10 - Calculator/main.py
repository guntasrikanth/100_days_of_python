import os
from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations ={
    '+': add,
    '-':subtract,
    '*':multiply,
    '/':divide,
    
}
os.system('cls')

def calculator():
    print(logo)
    info ='y'
    n1 = int(input("Enter the first number: "))
    while info =='y':
        for key in operations:
            print(key)
        symbol = input("Which operation do you want to perform: ")
        n2 = int(input("What's the next number: "))
        cal_function = operations[symbol]
        answer = cal_function(n1,n2)
        print(f"{n1} {symbol} {n2} : {answer}")
        info =input(f"type \'y\' to continue calculating with {answer}, or type \'n\' to start a new calculator: ")
        if info == 'y':
            n1 = answer
        else:
            os.system('cls')
            calculator()

calculator()