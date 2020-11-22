class Search:

    def __init__(self, list):

        self.list = list

    def search_in_out(self):
        self.search_input = int(input("Search for a numbers between 0 and 30: "))
        if self.search_input in self.list:
            print(f"\n %s is found in the list, at index" % int((self.list.index(self.search_input))))
        else:
            print(f"\n not in array")