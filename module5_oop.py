
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

def main():
    while True:
        try:
            N = int(input("Enter N (positive integer): "))
            if N <= 0:
                print("N must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    collection = NumberCollection()
    collection.read_numbers(N)
    
    while True:
        try:
            X = int(input("Enter X (integer to search): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    result = collection.search_number(X)
    print(result)

if __name__ == "__main__":
    main()
