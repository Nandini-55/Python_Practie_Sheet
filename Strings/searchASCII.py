str=input()
asci=chr(int(input()))
for i in range(len(str)):
    if(asci==str[i]):
        print(i)
        break
    if(i==len(str)-1):
        print("Not present")
