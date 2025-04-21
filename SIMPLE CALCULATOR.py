#WELCOME TO THE SIMPLE CALCULATOR
#This is a simple calculator that can perform addition, subtraction, multiplication, and division.
num1=int(input("Enter a number: "))
operand=input("Enter an operator (+, -, *, /): ")
num2=int(input("Enter another number: "))
print("Calculating...")
if operand == '+':
    result = num1 + num2
    print(num1,operand, num2," =" ,result)
if operand == '-':
    result = num1 - num2
    print(num1,operand, num2 ,"= ",result)
if operand == '*':
    result = num1 * num2
    print(num1,operand, num2 ,"= ",result)
if operand == '/':
    if num2 != 0:
        result = num1 / num2
        print(num1,operand, num2 ,"= ",result)
print(result)
print("Thank you for using the simple calculator!")
