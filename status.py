class Status:
    def __init__(self, hunger=50, happiness=50, energy=50):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def feed(self):
        self.hunger = min(100, self.hunger + 20)
        self.energy = max(0, self.energy - 10)

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 15)
        self.hunger = max(0, self.hunger - 10)

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.happiness = max(0, self.happiness - 10)
        self.hunger = max(0, self.hunger - 5)

    def get_status(self):
        return {
            "hunger": self.hunger,
            "happiness": self.happiness,
            "energy": self.energy
        }
