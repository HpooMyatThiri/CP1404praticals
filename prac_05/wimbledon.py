FILE_PATH = "wimbledon.csv"
COUNTRY_COLUMN = 1
CHAMPION_COLUMN = 2

def main():
    """Read the data file and display information about Wimbledon champions and participating countries."""

    entries = retrieve_entries(FILE_PATH)
    champion_counts, participating_countries = analyze_entries(entries)
    show_results(champion_counts, participating_countries)

def analyze_entries(entries):
    """Create a dictionary of champions and a set of countries from the provided entries (a list of lists)."""

    champion_counts = {}
    countries_set = set()

    for entry in entries:
        countries_set.add(entry[COUNTRY_COLUMN])
        try:
            champion_counts[entry[CHAMPION_COLUMN]] += 1
        except KeyError:
            champion_counts[entry[CHAMPION_COLUMN]] = 1

    return champion_counts, countries_set

def show_results(champion_counts, countries_set):
    """Display information about champions and countries."""

    print("Wimbledon Champions: ")
    for name, count in champion_counts.items():
        print(name, count)
    print(f"\nThese {len(countries_set)} countries have secured victory at Wimbledon: ")
    print(", ".join(country for country in sorted(countries_set)))

def retrieve_entries(file_path):
    """Fetch entries from the file and represent them as a list of lists."""

    entries_list = []

    with open(file_path, "r", encoding="utf-8-sig") as input_file:
        input_file.readline()  # Skip the header
        for line in input_file:
            parts = line.strip().split(",")
            entries_list.append(parts)

    return
