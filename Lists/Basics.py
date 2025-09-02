#List - is used to store mulitple and hetrogenous variables in a single variable

#Creating list
marks=[89,49,35]
print("List of marks of students : ")
print(marks)

#Features of list - 
# can store variables of different data type
details=['Nandini',True,'98']
print("Details of student : ")
print(details)

#can store duplicates 
age=[16,16,17,18,20,20]
print(age)

#Indexing and Accessing elements 

#E.g.- updating marks 
marks[2]=79
print(marks)

# marks[10]=90  # IndexError: list assignment index out of range
# print(marks)

#Accessing elements from 2D list
bill=[['Oil',100],['Bread',55],['Chips',25]]
print("Cost of ",bill[1][0],"is :",bill[1][1])

#List vs Array 
# List - stores heterogenous data types  e.g.-details=['Nandini',True,'98']
# Array - stores homogenous data types e.g.-marks=[89,49,35]


#Length function
print(len(bill))
print(len(bill[0]))


#append function - adds element at the end of the list
marks.append(95)
print(marks)        
#marks.append([67,78])  # can add list as an element
#print(marks)   
#marks.append((67,78))  # can add tuple as an element
#print(marks)
#marks.append(24,89) ` # TypeError: list.append() takes exactly one argument (2 given)
#marks.append('A')  # can add different data type
#print(marks)   

#insert function - adds element at the specified index
marks.insert(1,67)
print(marks)    
#marks.insert(10,67)  # can add at index greater than length of list
#print(marks)

#extend function - adds elements of another list at the end of the list
marks.extend([34,78])
print(marks)    
#marks.extend((34,78))  # can add tuple as well
#print(marks)
#marks.extend(34)  # TypeError: 'int' object is not iterable
#print(marks)
#marks.extend('A')  # can add string as well - adds each character as an element
#print(marks)

#remove function - removes the specified element's first occurrence
marks.remove(67)
print(marks)    
#marks.remove(100)  # ValueError: list.remove(x): x not in list
#print(marks)

#pop function - removes element at the specified index or from the end if index not specified
marks.pop()
print(marks)    
#marks.pop(10)  # IndexError: pop index out of range
#print(marks)

#reverse function - reverses the list - time complexity O(n) space complexity O(1)
marks.reverse()
print(marks)

#reversed function - returns the reversed iterator(object) of the list - time complexity O(n) space complexity O(n)
marks=reversed(marks)  # marks becomes an iterator
print(marks)
marks=list(reversed(marks))  # marks becomes a list again
print(marks)

#reverse slicing - another way to reverse a list
marks=marks[::-1]
print(marks)
#time complexity O(n) space complexity O(n)

# reverse using loop - another way to reverse a list
n=len(marks)
for i in range(n//2):
    marks[i],marks[n-i-1]=marks[n-i-1],marks[i]
print(marks)
#time complexity O(n) space complexity O(1)


