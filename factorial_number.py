#factorial of a given number
n = int(input("Enter the factorial of a number : "))
fact = 1
if n < 0:
    print("Factorial does not exist")
elif n == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact *= i
    print("The factorial of ",n,"is",fact)
