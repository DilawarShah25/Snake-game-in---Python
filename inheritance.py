class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhales")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing under the water")
    def swim(self):
        print("can move in water")


nemo = Fish()
nemo.breathe()
eyes = nemo.num_eyes
print(eyes)