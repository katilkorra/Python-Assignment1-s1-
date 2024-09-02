#5.Write a program to find out if the two blood groups match.


p1=input("1st Blood Group:")
p2=input("2nd Blood Group:")
BloodA=p1.upper()
BloodB=p2.upper()

if BloodA and BloodB=="A+" or BloodA and BloodB=="B+" or BloodA and BloodB=="O+" or BloodA and BloodB=="AB+" or BloodA and BloodB=="A-" or BloodA and BloodB=="B-" or BloodA and BloodB=="O-" or BloodA and BloodB=="AB-":
    if(BloodA==BloodB):
        print("Blood Is Matched , its Positive. ")
    else:
        print("Blood Is Not Matched , its Negative. ")
else:
    print("Wrong Blood Group")