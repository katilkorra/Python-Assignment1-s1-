# Find Out pass-percentage of a class.


students=int(input("Total Students : "))
countStudent=0
i=1
while(i<=students):
    marks=int(input("Student Marks is: "))
    if(marks>100 or marks<0):
        print("Pls Enter Valid Marks")
    elif(marks>=40):
        countStudent+=1
    i+=1  
    

percentage =int((countStudent*100)/students)
print("Percantage of Passing Students is : ", percentage,"%")