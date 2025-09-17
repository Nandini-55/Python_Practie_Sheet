n = int(input("Enter no. of students :"))
marks= list(map(int,input().split()))
passed=0
failed=0

for mark in marks:
    if(mark>=35):passed+=1
    else:failed+=1
print(passed,failed)
