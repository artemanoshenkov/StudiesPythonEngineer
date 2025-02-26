import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication(sys.argv)

def center_widget():
    #Центрует окно
    qr = window.frameGeometry()
    cp = QApplication.desktop().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())

def clic_button():
    #Добавление счета по нажатию кнопки
    global count
    count += 1
    counter.setText(f"Счетчик: {count}")

#Инициализация окна
window = QWidget()
window.setWindowTitle("Счетчик кликов")
window.setGeometry(100, 100, 310, 150)
center_widget()

#Инициализация кнопки
button = QPushButton()
button.setText("Кликни меня")
button.clicked.connect(clic_button)

#Инициализация вывода результата счетчика
count = 0
counter = QLabel("Счетчик: 0")

#Расположение кнопки и счетчика
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(counter)

#Добавление кнопки и счетчика в основное окно
window.setLayout(layout)

window.show()
sys.exit(app.exec())