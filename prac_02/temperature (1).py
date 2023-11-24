"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

''''
define main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    display MENU
    get choice 
    while choice != "Q"
        if choice == "C"
            get celsius
            display fahrenheit 
        else if choice == "F"
            get fahrenheit
            display celsius
        else 
            display "Invalid option"
        display MENU
        get choice
    display "Thank you"

define calculate_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

define calculate_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius
    
main()
'''


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius(celsius, fahrenheit)
            print(f"Result: {celsius: .2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(celsius, fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
