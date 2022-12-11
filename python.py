# This is the program to print the fibonacci numbers and then find
#weather the given numbers are present in the list or not.
# Here I have taken an input upto which user wants the values in the
#Fibonacci List
r = int(input("r: "))
# This is the function which returns the value Fibonacci Series
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)
fibbList = []
for n in range(0, r):
    fibbList.append(fibb(n))
print(fibbList)
num1 = int(input("Enter the number you want to verify: "))
num2 = int(input("Enter the number you want to verify: "))
if (num1 or num2) in fibbList:
    print("{} and {} are present in Fibonacci List.".format(num1, num2))
elif (num1 in fibbList) and (num2 not in fibbList):
    print("{} is present in Fibonacci List, but {} is not present.".format(num1, num2))
elif (num2 in fibbList) and (num1 not in fibbList):
    print("{} is present in Fibonacci List, but {} is not present.".format(num2, num1))
else:
    print("{} and {} are not present in Fibinacci List.".format(num1, num2))
