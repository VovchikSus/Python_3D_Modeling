import numpy as np


def read_fdf_file(file_path):
    heights = []
    colors = []
    with open(file_path, 'r') as f:
        for line in f:
            row_heights = []
            row_colors = []
            for item in line.split():
                if ',' in item:
                    height, color = item.split(',')
                    rgb_color = int(color, 16)
                    color_rgb = (
                        (rgb_color >> 16 & 0xFF) / 255.0,
                        (rgb_color >> 8 & 0xFF) / 255.0,
                        (rgb_color & 0xFF) / 255.0
                    )
                else:
                    height = item
                    # Нормализуем высоту (предполагая максимальную высоту 255)
                    intensity = float(height) / 255.0
                    color_rgb = (intensity, intensity, intensity)

                row_heights.append(float(height))
                row_colors.append(color_rgb)

            heights.append(row_heights)
            colors.append(row_colors)

    return np.array(heights), np.array(colors)
