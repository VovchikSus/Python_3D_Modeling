import sys
from tkinter import filedialog
import pygame
from pygame.locals import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

class Model3DViewer:
    def __init__(self, file_path):
        self.angle_x = 0
        self.angle_y = 0

        self.scale = 1.0
        self.last_mouse_x = 0
        self.last_mouse_y = 0

        self.heights, self.colors = self.read_fdf_file(file_path)

        # Инициализация Pygame
        pygame.init()
        pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("3D Model Viewer with OpenGL")

        glEnable(GL_DEPTH_TEST)
        glClearColor(1.0, 1.0, 1.0, 1.0)

        # Установка начальной матрицы проекции
        self.reshape(800, 600)

    def read_fdf_file(self, file_path):
        heights = []
        colors = []
        with open(file_path, 'r') as f:
            for line in f:
                row_heights = []
                row_colors = []
                for item in line.split():
                    height, color = item.split(',')
                    row_heights.append(float(height))
                    rgb_color = int(color, 16)
                    row_colors.append((
                        (rgb_color >> 16 & 0xFF) / 255.0,
                        (rgb_color >> 8 & 0xFF) / 255.0,
                        (rgb_color & 0xFF) / 255.0
                    ))
                heights.append(row_heights)
                colors.append(row_colors)
        return np.array(heights), np.array(colors)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Перемещение камеры назад для обзора модели
        glTranslatef(0.0, 0.0, -50.0)

        # Повороты модели
        glRotatef(self.angle_x, 1.0, 0.0, 0.0)
        glRotatef(self.angle_y, 0.0, 1.0, 0.0)

        # Масштабирование модели
        glScalef(self.scale, self.scale, self.scale)

        rows, cols = self.heights.shape
        for i in range(rows - 1):
            for j in range(cols - 1):
                glBegin(GL_QUADS)
                # Вершина 1
                glColor3fv(self.colors[i][j])
                glVertex3f(i - rows / 2, j - cols / 2, self.heights[i][j])
                # Вершина 2
                glColor3fv(self.colors[i + 1][j])
                glVertex3f(i + 1 - rows / 2, j - cols / 2, self.heights[i + 1][j])
                # Вершина 3
                glColor3fv(self.colors[i + 1][j + 1])
                glVertex3f(i + 1 - rows / 2, j + 1 - cols / 2, self.heights[i + 1][j + 1])
                # Вершина 4
                glColor3fv(self.colors[i][j + 1])
                glVertex3f(i - rows / 2, j + 1 - cols / 2, self.heights[i][j + 1])
                glEnd()

        pygame.display.flip()

    def reshape(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 1, 1000)
        glMatrixMode(GL_MODELVIEW)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 4:  # Колесико мыши вверх
                        self.scale *= 1.1
                    elif event.button == 5:  # Колесико мыши вниз
                        self.scale /= 1.1
                elif event.type == MOUSEMOTION:
                    if event.buttons[0]:  # Левая кнопка мыши зажата
                        dx, dy = event.rel
                        self.angle_y += dx * 0.5
                        self.angle_x += dy * 0.5
            self.display()
        pygame.quit()

def main():
    file_path = filedialog.askopenfilename(
        title="Выберите FDF файл",
        filetypes=(("FDF Files", "*.fdf"), ("All Files", "*.*"))
    )
    if not file_path:
        return

    viewer = Model3DViewer(file_path)
    viewer.run()

if __name__ == "__main__":
    main()