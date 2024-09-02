#Print Fibonacci sequence.

def fibonacci(n):
    first=1
    second=0
    sum=0
    for i in range(n):
        print(sum)
        sum=first+second
        first=second
        second=sum
    print()

num = int(input("Enter the number: "))
fibonacci(num)