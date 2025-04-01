import os
import pandas as pd
from pandas.errors import EmptyDataError
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLineEdit, QComboBox, QMessageBox

def generating_test_data() -> None:
    """
    Создает тестовые файлы в форматах: csv, json
    :return:
    """
    data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "age": [25, 30, 35, 40, 45],
        "email": [
            "alice@example.com",
            "bob@example.com",
            "charlie@example.com",
            "david@example.com",
            "eva@example.com",
        ],
    }

    # Создание DataFrame
    df = pd.DataFrame(data)

    # Сохранение в CSV
    csv_file_path = "test_data/test_data.csv"
    df.to_csv(csv_file_path, index=False, sep=';')
    print(f"Тестовые данные сохранены в {csv_file_path}")

    # Сохранение в JSON
    json_file_path = "test_data/test_data.json"
    df.to_json(json_file_path, orient="records", lines=True)
    print(f"Тестовые данные сохранены в {json_file_path}")

class MyConverter(QWidget):
    FORMAT = "JSON"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Конвертер файлов")
        self.setGeometry(1000, 1000, 500, 250)

        # Выбор в какой формат необходимо
        self.combobox = QComboBox()
        self.combobox.addItem("CSV -> JSON")
        self.combobox.addItem("JSON -> CSV")
        self.combobox.currentTextChanged.connect(self.format_selection)
        # Кнопка для преобразования
        self.button_upload_file = QPushButton("Загрузить файл")
        self.button_upload_file.clicked.connect(self.get_path_file)

        # Поля для указания пуди до файла
        self.line_edit = QLineEdit()  # Создаем поле для ввода текста
        self.line_edit.setPlaceholderText("Укажите путь до файла")  # Текст-подсказка

        # Установка компоновщика
        layout = QVBoxLayout()
        layout.addWidget(self.combobox)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button_upload_file)
        self.setLayout(layout)

    def get_path_file(self):
        """
        Этот метод обрабатывает ввод пользователя,
        проверяет формат файла и вызывает соответствующую функцию для конвертации.
        Она также обрабатывает ошибки и отображает сообщения пользователю.
        :return:
        """
        path = self.line_edit.text()
        try:

            # Проверка формата файла
            if self.FORMAT == "JSON":
                if path.endswith(".json"):
                    raise ValueError("Вы пытаетесь конвертировать файл в тот же формат.")
                info = self.format_translation_csv(path)  # Конвертация из CSV в JSON
            elif self.FORMAT == "CSV":
                if path.endswith(".csv"):
                    raise ValueError("Вы пытаетесь конвертировать файл в тот же формат.")
                info = self.format_translation_json(path)  # Конвертация из JSON в CSV

            # Сообщение об успешной конвертации
            message = QMessageBox()
            message.setWindowTitle("Конвертирование выполнено!")
            message.setText(info)
            message.setIcon(QMessageBox.Information)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()

        except EmptyDataError:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Файл пуст! Его необходимо наполнить данными или выбрать другой.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec()

        except ValueError as ve:
            # Обработка ошибки, если файл уже в нужном формате
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText(str(ve))
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec()

        except Exception as er:
            # Обработка других ошибок, например, файл не найден
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Файл не найден! Возможно вы указали неверный путь или название файла.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.setDetailedText(str(er))
            error.exec()

    def format_selection(self, format: str):
        """
        Этот метод обновляет глобальную переменную FORMAT
        в зависимости от выбранного формата в комбобоксе.
        :param format:
        :return:
        """
        # global FORMAT
        self.FORMAT = format.split()[-1]

    def format_translation_csv(self, file_path: str) -> str:
        """
        Преобразует csv файл в json
        :param file_path: Путь к CSV файлу
        :return: Сообщение об успешном сохранении
        """

        name_file = os.path.basename(file_path)
        # Чтение данных из CSV файла
        df = pd.read_csv(file_path, sep=';')

        # Создание директории для результатов, если она не существует
        os.makedirs("result", exist_ok=True)

        # Сохранение данных в JSON файл
        json_file_path = f'{name_file.split(".")[0]}.json'
        df.to_json("result/" + json_file_path, orient='records', lines=True)

        current_directory = os.getcwd()
        return f"Данные из '{file_path}' успешно сохранены в '{current_directory}/result/{json_file_path}'."

    def format_translation_json(self, file_path: str) -> str:
        """
        Преобразует json файл в csv
        :param file_path: Путь к JSON файлу
        :return: Сообщение об успешном сохранении
           """
        name_file = os.path.basename(file_path)
        # Чтение данных из JSON файла
        df = pd.read_json(file_path, lines=True)

        # Создание директории для результатов, если она не существует
        os.makedirs("result", exist_ok=True)

        # Сохранение данных в CSV файл
        csv_file_path = f'{name_file.split(".")[0]}.csv'
        df.to_csv("result/" + csv_file_path, index=False, sep=";")

        current_directory = os.getcwd()
        return f"Данные из '{file_path}' успешно сохранены в '{current_directory}/result/{csv_file_path}'."


