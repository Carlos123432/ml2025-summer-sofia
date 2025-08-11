
from module5_mod import NumberCollection

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
