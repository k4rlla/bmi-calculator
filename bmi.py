height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / ((height / 100) ** 2)

if bmi < 16 :
    print("Severe Thinness")
elif bmi >= 16 and bmi < 17:
    print("Moderate Thinness")
elif bmi >= 17 and bmi < 18.5 :
    print("Mild Thinness")
elif bmi >= 18.5 and bmi < 25 :
    print("Normal")
elif bmi >= 25 and bmi < 30 :
    print("Overweight")
elif bmi >= 30 and bmi < 35 :
    print("Obese Class I")
elif bmi >= 35 and bmi < 40 :
    print("Obese Class II")
else: 
    print("Obese Class III")
