def convert_image_to_fdf(file_path):
    from PIL import Image
    try:
        img = Image.open(file_path)
        img = img.convert("L")  # Конвертация в оттенки серого для высот

        fdf_path = file_path.rsplit('.', 1)[0] + ".fdf"
        with open(fdf_path, 'w') as f:
            for y in range(img.height):
                line = []
                for x in range(img.width):
                    # Нормализация высоты
                    height = img.getpixel((x, y)) / 255.0 * 10

                    # Цвет: оттенок серого, соответствующий высоте
                    intensity = height / 10.0  # Нормализация высоты в диапазон [0, 1]
                    color = int(intensity * 255) * 0x010101  # Создаем оттенок серого

                    line.append(f"{height:.2f},{color:06x}")
                f.write(" ".join(line) + "\n")
        return fdf_path
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
        return None
