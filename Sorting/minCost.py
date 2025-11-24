# minimum cost to remove all elements
#given 'n' array elements at every step remove an array element 
#cost to remove element = sum of array elements present in the array 
#find the minimum cost to remove all elements

arr=list(map(int,input().split()))
arr.sort()
arr.reverse()

# -- approach - by calculating sum each time and removing the element from array
# cost=0
# for i in range(len(arr)):
#     cost+=sum(arr)
#     arr=arr[1:]

# print(cost)

# -- approach - by calculating each elements participation based on their index
ar=['a','b','c','d']
#remove a , cost=a+b+c+d
#remove b , cost=b+c+d
#remove c , cost=c+d
#remove d , cost=d
# observation - a+2b+3c+4d

cost=0
for i in range(len(arr)):
    cost+=(arr[i]*(i+1))
print(cost)