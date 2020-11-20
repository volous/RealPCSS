import random


class Bubblesort:

    def __init__(self):
        self.array = []

    # importing random numbers to array 100 times
    def makeArray(self):
        for _ in range(100):
            randint = random.randint(0, 30)
            self.array.append(randint)
        print(self.array)

    #Bubblesort algorithm
    def bubble(self):
        # n is defined as the length of makeArray()
        n = len(self.array)

        for i in range(n):

            for j in range(0, n-i-1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]


test = Bubblesort()
test.makeArray()
test.bubble()
print(test.array)



