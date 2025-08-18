a = int(input("Enter first angle : "))
b = int(input("Enter secondt angle : "))
c = int(input("Enter third angle : "))

def checkType(d):
    if(d==90):
        print(d , " is Right angle.")
    elif(d<90):
        print(d," is Acute angle.")
    else:
        print(d," is Obtuse anlge.")

checkType(a)
checkType(b)
checkType(c)