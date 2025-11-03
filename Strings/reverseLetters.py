def reverseWord(word):
    result=""
    for i in range(len(word)-1,-1,-1):
        result+=word[i]
    return result

str=input()
lst=str.split()
result=""
for i in range(len(lst)):
    word=lst[i]
    word=reverseWord(word)
    result+=word+" "

print(result)