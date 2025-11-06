# Write a program to print numbers from 1 to n using recursion
def printN(n):
    if(n==0):
        return
    printN(n-1)
    print(n)
n=int(input())
printN(n)
