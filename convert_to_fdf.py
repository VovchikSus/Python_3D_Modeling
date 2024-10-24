def convert_image_to_fdf(file_path):
    from PIL import Image
    try:
        img = Image.open(file_path)
        # Конвертация в RGB для сохранения цветовой информации
        img = img.convert("RGB")

        fdf_path = file_path.rsplit('.', 1)[0] + ".fdf"
        with open(fdf_path, 'w') as f:
            for y in range(img.height):
                line = []
                for x in range(img.width):
                    # Получаем RGB-значение пикселя
                    r, g, b = img.getpixel((x, y))

                    # Нормализуем высоту на основе яркости
                    # Масштабируем на диапазон [0, 10]
                    height = (r + g + b) / (3 * 255.0) * 10

                    # Сохраняем оригинальный цвет пикселя
                    color = (r << 16) | (g << 8) | b

                    line.append(f"{height:.2f},{color:06x}")
                f.write(" ".join(line) + "\n")
        return fdf_path
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
        return None
