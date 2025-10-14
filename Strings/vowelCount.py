
def countVowel(word):
    count=0
    
    for i in range(len(word)):
        if(word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u' or word[i]=='A' or word[i]=='E' or word[i]=='I' or word[i]=='O' or word[i]=='U'):
            count+=1
    return count

n=int(input())
words=[]
for i in range(n):
    words.append(input())
for i in range(n):
    vowel=countVowel(words[i])
    print(vowel,end=" ")
    print(len(words[i])-vowel)
