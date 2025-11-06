#Write a program to print n to 1
def reverseN(n):
    if(n==0):
        return 
    print(n)
    reverseN(n-1)
n=int(input())
reverseN(n)