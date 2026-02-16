# Stage 3: Student Grade Calculator

def grade_calculator():
    print("Welcome to Student Grade Calculator")
    
    name = input("Enter student name: ")
    
    try:
        marks1 = float(input("Enter marks for subject 1 (0-100): "))
        marks2 = float(input("Enter marks for subject 2 (0-100): "))
        marks3 = float(input("Enter marks for subject 3 (0-100): "))

        if any(m < 0 or m > 100 for m in [marks1, marks2, marks3]):
            print("Invalid marks. Please enter values between 0 and 100.")
            return

        total_marks = marks1 + marks2 + marks3
        percentage = (total_marks / 300) * 100

        grade = ""
        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "F"

        print("\nOutput:")
        print(name)
        print(f"Total: {total_marks:.0f}/300")
        print(f"Percentage: {percentage:.1f}%")
        print(f"Grade: {grade}")
            
    except ValueError:
        print("Invalid input. Please enter numeric marks.")

if __name__ == "__main__":
    grade_calculator()
