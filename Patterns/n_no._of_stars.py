num = int(input("Enter num : "))
#horizontally
print("Horizontally print : ")
for i in range(num):
    print("*",end=" ")

#veritcally
print()
print("Vertically print : ")
for i in range(num):
     print("*")

# n x n matrix
print("Matrix of n x n print : ")
for i in range(num):
     for j in range(num):
        print("*",end=" ")
     print()