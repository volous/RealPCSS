import random
from node import Node, LinkedList


class BubbleSort:
    def __init__(self):
        self.array = []

    # importing random numbers to array 100 times
    def makeArray(self):
        for _ in range(100):
            randint = random.randint(0, 30)
            self.array.append(randint)
        print(self.array)

    # bubble sort algorithm
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


# run this to bubble sort random numbers, the values randomly generated will then be inserted into a LinkedList
bub = BubbleSort()
bub.makeArray()
bub.bubble()
print(bub.array)
search = input("input number you wish to search for: ")
llist = LinkedList(bub.array)
for i in range(len(bub.array)):
    llist.push(bub.array[i])
# inside of this if statement a number can be inserted that is between 0 and 30 and there will be a search performed
if llist.search(int(search)):
    print(search, "is in list")
else:
    print(search, "is not in list")
