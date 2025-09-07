import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Enter N: "))
    train_data = np.zeros((N, 1), dtype=float)
    train_labels = np.zeros(N, dtype=int)
    for i in range(N):
        x = float(input("Enter x" + str(i+1) + ": "))
        y = int(input("Enter y" + str(i+1) + ": "))
        train_data[i, 0] = x
        train_labels[i] = y


    M = int(input("Enter M: "))
    test_data = np.zeros((M, 1), dtype=float)
    test_labels = np.zeros(M, dtype=int)
    for i in range(M):
        x = float(input("Enter x" + str(i+1) + ": "))
        y = int(input("Enter y" + str(i+1) + ": "))
        test_data[i, 0] = x
        test_labels[i] = y

    param_grid = {"n_neighbors": list(range(1, 11))}
    knn = KNeighborsClassifier()
    grid = GridSearchCV(knn, param_grid, cv=3)
    grid.fit(train_data, train_labels)

    best_k = grid.best_params_["n_neighbors"]
    best_model = grid.best_estimator_

    predictions = best_model.predict(test_data)
    accuracy = accuracy_score(test_labels, predictions)

    print("Best k:", best_k)
    print("Test Accuracy:", accuracy)

if __name__ == "__main__":
    main()
