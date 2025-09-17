def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 40:
        return 'D'
    elif marks >= 0:
        return 'F'
    else:
        return None  # Invalid marks
        

def main():
    print("Student Grade Calculator")
    while True:
        try:
            marks = float(input("Enter the marks (0-100): "))
            if marks < 0 or marks > 100:
                print("Error: Marks should be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

    grade = calculate_grade(marks)
    if grade:
        print(f"Marks: {marks}")
        print(f"Grade: {grade}")
    else:
        print("Invalid marks entered.")

    while True:
        try:
            again = input("Do you want to calculate another grade? (y/n): ").strip().lower()
            if again == 'y':
                main()  # Recursive call to restart
                return
            elif again == 'n':
                print("Thank you for using the Student Grade Calculator!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                continue
        except KeyboardInterrupt:
            print("\nExiting...")
            return

if __name__ == "__main__":
    main()

# Student_Grade_Calculator.py
# A simple program to calculate student grades based on marks

'''
How It Works
The user inputs marks between 0 and 100.
The program checks the range and assigns a grade based on the marks.
Grades are assigned as follows:
Marks Range

Grade

90 - 100
A+

80 - 89
A

70 - 79
B+

60 - 69
B

50 - 59
C

40 - 49
D

0 - 39
F
'''

