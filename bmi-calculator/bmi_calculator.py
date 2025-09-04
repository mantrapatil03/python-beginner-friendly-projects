def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()

# BMI Calculator
# This script calculates the Body Mass Index (BMI) based on user input for weight and height.
# It then categorizes the BMI into standard health categories.


# BMI Calculator
# Enter your weight in kilograms: 70
# Enter your height in meters: 1.75

# Your BMI is: 22.86
# Category: Normal weight
