from prac_06.guitar import Guitar


def main():
    """Guitar program utilizing the Guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Enter guitar name: ")

    while name != "":
        year = int(input("Enter the year: "))
        cost = float(input("Enter the cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} has been added.")
        name = input("Enter guitar name: ")

    # Adding predefined guitars
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_info = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), valued at ${guitar.cost:,.2f}{vintage_info}")
    else:
        print("No guitars found. Hurry, go get one!")


if __name__ == "__main__":
    main()
