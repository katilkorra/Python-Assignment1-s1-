#2.Find the sum of the first n natural numbers.

num=int(input('Enter N Number::'))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print("sum of n number is : ",sum)