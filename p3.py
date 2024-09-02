#3.Extracting fields of a roll number using string indexing and slicing.


print("Enter the roll number in this syntex: CS24B234 ")
rno=input("Enter your RollNo:-")
rollNo=rno.upper()

if len(rollNo)==8:
    branch=rollNo[0:2]
    year=int(rollNo[2:4])
    degree=rollNo[4]
    position=int(rollNo[5:8])
    
    print("Your Branch is " ,branch ,"of year " , year, "in ", degree, " degree with class_Roll no is ", position)
else:
    print("Pls Enter the valid RollNo.!!")