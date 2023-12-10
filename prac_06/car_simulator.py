# from prac_06.car import Car

MENU = ("Menu:\n"
        "d) drive\n"
        "r) refuel\n"
        "q) quit")


def main():
    print("Let's hit the road!")
    car_name = input("Enter your car's name: ")

    # Create a Car instance with an initial fuel level of 100 and the user-provided name
    car = Car(car_name, 100)
    print(car)
    print(MENU)

    user_choice = input("Enter your choice: ").lower()

    while user_choice != "q":
        if user_choice == "d":
            distance_to_drive = int(input("How many kilometers do you want to drive? "))

            while distance_to_drive < 0:
                print("Distance must be >= 0")
                distance_to_drive = int(input("How many kilometers do you want to drive? "))

            distance_driven = car.drive(distance_to_drive)
            print(f"The car covered {distance_driven}km", end="")

            if car.fuel == 0:
                print(" and ran out of fuel", end="")

            print(".")

        elif user_choice == "r":
            fuel_amount = int(input("How many units of fuel do you want to add to the car? "))

            while fuel_amount < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = int(input("How many units of fuel do you want to add to the car? "))

            car.add_fuel(fuel_amount)
            print(f"Added {fuel_amount} units of fuel.")

        else:
            print("Invalid choice")

        print()
        print(car)
        print(MENU)
        user_choice = input("Enter your choice: ").lower()

    print(f"\nFarewell, {car.name}'s driver.")


if __name__ == "__main__":
    main()
