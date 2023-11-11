from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPixmap


class ResultWindow(QMainWindow):
    def __init__(self, filename, predicted=None):
        super().__init__()

        self.setWindowTitle('Определение')
        self.setFixedHeight(1000)
        self.setFixedWidth(400)
        self.__load_data(filename, predicted)
        self.__construct_view()

    def __construct_view(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.__data_label)
        main_layout.setContentsMargins(0,350,0,0)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def __load_data(self, filename, predicted):
        self.__load_image(filename)
        self.__load_results(predicted)

    def __load_image(self, filename):
        pixmap = QPixmap(filename)
        pixmap = pixmap.scaled(400, 400)

        self.label = QLabel(self)
        self.label.setFixedSize(400, 400)
        self.label.setPixmap(pixmap)

    def __load_results(self, predicted):
        res = ""
        max_value = round(predicted[0] * 100, 2)
        max_index = 0
        for i in range(len(predicted)):
            if round(predicted[i] * 100, 2) > max_value:
                max_index = i; max_value = round(predicted[i] * 100, 2)

        if max_index == 0:
            res = "Guns"
        if max_index == 1:
            res = "NoGuns"
       
        self.__data_label = self.label = QLabel(
            f"Финальный результат: " + res + "\n" +
            f"Guns - {round(predicted[0] * 100, 2)}%\n" +
            f"NoGuns  - {round(predicted[1] * 100, 2)}%\n"
        )
        self.__data_label.setFixedSize(400, 700)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    ex = ResultWindow()
    ex.load_image('C:\\nonsystemic\\downloads\\datasets\\watches\\from web\\rado.jpg')
    ex.show()

    sys.exit(app.exec_())
