key = int(input("Enter no. for the day :"))

day = key%7

if(day==1): print("Sunday")
elif(day==2): print("Monday")
elif(day==3):print("Tuesday")
elif(day==4):print("Wednesday")
elif(day==5):print("Thursday")
elif(day==6):print("Friday")
else:print("Saturday")