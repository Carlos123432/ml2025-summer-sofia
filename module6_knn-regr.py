import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def predict(self, X):
        if len(self.points) == 0:
            return "Error: no points"
        data = np.array(self.points, dtype=float)
        if data.ndim != 2 or data.shape[1] != 2:
            return "Error: invalid data"
        xs = data[:, 0]
        ys = data[:, 1]
        distances = np.abs(xs - X)
        idx = np.argsort(distances)[:self.k]
        return float(np.mean(ys[idx]))

def main():
    N = int(input("Enter N: "))
    k = int(input("Enter k: "))
    if k > N:
        print("Error: k cannot be greater than N")
        return
    model = KNNRegression(k)
    for i in range(N):
        x = float(input("Enter x" + str(i+1) + ": "))
        y = float(input("Enter y" + str(i+1) + ": "))
        model.add_point(x, y)
    X = float(input("Enter X: "))
    print(model.predict(X))

if __name__ == "__main__":
    main()