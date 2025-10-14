
def checkPalindrome(str):
    result=""
    for i in range(len(str)-1,-1,-1):
        result+=str[i]
    if(result==str):
        return 1
    else:
        return 0
n=int(input())
words=[]
for i in range(n):
    words.append(input())

for i in range(n):
    print(checkPalindrome(words[i]))
