def calculate_grade(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"
