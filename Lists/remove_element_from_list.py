marks=[89,49,35]
#remove function - removes the specified element's first occurrence
marks.remove(67)
print(marks)    
marks.remove(100)  # ValueError: list.remove(x): x not in list
print(marks)

# pop function - removes element at the specified index or from the end if index not specified
marks.pop()
print(marks)    
marks.pop(1)
print(marks)    
marks.pop(10)  # IndexError: pop index out of range
print(marks)
