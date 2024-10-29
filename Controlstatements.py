
num=int(input("enter number: "))

if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

    #create a program that checks if someone can vote or not using age above 18

age=int(input("enter age: "))

if age>=18:
    print(f"you are eligible to vote")
else:
    print(f"you are under age")

    #CREATE A PROGRAM a TO fail

marks=int(input("enter marks:"))
if marks <= 100 and marks >= 80:
    print("you have an A")
elif marks <= 79  and marks >= 60:
    print("you have a B")
elif marks <= 59 and marks >= 40:
    print("you have a C")
elif marks <= 39 and marks >= 0:
    print("you have FAILED")

#condition checking for bmi calculation..
def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):
    # Determine BMI category
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    # Get user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Print the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {bmi_category(bmi)}")


if __name__ == "__main__":
    main()