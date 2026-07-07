# # pip install pyqt6
# import sys
#
# from PyQt6.QtWidgets import (
#     QMessageBox,
#     QPushButton,
#     QMainWindow,
#     QTextEdit,
#     QFileDialog,
#     QApplication,
#     QVBoxLayout,
#     QWidget,
# )
#
#
# class MyNoteApp(QMainWindow):
#     def save_note(self):
#         file_dialog = QFileDialog.getSaveFileName(self, "Сохранение!", "", "Text Files (*.txt)")
#         file_path = file_dialog[0]
#         if file_path:
#             with open(file_path, "w") as file:
#                 text_edit_info = self.text_edit.toPlainText()
#                 file.write(text_edit_info)
#                 QMessageBox.information(self, "Успешно!", "Файл успешно сохранен!")
#
#     def export_note(self):
#         file_dialog = QFileDialog.getOpenFileName(self, "", "Text Files (*.txt)")
#         file_path = file_dialog[0]
#         if file_path:
#             with open(file_path, "r") as file:
#                 text_file = file.read()
#                 self.text_edit.setPlainText(text_file)
#                 QMessageBox.information(self, "Успешно", "Файл успешно заружен")
#
#
#     # Само приложение реализовывается внутри конструктара класса
#     def __init__(self):
#         super().__init__()
#
#         # Переменные для геометрии нашего приложение
#         pos_x = 200
#         pos_y = 200
#         # Размеры приложение
#         wix_x = 400
#         win_y = 300
#
#         self.setWindowTitle("Наше приложение")
#         self.setGeometry(pos_x, pos_y, wix_x, win_y)
#
#         # Создаем переменную для текстового поля
#         self.text_edit = QTextEdit()
#
#         # Создаем переменные для двух кнопок
#         self.save_button = QPushButton("Сохранить заметку")
#         self.export_button = QPushButton("Загрузить заметку")
#
#         # когда нажмем на кнопку соединись с определенной функцией
#         self.save_button.clicked.connect(self.save_note)
#         self.export_button.clicked.connect(self.export_note)
#
#         # Создаем линию вертикальную
#         layout = QVBoxLayout()
#         layout.addWidget(self.text_edit)
#         layout.addWidget(self.save_button)
#         layout.addWidget(self.export_button)
#
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     note = MyNoteApp()
#     note.show()
#     sys.exit(app.exec())

class AppCalculetionError(Exception):
    def __init__(self, message="Возможно вы ошиблись!"):
        self.message = message
        super().__init__(message)



while True:
    print("1. +")
    print("2. -")
    print("3. *")

    try:
        user_menu = input("Введите что-то: ")

        match user_menu:
            case "+":
                user_num_1 = float(input("Введите первое число: "))
                user_num_2 = float(input("Введите второе число: "))
                result = user_num_1 + user_num_2
                print(f"Результат сложение: {user_num_1} + {user_num_2} = {result}")

            case "-":
                user_num_1 = float(input("Введите первое число: "))
                user_num_2 = float(input("Введите второе число: "))
                result = user_num_1 - user_num_2
                print(f"Результат сложение: {user_num_1} - {user_num_2} = {result}")

            case "*":
                user_num_1 = float(input("Введите первое число: "))
                user_num_2 = float(input("Введите второе число: "))
                result = user_num_1 * user_num_2
                print(f"Результат сложение: {user_num_1} * {user_num_2} = {result}")

            case _:
                print("Ошибка")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")

