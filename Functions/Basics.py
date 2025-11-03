#A function is a block of reusable code / statements that written a specific task 
#It executes the code whenever the function is called
# 'def'  - keyword to define function 

# def Hello():
#     print("Hello")
# Hello() # calling a function 

# def makeTea():
#     print("Light on the gas")
#     print("put a pan on that ")
#     print("Pour water , milk and sugar in it")
#     print("Let it boil ")
#     print("Turn off the gas ")
#     print("Pour it into cup")

# makeTea()

#Parameters are the variables listed inside the paranthese in function definition

# def hello(name):#parameter
#     print("Hello",name)

# #Arguments are the actual values that are passed to a function when it is called

# hello("Vinu")#argument
# # hello()  #--TypeError: hello() missing 1 required positional argument: 'name'
# hello(1)

#q-- write a function to print square of a no.

def sqr(num):
    print(num*num)

# sqr(5)
#q- write a program to print square of all no.s from x to y

def allSqr(x,y):
    if(y>x):
        for i in range(x,y+1):
            print(i*i)
    else:
        print("y must be greater than x")

# allSqr(2,5)
    
#q - write a program to implement pythagorus theorem using fucntion
import math
def pythagorus(b,p):
    h=(b*b)+(p*p)
    print(math.sqrt(h))

# pythagorus(5,8)
#q - write a program to make a calculator using fucntion

def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

def cal():
    repeat =True
    while(repeat):
        choice=int(input("Enter 1.Sum 2.Subtract 3.Multiply 4.Divide  : "))
        a=int(input("First no. : "))
        b=int(input("Second no. : "))
        match choice:
            case 1:
                sum(a,b)
            case 2:
                sub(a,b)
            case 3:
                multi(a,b)
            case 4:
                div(a,b)
            case _:
                print("invalid choice")
        reply = input("Want to continue? y/n  ")
        if(reply=="n"):repeat=False

cal()