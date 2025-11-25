#Given n array elements of unique no.s calculate no. of nobel integers present in it.
#  A[i] is set to bt nobel if no. of elements < A[i] = A[i]

# arr=[2,1,0,5,9]
# arr=[1,-5,3,5,-10,4]
# arr=[-3,0,2,5]

#Time complexity - O(n log n)
arr=[-10,-5,1,3,4,5,10]
arr.sort()
nobel=[]
count=0
for i in range(len(arr)):
    if(i==arr[i]):
        nobel.append(arr[i])
        count+=1
    
print("Count of nobel values : ",count)
print(nobel)