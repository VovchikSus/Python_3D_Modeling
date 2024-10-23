import numpy as np


def draw_3d_model(canvas, heights, scale=10, angle_x=0.5, angle_y=0.5):
    """
    Отрисовка 3D модели на канвасе с учетом матрицы высот.
    """
    canvas_width = canvas.winfo_width() / 2
    canvas_height = canvas.winfo_height() / 2
    rows, cols = heights.shape

    for i in range(rows - 1):
        for j in range(cols - 1):
            # Координаты в пространстве
            x1, y1, z1 = i, j, heights[i][j]
            x2, y2, z2 = i + 1, j, heights[i + 1][j]
            x3, y3, z3 = i, j + 1, heights[i][j + 1]

            # Проекция на 2D плоскость
            p1 = project(x1, y1, z1, canvas_width, canvas_height, scale, angle_x, angle_y)
            p2 = project(x2, y2, z2, canvas_width, canvas_height, scale, angle_x, angle_y)
            p3 = project(x3, y3, z3, canvas_width, canvas_height, scale, angle_x, angle_y)

            # Рисуем линии между точками
            canvas.create_line(p1, p2, fill="black")
            canvas.create_line(p1, p3, fill="black")


def project(x, y, z, cx, cy, scale, angle_x, angle_y):
    """
    Проецирование 3D координат на 2D плоскость.
    """
    # Простейшая изометрическая проекция
    x_new = cx + (x - y) * np.cos(angle_x) * scale
    y_new = cy + (x + y) * np.sin(angle_y) * scale - z * scale * 0.5
    return x_new, y_new
