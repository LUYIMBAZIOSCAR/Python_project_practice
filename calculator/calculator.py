print("--Calculator--")

# Functions for the operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def divide(a,b):
    return a/b
def product(a,b):
    return a*b

num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))

print("Please choose an operation you want to carry out")
print("1.Addition")
print('2.Subtraction')
print("3.Division")
print("4.Mutliplication")

user_choice=input("Please enter your choice: ")

if user_choice=='1':
    result=add(num1,num2)
    print(result)
elif user_choice=='2':
    result=sub(num1,num2)
    print(result)
elif user_choice=='3':
    result=divide(num1,num2)
    print(result)
elif user_choice=='4':
    result=product(num1,num2)
    print(result)
else:
    print("Invalid choice")

    



