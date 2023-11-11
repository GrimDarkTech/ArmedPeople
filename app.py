from PyQt5.QtWidgets import (QTreeView, QFileSystemModel, QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QListWidget)
from PyQt5.QtCore import QDir

from tensorflow import keras
import numpy as np

from img_widge_test import ResultWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__ml_model = keras.models.load_model("model_1")
        self.__data_side = 150
        self.__data_shape = (self.__data_side, self.__data_side, 3)

        self.setWindowTitle('Drag & Drop')
        self.setGeometry(500, 100, 800, 800)

        self.setAcceptDrops(True)

        self.list_files = QListWidget()
        self.label_total_files = QLabel()

        self.list_files.itemActivated.connect(self.itemActivatedEvent)

        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        model.setReadOnly(False)

        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(QDir.currentPath()))
        self.tree.setSelectionMode(QTreeView.SingleSelection)
        self.tree.setDragDropMode(QTreeView.InternalMove)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tree)
        main_layout.addWidget(QLabel('Перетащите файл:'))
        main_layout.addWidget(self.list_files)
        main_layout.addWidget(self.label_total_files)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        self._update_states()

    def _update_states(self):
        self.label_total_files.setText('Files: {}'.format(self.list_files.count()))

    def dragEnterEvent(self, event):
        mime = event.mimeData()

        if mime.hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Обработка события Drop

        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            self.list_files.addItem(file_name)

        self._update_states()

        return super().dropEvent(event)

    def itemActivatedEvent(self, item):
        path = item.text().replace('/', '\\')
        print(path)

        predicted = self.predict(path)
        print(predicted)
        self.res_window = ResultWindow(path, predicted)
        self.res_window.show()

    def predict(self, path):
        image = keras.preprocessing.image.load_img(path, target_size=self.__data_shape)
        input_img = keras.preprocessing.image.img_to_array(image)
        input_array = np.array(input_img)
        input_array = input_array / 255
        return self.__ml_model.predict(input_array.reshape(-1, self.__data_side, self.__data_side, 3))[0]


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
