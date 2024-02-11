from decisions import get_faculty_rating
from decisions import get_options_ratio
val1 = int(input("Enter Numerator:\n"))
val2 = int(input("Enter Denominator:\n"))
print("Options Ratio: ", get_options_ratio(val1, val2))
print("Faculty Rating: ", get_faculty_rating(get_options_ratio(val1, val2)))