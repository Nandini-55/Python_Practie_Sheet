def reverseWord(word):
    result=""
    for i in range(len(word)-1,-1,-1):
        result+=word[i]
    return result

str=input()
print(reverseWord(str))