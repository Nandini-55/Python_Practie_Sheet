#ord(b)->98  , chr(66)->B
n=int(input())
char=65
for i in range(n):
    for j in range(i+1):
        print(chr(char),end=" ")
    char+=1
    print()
