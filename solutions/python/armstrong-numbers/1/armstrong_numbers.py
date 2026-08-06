def is_armstrong_number(number):
    total = 0
    length = len(str(number))
    for digit in str(number):
        digit = int(digit) ** length
        total += digit
    return total == number
    