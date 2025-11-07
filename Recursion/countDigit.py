def countDig(num):
    if(num==0):
        return 0
    return countDig(num//10)+1
num=int(input())
print(countDig(num))