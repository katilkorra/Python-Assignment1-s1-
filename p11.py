#Primality testing: Given a positive integer, check if the number is prime or not.

num=int(input('Check Number:-'))

if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime Number.")
    else:
        print("It is  Prime Number.")
else:
    print("Not Prime Number.")

