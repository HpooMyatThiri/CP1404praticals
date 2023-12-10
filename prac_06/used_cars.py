from prac_06.car import Car


def main():
    """Illustrative test code demonstrating the usage of the car class."""

    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"Current fuel level: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo)


if __name__ == "__main__":
    main()
