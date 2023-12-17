from guitar import Guitar

def main():
    file_path = 'guitars.csv'
    guitars = read_guitars_from_file(file_path)
    guitars.sort()
    print("Original Guitars:")
    display_guitars(guitars)
    user_input = input("Do you want to add a new guitar? (yes/no): ").lower()
    while user_input == 'yes':
        new_guitar = add_new_guitar()
        guitars.append(new_guitar)
    write_guitars_to_file(file_path, guitars)
    print("Updated Guitars:")
    display_guitars(guitars)
def read_guitars_from_file(file_path):
    guitars = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name, year, cost = data[0], int(data[1]), float(data[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)
    print()


def write_guitars_to_file(file_path, guitars):
    with open(file_path, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.1f}\n")


def add_new_guitar():
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)

if __name__ == "__main__":
    main()
