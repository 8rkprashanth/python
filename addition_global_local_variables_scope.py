#creating addition of 2 values
from audioop import add


def addition(a,b):
    return a+b

#main program
num1 = float(input("enter the number one value\n"))
num2 = float(input('enter the number second value\n'))

#call function
result = addition(num1,num2)
print("the addition of entered 2 numbers is ",result)


def main():
    num1 = float(input("enter the number one value\n"))
    num2 = float(input('enter the number second value\n'))
    result1 = addition(num1,num2)
    print("the addition of entered 2 numbers is ",result1)

main()