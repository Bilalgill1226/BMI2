Height=float(input("Enter the height in cm :"))
Weight=int(input("Enter the weight in kg :"))
Height_ = Height**2
BMI = Weight/Height_
BMI_=round(BMI,2)
if BMI_<18.5:
  print(f"Your BMI is {BMI_},you are underweight")
elif BMI_<25:
  print(f"Your BMI is {BMI_},you are normal weight")
elif BMI_<30:
  print(f"Your BMI is {BMI_},you are slightly over weight")
elif BMI_<35:
  print(f"Your BMI is {BMI_},you are obese")
else:
  print(f"Your BMI is {BMI_},you are clinically obese")

