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
            res = "Alfalfa (люцерна)"
        if max_index == 1:
            res = "Allium (лук)"
        if max_index == 2:
            res = "Borage (огуречник)"
        if max_index == 3:
            res = "Burdock (лопух)"
        if max_index == 4:
            res = "Calendula (календула)"
        if max_index == 5:
            res = "Cattail (рогоз)"
        if max_index == 6:
            res = "Chickweed (крапива)"
        if max_index == 7:
            res = "Chicory (цикорий)"
        if max_index == 8:
            res = "Chive blossom (цветок зеленого лука)"
        if max_index == 9:
            res = "Coltsfoot (мать-и-мачеха обыкновенная)"
        if max_index == 10:
            res = "Common mallow (мальва лесная)"
        if max_index == 11:
            res = "Common milkweed (ваточник сирийский)"
        if max_index == 12:
            res = "Common vetch (горошек посевной)"
        if max_index == 13:
            res = "Common yarrow (тысячелистник обыкновенный)"
        if max_index == 14:
            res = "Coneflower (эхинацея)"
        if max_index == 15:
            res = "Cow parsley (купырь лесной)"
        if max_index == 16:
            res = "Cowslip (первоцвет весенний)"
        if max_index == 17:
            res = "Crimson clover (клевер пунцовый)"
        if max_index == 18:
            res = "Crithmum maritimum (критмум)"
        if max_index == 19:
            res = "Daisy (нивяник)"
        if max_index == 20:
            res = "Dandelion (одуванчик)"
        if max_index == 21:
            res = "Fennel (фенхель обыкновенный)"
        if max_index == 22:
            res = "Fireweed (иван-чай узколистный)"
        if max_index == 23:
            res = "Gardenia (гардения)"
        if max_index == 24:
            res = "Garlic mustard (чесночница черешчатая)"
        if max_index == 25:
            res = "Geranium (герань)"
        if max_index == 26:
            res = "Ground ivy (будра плющевидная)"
        if max_index == 27:
            res = "Harebell (колокольчик круглолистный)"
        if max_index == 28:
            res = "Henbit (яснотка стеблеобъемлющая)"
        if max_index == 29:
            res = "Knapweed (василёк)"
        if max_index == 30:
            res = "Meadowsweet (таволга вязолистная)"
        if max_index == 31:
            res = "Mullein (коровяк)"
        if max_index == 32:
            res = "Pickerelweed (понтедерия)"
        if max_index == 33:
            res = "Ramsons (черемша)"
        if max_index == 34:
            res = "Red clover (клевер луговой)"
        self.__data_label = self.label = QLabel(
            f"Финальный результат: " + res + "\n" +
            f"Alfalfa (люцерна) - {round(predicted[0] * 100, 2)}%\n" +
            f"Allium (лук)  - {round(predicted[1] * 100, 2)}%\n" +
            f"Borage (огуречник) - {round(predicted[2] * 100, 2)}%\n" +
            f"Burdock (лопух) - {round(predicted[3] * 100, 2)}%\n" +
            f"Calendula (календула) - {round(predicted[4] * 100, 2)}%\n" +
            f"Cattail (рогоз) - {round(predicted[5] * 100, 2)}%\n" +
            f"Chickweed (крапива) - {round(predicted[6] * 100, 2)}%\n" +
            f"Chicory (цикорий) - {round(predicted[7] * 100, 2)}%\n" +
            f"Chive blossom (цветок зеленого лука) - {round(predicted[8] * 100, 2)}%\n" +
            f"Coltsfoot (мать-и-мачеха обыкновенная) - {round(predicted[9] * 100, 2)}%\n" +
            f"Common mallow (мальва лесная) - {round(predicted[10] * 100, 2)}%\n" +
            f"Common milkweed (ваточник сирийский) - {round(predicted[11] * 100, 2)}%\n" +
            f"Common vetch (горошек посевной) - {round(predicted[12] * 100, 2)}%\n" +
            f"Common yarrow (тысячелистник обыкновенный) - {round(predicted[13] * 100, 2)}%\n" +
            f"Coneflower (эхинацея) - {round(predicted[14] * 100, 2)}%\n" +
            f"Cow parsley (купырь лесной) - {round(predicted[15] * 100, 2)}%\n" +
            f"Cowslip (первоцвет весенний) - {round(predicted[16] * 100, 2)}%\n" +
            f"Crimson clover (клевер пунцовый) - {round(predicted[17] * 100, 2)}%\n" +
            f"Crithmum maritimum (критмум) - {round(predicted[18] * 100, 2)}%\n" +
            f"Daisy (нивяник) - {round(predicted[19] * 100, 2)}%\n" +
            f"Dandelion (одуванчик) - {round(predicted[20] * 100, 2)}%\n" +
            f"Fennel (фенхель обыкновенный) - {round(predicted[21] * 100, 2)}%\n" +
            f"Fireweed (иван-чай узколистный) - {round(predicted[22] * 100, 2)}%\n" +
            f"Gardenia (гардения) - {round(predicted[23] * 100, 2)}%\n" +
            f"Garlic mustard (чесночница черешчатая) - {round(predicted[24] * 100, 2)}%\n" +
            f"Geranium (герань) - {round(predicted[25] * 100, 2)}%\n" +
            f"Ground ivy (будра плющевидная) - {round(predicted[26] * 100, 2)}%\n" +
            f"Harebell (колокольчик круглолистный) - {round(predicted[27] * 100, 2)}%\n" +
            f"Henbit (яснотка стеблеобъемлющая) - {round(predicted[28] * 100, 2)}%\n" +
            f"Knapweed (василёк) - {round(predicted[29] * 100, 2)}%\n" +
            f"Meadowsweet (таволга вязолистная) - {round(predicted[30] * 100, 2)}%\n" +
            f"Mullein (коровяк) - {round(predicted[31] * 100, 2)}%\n" +
            f"Pickerelweed (понтедерия) - {round(predicted[32] * 100, 2)}%\n" +
            f"Ramsons (черемша) - {round(predicted[33] * 100, 2)}%\n" +
            f"Red clover (клевер луговой) - {round(predicted[34] * 100, 2)}%\n"
        )
        self.__data_label.setFixedSize(400, 700)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    ex = ResultWindow()
    ex.load_image('C:\\nonsystemic\\downloads\\datasets\\watches\\from web\\rado.jpg')
    ex.show()

    sys.exit(app.exec_())
