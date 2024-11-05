
print(" BMI CALCULATOR")

height = float(input("Enter your height in metres"))
weight = float(input("Enter your weight in kilograms"))

user_BMI = weight // height **2

if user_BMI < 18.5:

     print("you are underweight")

elif user_BMI < 25:

     print("you are average ")

elif user_BMI < 30:
     
     print("you are over weight")

elif user_BMI < 35:
     
     print("you are over obese")

elif user_BMI < 40:
     
     print("you are over very obese")

else:

     print("you are severely obese")