yr = int(input("Enter year : "))

if(yr%100==0):
    if(yr%400==0):
        print(yr," is a leap year.")
    else:
        print(yr," is not a leap year.")
else:
    if(yr%4==0):
        print(yr," is a leap year.")
    else:
        print(yr," is not a leap year.")