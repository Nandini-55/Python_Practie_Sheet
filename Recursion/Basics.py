# Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller, self-similar subproblems

# Recursion is  a programming technique where a function calls itself directly or indirectly in order to solve a problem
# In a recursive function a function makes one or more calls to itself as a part of its execution 
#The process continue until a base case is reached , at which point the functions stop calling itself and return a result

#   Advantages :- 
# Increase readability
# Solve Complex problem 
# Divide and conqure 
# less lines of code 
 
#Steps 
# 1. -make an assumption- decide what your function does and trust that it will do it 
#2. - main logic - solve the bigger problem using sub problem 
#3. -base case - when your recursion stops

# Q- Write a program to calculate sum of natural no.
# alternative of recursion - iteration - for loop ,  etc.
n=int(input("Enetr no. : "))
sum=0

for i in range(n+1):
    sum+=i
print(sum)

def nSum(n):
    if n==1:
        return 1
    return nSum(n-1)+n
#Recursion 
print(nSum(n))


