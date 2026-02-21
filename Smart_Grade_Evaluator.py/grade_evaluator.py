print("--Smart Grade Evualator--")
# This allows the student to his or her score
score=int(input("Please enter your score: "))

# conditional statement for grading
if score<0 or score>100:
    print("Value must be between 0 and 100")
elif score<60:
    print("F")
elif score<=69:
    print("D")
elif score<=79:
    print("C")
elif score<=89:
    print("B")
else:
    print("A")

