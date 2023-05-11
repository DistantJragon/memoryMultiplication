class Number:
    def __init__(self, value):
        self.value = value
        self.last_step = []
        self.steps = 0
        self.uniqueNumbers = []
        self.dependencies = []
        self.dependents = []

    def update_unique_numbers(self):
        self.uniqueNumbers.clear()
        for term in self.last_step:

            self.uniqueNumbers.append(term.value)


    def update_steps(self):
        self.steps += 1