CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year
