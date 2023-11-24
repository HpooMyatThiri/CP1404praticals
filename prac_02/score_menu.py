'''
define main():
    MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""
    display MENU
    get user_choice
    while user_choice != "Q":
        if user_choice == "G":
            user_score = get_valid_score()
        else if user_choice == "P":
            dsiplay (decides_result(user_score))
        else if user_choice == "S":
            print_asterisks(user_score)
            display()
        get user_choice
    display "Thank you for using!"


define print_asterisks(score):
    for i in range of (1, score + 1):
        display "*"


define get_valid_score():
    get score
    while score < 0 or score > 100:
        display "Invalid score!"
        get score
    return score

define decides_result(score):
    if score >= 90:
        result = "Excellent"
    else if score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()

'''


def main():
    MENU = """(G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit"""
    print(MENU)
    user_choice = input(">>>").upper()
    while user_choice != "Q":
        if user_choice == "G":
            user_score = get_valid_score()
        elif user_choice == "P":
            print(decides_result(user_score))
        elif user_choice == "S":
            print_asterisks(user_score)
            print()
        user_choice = input(">>>").upper()
    print("Thank you for using!")

def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Score: "))
    return score

def print_asterisks(score):
    for i in range(1, score + 1):
        print("*", end="")

def decides_result(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
