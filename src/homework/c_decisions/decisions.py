def get_options_ratio(num1, num2):
    return num1 / num2
def get_faculty_rating(rat1):
    if rat1 >= 0.9:
        return "Excellent"
    elif rat1 >= 0.85:
        return "Very Good"
    elif rat1 >= 0.7:
        return "Good"
    elif rat1 >= 0.65:
        return "Needs Improvement"
    elif rat1 < 0.65:
        return "Unacceptable"
