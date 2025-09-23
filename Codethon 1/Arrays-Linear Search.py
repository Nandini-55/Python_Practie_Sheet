n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
target=int(input())
for i in range(n):
    if(target==arr[i]):
        print(i)
        break
    if(i==(n-1)):
       print(-1)