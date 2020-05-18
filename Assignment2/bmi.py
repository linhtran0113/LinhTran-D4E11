weight = int(input("your weight (kg) :"))
height = int(input("your height (cm) :"))
height_m = height / 100
bmi = weight / height_m**2

if bmi < 16:
    print("Severely Underweight")
elif 16 <= bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
