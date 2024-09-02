#6.Find the student from CS department where the roll number may be in capital or smallcase Letters.

print("Find Your Department:")
rollNo=input("Enter your RollNo in syntex = Dept(CS)Year(24)Degree(B/M)Roll(123)")

if len(rollNo)==8:
    branch=rollNo[0:2]
    if branch=='CS' or branch=='Cs' or branch=='cS' or branch=='cs':
        print("Welcome!, You Belong To Computer Science Department")
    else:
        print("Sorry! Your Are Not From Computer Science")
else:
    print("Invalid RollNo.!!")