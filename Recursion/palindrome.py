def checkPalin(str):
    if(len(str)<=1):
        return True 
    if(str[0]==str[-1]):
        return checkPalin(str[1:-1])
    else:
        return False


str = input()
if(checkPalin(str)):
    print("Palindrome")
else:
    print("Not Palindrome")


