import csv
import time
def time_decorator(func): #декоратор с семинара
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print('time=', time.time() - start_time)
        return res
    return wrapper
matrix_1=[]
matrix_2=[]
with open ("matrix_1.csv", encoding='utf-8') as file_1:
    reader = csv.reader(file_1, delimiter=';')
    for row in reader:
        matrix_1.append(list(map(int, row)))
with open("matrix_2.csv", encoding='utf-8') as file_2:
    reader = csv.reader(file_2, delimiter=";")
    for row in reader:
        matrix_2.append(list(map(int, row)))

@time_decorator
def mul (matrix_1, matrix_2):
    matrix_12 = [[0] * len(matrix_2[0]) for _ in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_1[0])):
                matrix_12[i][j]+= matrix_1[i][k]*matrix_2[k][j]
    return matrix_12
print(mul(matrix_1, matrix_2))