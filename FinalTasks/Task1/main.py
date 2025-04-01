import sys
from modules import generating_test_data, MyConverter
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    generating_test_data()# Создаем тестовые данные
    app = QApplication(sys.argv)
    window = MyConverter()
    window.show()
    sys.exit(app.exec_())