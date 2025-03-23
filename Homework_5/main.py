import numpy as np
import random

lines = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

matrix_1 = np.array([[random.randint(1, 50) for _ in range(columns)] for _ in range(lines)])
matrix_2 = np.array([[random.randint(1, 50) for _ in range(columns)] for _ in range(lines)])

print("\nМатрица A:")
print(matrix_1)

print("\nМатрица В:")
print(matrix_2)

print("\nСумма матриц:")
print(matrix_1 + matrix_2)