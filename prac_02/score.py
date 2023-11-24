"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

'''
define main():
    get score
    display (decides_result(score))


define decides_result(score):
    if score < 0 or score > 100:
        result= "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()

'''
def main():
    score = float(input("Score: "))
    print(decides_result(score))


def decides_result(score):
    if score < 0 or score > 100:
        result= "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
