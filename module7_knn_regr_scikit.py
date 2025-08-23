{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMkEt1vSueeDby27arapc6c"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XEE1Rhh-bvtY",
        "outputId": "7d723a3e-a546-4806-94fa-360af0bf502a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter N: 5\n",
            "Enter k: 2\n",
            "Enter x1: 4\n",
            "Enter y1: 3\n",
            "Enter x2: 3\n",
            "Enter y2: 2\n",
            "Enter x3: 5\n",
            "Enter y3: 3\n",
            "Enter x4: 2\n",
            "Enter y4: 3\n",
            "Enter x5: 6\n",
            "Enter y5: 7\n",
            "Variance of labels: 3.04\n",
            "Enter X: 2\n",
            "Predicted Y: 2.5\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "from sklearn.neighbors import KNeighborsRegressor\n",
        "\n",
        "def main():\n",
        "    N = int(input(\"Enter N: \"))\n",
        "    k = int(input(\"Enter k: \"))\n",
        "\n",
        "    if k > N:\n",
        "        print(\"Error: k cannot be greater than N\")\n",
        "        return\n",
        "\n",
        "    points = []\n",
        "    labels = []\n",
        "    for i in range(N):\n",
        "        x = float(input(\"Enter x\" + str(i+1) + \": \"))\n",
        "        y = float(input(\"Enter y\" + str(i+1) + \": \"))\n",
        "        points.append([x])\n",
        "        labels.append(y)\n",
        "\n",
        "    X_train = np.array(points, dtype=float)\n",
        "    y_train = np.array(labels, dtype=float)\n",
        "\n",
        "    variance = np.var(y_train)\n",
        "    print(\"Variance of labels:\", variance)\n",
        "\n",
        "    model = KNeighborsRegressor(n_neighbors=k)\n",
        "    model.fit(X_train, y_train)\n",
        "\n",
        "    X = float(input(\"Enter X: \"))\n",
        "    prediction = model.predict([[X]])\n",
        "    print(\"Predicted Y:\", float(prediction[0]))\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}