def get_factorial(val1):
    if val1 == 0:
        return 1
    else:
        int = 1
        for count in range(1, val1 + 1):
            int *= count
        return int
def sum_odd_numbers(num1):
    n = 0
    i = 1
    while i <= num1:
        n += i
        i += 2
    return n