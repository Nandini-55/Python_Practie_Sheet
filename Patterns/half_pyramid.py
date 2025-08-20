num = int(input("Enter no. of rows : "))
#time Complexity - i *j
for i in range(1,num+1):
    for j in range(i):
        print("*",end=" ")
    print()

#time Complexity - i
for i in range(1,num+1):
        print("* "*i)