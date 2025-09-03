#map(function,iterable(list,tuples,dictionary,etc.))  fucntion - returns object
m=map(int,input().split())
print(m) #<map object at 0x0000021CA49F22F0>

A=list(m)
print(A)

#DRY RUN 

i ="1 2 3 4 5"
s=i.split()
print(s)
m=map(int,s)
A=list(m)
for i in range(len(A)):
    print(A[i],end=" ")

#Q- given an array compute the sum of all elements

m=list(map(int,input().split()))
sum=0
for i in range(len(m)):
    sum+=m[i]

print(sum)


#Q-find maximum

m=list(map(int,input().split()))
max=m[0] # want to take -infinite = -float("inf")
for i in range(1,len(m)):
    max=m[i] if m[i]>max else max

print("Maximum value : ",max)

#Q  - given an array and a target find no. of occurrence of the target

m=list(map(int,input().split()))
target=int(input("Target : "))
count=0
for i in range(len(m)):
    count+=1 if m[i]==target else 0

print("Count of",target,"is :",count)

