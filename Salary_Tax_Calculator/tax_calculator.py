print("--Simple tax Calculator--")

# This allows the user to enter his salary
user_salary=float(input("Please enter your salary: "))

# salary below 1000
if user_salary<1000:
    print('Salary is not taxable')
# salary between 1000 and 5000 inclusive
elif user_salary>=1000 and user_salary<=5000:
    tax_rate=0.1
    tax= user_salary*tax_rate
    net_salary=user_salary-tax
    print(f'Your tax amount is {tax} and your remaining salary is {net_salary}')

else:
    tax_rate=0.2
    tax=user_salary*tax_rate
    net_salary=user_salary-tax
    print(f'Your tax amount is {tax} and your remaining salary is {net_salary}')


    



