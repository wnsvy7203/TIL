class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1

    def bark(self):
        return f'멍멍'

    @classmethod
    def get_status(cls):
        return f'태어난 개: {cls.birth_of_dogs}, 현재 마리 수: {cls.num_of_dogs}'