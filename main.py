from tkinter import filedialog
import pygame
from model_viewer import Model3DViewer
import convert_to_fdf


def main():
    file_path = filedialog.askopenfilename(
        title="Выберите FDF или изображение",
        filetypes=(("FDF Files", "*.fdf"), ("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*"))
    )
    if not file_path:
        return

    if not file_path.endswith('.fdf'):
        print("Конвертация изображения в FDF...")
        file_path = convert_to_fdf.convert_image_to_fdf(file_path)
        if file_path is None:
            return

    viewer = Model3DViewer(file_path)
    print("Загрузка модели...")

    # Имитация загрузочного экрана
    for i in range(101):
        print(f"Загрузка: {i}%", end="\r")
        pygame.time.wait(10)

    viewer.run()


if __name__ == "__main__":
    main()
