import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import read_fdf_file


class Model3DViewer:
    def __init__(self, file_path):
        self.angle_x = 0
        self.angle_y = 0
        self.scale = 1.0

        self.heights, self.colors = read_fdf_file(file_path)

        # Инициализация Pygame
        pygame.init()
        pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("3D Model Viewer with OpenGL")

        glEnable(GL_DEPTH_TEST)
        glClearColor(1.0, 1.0, 1.0, 1.0)

        # Установка начальной матрицы проекции
        self.reshape(800, 600)

        # Создание списка отображения
        self.display_list = self.create_display_list()

    def create_display_list(self):
        display_list = glGenLists(1)
        glNewList(display_list, GL_COMPILE)

        rows, cols = self.heights.shape
        for i in range(rows - 1):
            for j in range(cols - 1):
                glBegin(GL_QUADS)
                glColor3fv(self.colors[i][j])
                glVertex3f(i - rows / 2, j - cols / 2, self.heights[i][j])
                glColor3fv(self.colors[i + 1][j])
                glVertex3f(i + 1 - rows / 2, j - cols / 2, self.heights[i + 1][j])
                glColor3fv(self.colors[i + 1][j + 1])
                glVertex3f(i + 1 - rows / 2, j + 1 - cols / 2, self.heights[i + 1][j + 1])
                glColor3fv(self.colors[i][j + 1])
                glVertex3f(i - rows / 2, j + 1 - cols / 2, self.heights[i][j + 1])
                glEnd()

        glEndList()
        return display_list

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -50.0)
        glRotatef(self.angle_x, 1.0, 0.0, 0.0)
        glRotatef(self.angle_y, 0.0, 1.0, 0.0)
        glScalef(self.scale, self.scale, self.scale)

        glCallList(self.display_list)
        pygame.display.flip()

    @staticmethod
    def reshape(width, height):
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
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.scale *= 1.1
                    elif event.button == 5:
                        self.scale /= 1.1
                elif event.type == MOUSEMOTION and event.buttons[0]:
                    dx, dy = event.rel
                    self.angle_y += dx * 0.5
                    self.angle_x += dy * 0.5
            self.display()
        pygame.quit()