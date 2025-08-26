row = int(input("Enter no. of rows : "))
col =int(input("Enter no. of cols : "))

for i in range(row):
     for j in range(col):
        if(j==0 or j==col-1): print("*",end=" ")
        else :print("",end=" ")
     print()