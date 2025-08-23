import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Enter N: "))
    k = int(input("Enter k: "))

    if k > N:
        print("Error: k cannot be greater than N")
        return

    points = []
    labels = []
    for i in range(N):
        x = float(input("Enter x" + str(i+1) + ": "))
        y = float(input("Enter y" + str(i+1) + ": "))
        points.append([x])
        labels.append(y)

    X_train = np.array(points, dtype=float)
    y_train = np.array(labels, dtype=float)

    variance = np.var(y_train)
    print("Variance of labels:", variance)

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    X = float(input("Enter X: "))
    prediction = model.predict([[X]])
    print("Predicted Y:", float(prediction[0]))


if __name__ == "__main__":
    main()
