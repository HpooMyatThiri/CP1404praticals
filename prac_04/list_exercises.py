MIN_SUBJECTS = 1
MAX_SUBJECTS = 5


def main():
    numbers = append_number_into_list()
    print(f"The first number is {numbers[0]} \nThe last number is {numbers[-1]}")
    numbers.sort()
    print(f"The smallest number is {numbers[0]} \nThe largest number is {numbers[-1]}")
    average = calculate_average(numbers)
    print(f"The average of the number is {average}")


def append_number_into_list():
    '''This funtion append number into list'''
    numbers = []
    for user_number in range(MIN_SUBJECTS, MAX_SUBJECTS + 1):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def calculate_average(numbers):
    '''This function calculates average'''
    total_number = 0
    for number in range(len(numbers)):
        number = int(numbers[number - 1])
        total_number += number
    average = total_number / len(numbers)
    return average


main()




usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
current_user_name = input("Username: ")
if current_user_name in usernames:
    result = "Access granted"
else:
    result = "Access denied"
print(result)