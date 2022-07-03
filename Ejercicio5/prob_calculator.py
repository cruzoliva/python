import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for x, i in kwargs.items():
            for y in range(i):
                self.contents.append(x)
        self._initial = copy(self.contents)

    def draw(self, count):
        try:
            drawn = random.sample(self.contents, count)
        except ValueError:
            drawn = copy(self.contents)

        for item in drawn:
            self.contents.remove(item)

        if len(self.contents) == 0:
            self.contents = copy(self._initial)

        return drawn


def experiment(Hat, expected_balls, num_drawn_balls, num_experiments):

    


