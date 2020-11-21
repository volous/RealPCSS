import random


class Bubblesort:

    def __init__(self):
        self.array = []

    # importing random numbers to array 100 times
    def makeArray(self):
        for _ in range(10000):
            randint = random.randint(0, 30)
            self.array.append(randint)
        print(self.array)

    # Bubblesort algorithm
    def bubble(self):
        # n is defined as the length of makeArray()
        n = len(self.array)

        for i in range(n):

            # boolean if index has changed
            changeIndex = False

            for j in range(0, n - i - 1):
                # Check if the current index is greater than the next index
                if self.array[j] > self.array[j + 1]:
                    # swap index around if the current index is greater than the next index
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

                    # If index changed continue the loop and compare values again
                    changeIndex = True

            # if index is false, check for next iteration  of the loop
            if not changeIndex:
                break


test = Bubblesort()
test.makeArray()
test.bubble()
print(test.array)
