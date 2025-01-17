# 3D Model Viewer

### Описание
Эта программа представляет собой 3D-движок, предназначенный для отображения и взаимодействия с 3D-моделями, основанными на данных высот и цветов. Она позволяет загружать модели из файлов формата FDF или конвертировать изображения в FDF для последующего 3D-отображения.

### Функциональность
- **Загрузка файлов формата FDF**: Файл FDF содержит данные о высоте и цвете каждой точки модели.
- **Конвертация изображений в FDF**: Программа поддерживает изображения форматов PNG, JPG и JPEG, конвертируя их в 3D-модели.
- **Интерактивное взаимодействие**: Возможность вращения модели, масштабирования и перемещения с помощью мыши.
- **Рендеринг с использованием OpenGL**: 3D-отображение и рендеринг моделей выполняются с использованием OpenGL.

### Требования
- Python 3.6+
- Библиотеки:
  - `pygame`
  - `PyOpenGL`
  - `numpy`
  - `PIL` (или `Pillow`)

Для установки всех необходимых библиотек используйте следующую команду:
```bash
pip install pygame PyOpenGL numpy Pillow
```

### Установка
1. Клонируйте репозиторий или скачайте исходный код.
2. Убедитесь, что у вас установлены все необходимые библиотеки.
3. Запустите программу, используя следующую команду:
   ```bash
   python main.py
   ```

### Как использовать
1. При запуске программы откроется окно выбора файла. Выберите файл формата `.fdf` или изображение (PNG, JPG, JPEG).
2. Если выбран файл изображения, программа конвертирует его в FDF-формат и отобразит результат в 3D.
3. Используйте мышь для взаимодействия с моделью:
   - **Левая кнопка мыши**: Вращение модели.
   - **Колесико мыши**: Масштабирование модели.

### Формат FDF
Формат FDF представляет собой текстовый файл, в котором каждая строка содержит данные о высоте и цвете в следующем формате:
```
высота1,цвет1 высота2,цвет2 ...
```
Например:
```
1.2,FF0000 1.5,00FF00 0.8,0000FF
1.1,FFAA00 1.4,AAFF00 0.7,00AAFF
```

### Основные файлы
- **`main.py`** - основной файл для запуска программы.
- **`model_viewer.py`** - класс для отображения и управления 3D-моделью.
- **`convert_to_fdf.py`** - модуль для конвертации изображений в формат FDF.
- **`utils.py`** - содержит функцию `read_fdf_file`, которая загружает данные из FDF-файла.

### Пример работы
При запуске программа предложит выбрать файл FDF или изображение. После выбора изображения оно будет конвертировано в FDF и отобразится в виде 3D-модели, где высота определяется яркостью пикселя изображения.

![Пример работы](https://github.com/VovchikSus/Python_3D_Modeling/blob/main/3DfDF.png)

### Заметки
- При отсутствии информации о цветах в FDF, программа будет отрисовывать модель в белом цвете.
- При работе с большими изображениями или моделями возможно увеличение времени загрузки и рендеринга.

### Лицензия
Программа является свободным программным обеспечением и распространяется под лицензией MIT.


