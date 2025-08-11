
class NumberCollection:
    def __init__(self):
        self.numbers = []
    
    def read_numbers(self, n):
        for i in range(n):
            while True:
                try:
                    num = int(input(f"Enter number {i+1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Please enter a valid integer.")
    
    def search_number(self, x):
        try:
            index = self.numbers.index(x) + 1
            return index
        except ValueError:
            return -1
