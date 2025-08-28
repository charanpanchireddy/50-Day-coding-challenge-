marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 35:
    grade = "C"
else:
    grade = "Fail"

print("Your Grade is:", grade)
