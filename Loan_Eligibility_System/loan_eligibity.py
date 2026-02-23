print("--Loan Eligibity System--")

age=int(input("Please enter your age: "))
monthly_income=int(input("Please enter your monthly income: "))
credit_score=int(input('Please enter your credit score: '))

if credit_score<1 or credit_score>100:
    print("Credit score must be between 1 and 100")
elif age<21:
    print("Loan request rejected.age must be greater than 21")
elif monthly_income<1000:
    print("Loan request rejected.monthly income is less than 1000")
elif credit_score<61:
    print("Loan request rejected. credit score is too low")
else:
    print("Loan request approved")

