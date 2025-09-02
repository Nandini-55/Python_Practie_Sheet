# range function gives range of no. : range(start , end , step )
# default  value of start->0 and step->1  # end must be passed as argument
# range -> list -> iterable
# this method is used in for loop 

print(range(0,6)) # output - range(0, 6)
print(list(range(0,6))) # output - [0, 1, 2, 3, 4, 5]
#iterables - object that can be iterated  - range , lists , tuples , sets , dictionaries and string

for i in range(1,10,2):
    print(i)

for i in range(1,10,2):
    print(i*i , end=" ")
 
