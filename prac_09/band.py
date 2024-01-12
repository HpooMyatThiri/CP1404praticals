class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        self.members.append(musician)

    def play(self):
        return [member.play() for member in self.members]

    def __str__(self):
        members_str = [str(member) for member in self.members]
        return f"{self.name} ({', '.join(members_str)})"
