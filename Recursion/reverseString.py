# Write a recursive function to reverse a string
def reverseStr(str):
    if(str==""):
        return ""
    letter=str[len(str)-1]
    return  letter + reverseStr(str[:len(str)-1])
str=input()
print(reverseStr(str))