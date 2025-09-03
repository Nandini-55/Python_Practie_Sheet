marks=[89,49,35]
# reverse function - reverses the list - time complexity O(n) space complexity O(1)
marks.reverse()
print(marks)

# reversed function - returns the reversed iterator(object) of the list - time complexity O(n) space complexity O(n)
reversed_marks=reversed(marks)  # marks becomes an iterator
print(reversed_marks)
reversed_marks=list(reversed_marks)  # marks becomes a list again
print(reversed_marks)

# reverse slicing - another way to reverse a list
marks=marks[::-1]
print(marks)
# time complexity O(n) space complexity O(n)

# reverse using loop - another way to reverse a list
n=len(marks)
for i in range(n//2):
    marks[i],marks[n-i-1]=marks[n-i-1],marks[i]
print(marks)
# time complexity O(n) space complexity O(1)
