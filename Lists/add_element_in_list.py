marks=[89,49,35]
#append function - adds element at the end of the list
marks.append(95)
print(marks)        
marks.append([67,78])  # can add list as an element
print(marks)   
marks.append((67,78))  # can add tuple as an element
print(marks)
marks.append(24,89)  # TypeError: list.append() takes exactly one argument (2 given)
marks.append('A')  # can add different data type
print(marks)   

# insert function - adds element at the specified index
marks.insert(1,67)
print(marks)    
marks.insert(10,67)  # can add at index greater than length of list
print(marks)

# extend function - adds elements of another list at the end of the list
marks.extend([34,78])
print(marks)    
marks.extend((34,78))  # can add tuple as well
print(marks)
marks.extend(34)  # TypeError: 'int' object is not iterable
print(marks)
marks.extend('A')  # can add string as well - adds each character as an element
print(marks)
