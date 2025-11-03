text = input()
result=""
for i in range(len(text)):
    char = text[i]
    if(ord(char)>=65 and ord(char)<=ord('Z') ):
        continue
    elif(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'  ):
        result+="#"
    else:
        result+=char

result*=2
print(result)