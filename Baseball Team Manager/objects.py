class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.firstName = first_name
        self.lastName = last_name
        self.position = position
        self.atBats = at_bats
        self.hits = hits

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @property
    def battingAvg(self):
        return round(self.hits / self.atBats, 3) if self.atBats > 0 else 0.0
