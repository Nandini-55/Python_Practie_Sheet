per = int(input("Enter your percentage: "))


if(per>85 and per<100):
    print("Grade A+")
elif(per>65 and per<=85):
   print("Grade A")
elif(per>45 and per<=65):
    print("Grade B")
elif(per>25 and per<=45):
    print("Grade C")
elif(per<=25):
    print("Grade D")

