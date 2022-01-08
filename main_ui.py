from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

from detect import detect

ID_DIALOG = "dialog"
ID_FIELD_FILE_NAME = "filename1"
ID_BTN_BROWSE = "browse1"
ID_BTN_SUBMIT = "submit_button"

TEXT_WINDOW_TITLE = "Duplicated Image Regions"
TEXT_BTN_BROWSE = "Browse"
TEXT_BTN_SUBMIT = "Submit Data"

IMAGE_FILE_TYPE_JPG = "Image file(*.jpg)"
IMAGE_FILE_TYPE_PNG = "Image file(*.png)"


class Window(object):
    def setupUi(self, dialog):
        dialog.setObjectName(ID_DIALOG)
        dialog.resize(1007, 652)
        dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # Init UI
        self.filename = QtWidgets.QLineEdit(dialog)
        self.browse = QtWidgets.QPushButton(dialog)
        self.submit_button = QtWidgets.QPushButton(dialog)
        self.image_view_1 = QtWidgets.QLabel(dialog)
        self.image_view_2 = QtWidgets.QLabel(dialog)

        # Set ID For UI Element
        self.filename.setObjectName(ID_FIELD_FILE_NAME)
        self.browse.setObjectName(ID_BTN_BROWSE)
        self.submit_button.setObjectName(ID_BTN_SUBMIT)

        # Set Size For UI Element
        # QRect (x,y,a,b)
        # x = x absis position
        # y = y absis position
        # a = width
        # b = height
        self.filename.setGeometry(QtCore.QRect(180, 20, 511, 28))
        self.browse.setGeometry(QtCore.QRect(20, 20, 150, 28))
        self.submit_button.setGeometry(QtCore.QRect(20, 50, 150, 28))
        self.image_view_1.setGeometry(QtCore.QRect(20, 100, 500, 300))
        self.image_view_2.setGeometry(QtCore.QRect(550, 100, 500, 300))

        # Set Function To Do For UI Element
        self.browse.clicked.connect(self.on_click_select)
        self.submit_button.clicked.connect(self.on_click_process)

        _translate = QtCore.QCoreApplication.translate

        # Set Text For UI Element
        dialog.setWindowTitle(_translate(ID_DIALOG, TEXT_WINDOW_TITLE))
        self.browse.setText(_translate(ID_DIALOG, TEXT_BTN_BROWSE))
        self.submit_button.setText(_translate(ID_DIALOG, TEXT_BTN_SUBMIT))

        QtCore.QMetaObject.connectSlotsByName(dialog)

    def on_click_select(self):
        # Get Image Path
        image1 = QFileDialog.getOpenFileName(None, 'OpenFile', '', IMAGE_FILE_TYPE_JPG)
        self.filename.setText(image1[0])

    def create_image1(self, image_path):
        self.pixmap = QPixmap(image_path)
        self.image_view_1.setPixmap(self.pixmap)

    def create_image2(self, image_path):
        self.pixmap = QPixmap(image_path)
        self.image_view_2.setPixmap(self.pixmap)

    # ------------------------------------------------------------------------------------------------------------------

    def on_click_process(self):
        # TODO For Processing Image
        image_path = self.filename.text()  # Image Path dari Selected Browse Image
        print(image_path)
        detect_model = detect(image_path, 32)
        detect_model.show_image()
        detect_model.show_metadata()

        detect_model.compute_block()
        detect_model.lexicographic_sort()
        detect_model.analyze()
        self.create_image1(image_path)  # Ini Buat Nampilin Gambar Pertama
        self.create_image2(image_path)  # Ini Buat Nampilin Gambar Kedua


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Window()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
