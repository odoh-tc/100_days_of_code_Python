height = float(input("Enter your height in meters\n"))
weight = int(input("Enter your weight in Kg\n"))

bmi_index = weight / (height ** 2)
if bmi_index < 18.5:
    print(f"Your BMI is {bmi_index} kg/m², you are underweight.")
elif 18.5 < bmi_index < 25:
    print(f"Your BMI is {bmi_index} kg/m², you have a normal weight.")
elif 25 <= bmi_index < 30:
    print(f"Your BMI is {bmi_index} kg/m², you are slightly overweight.")
elif 30 <= bmi_index < 35:
    print(f"Your BMI is {bmi_index} kg/m², you are obese.")
else:
    print(f"Your BMI is {bmi_index} kg/m², you are clinically obese")