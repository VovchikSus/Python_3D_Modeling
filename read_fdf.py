import numpy as np


def read_fdf_file(file_path):
    """
    Чтение FDF файла и получение матрицы высот.
    Предполагается, что FDF файл содержит матрицу чисел, разделенных пробелами.
    """
    heights = []
    with open(file_path, 'r') as f:
        for line in f:
            row = list(map(float, line.split()))
            heights.append(row)
    return np.array(heights)
