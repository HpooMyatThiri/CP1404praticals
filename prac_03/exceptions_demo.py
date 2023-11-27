"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        raise ValueError

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers.txt!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

'''
1.ValueError will happen when the numerator and denominator are not integers.
2.ZeroDivisionError will happen when the denominator is zero.
3.Adding
    if denominator == 0:
        raise ValueError
will avoid the possibility of ZeroDivisionError
'''