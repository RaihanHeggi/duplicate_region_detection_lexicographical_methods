from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog


ID_DIALOG = "dialog"
ID_FIELD_FILE_NAME_1 = "filename1"
ID_FIELD_FILE_NAME_2 = "filename2"
ID_BTN_BROWSE_1 = "browse1"
ID_BTN_BROWSE_2 = "browse2"
ID_BTN_SUBMIT = "submit_button"

TEXT_WINDOW_TITLE = "Duplicated Image Regions"
TEXT_BTN_BROWSE_1 = "Browse File Original"
TEXT_BTN_BROWSE_2 = "Browse File Fake"
TEXT_BTN_SUBMIT = "Submit Data"

IMAGE_FILE_TYPE_JPG = "Image file(*.jpg)"
IMAGE_FILE_TYPE_PNG = "Image file(*.PNG)"

class Window(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(ID_DIALOG)
        Dialog.resize(1007, 652)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # Init UI
        self.filename1 = QtWidgets.QLineEdit(Dialog)
        self.filename2 = QtWidgets.QLineEdit(Dialog)
        self.browse1 = QtWidgets.QPushButton(Dialog)
        self.browse2 = QtWidgets.QPushButton(Dialog)
        self.submit_button = QtWidgets.QPushButton(Dialog)

        # Set ID For UI Element
        self.filename1.setObjectName(ID_FIELD_FILE_NAME_1)
        self.filename2.setObjectName(ID_FIELD_FILE_NAME_2)
        self.browse1.setObjectName(ID_BTN_BROWSE_1)
        self.browse2.setObjectName(ID_BTN_BROWSE_2)
        self.submit_button.setObjectName(ID_BTN_SUBMIT)

        # Set Size For UI Element
        self.filename1.setGeometry(QtCore.QRect(20, 130, 511, 22))
        self.filename2.setGeometry(QtCore.QRect(20, 170, 511, 21))
        self.browse1.setGeometry(QtCore.QRect(550, 130, 150, 28))
        self.browse2.setGeometry(QtCore.QRect(550, 170, 150, 28))
        self.submit_button.setGeometry(QtCore.QRect(30, 230, 181, 41))

        # Set Function To Do For UI Element
        self.browse1.clicked.connect(self.on_click_select_1)
        self.browse2.clicked.connect(self.on_click_select_2)
        self.submit_button.clicked.connect(self.on_click_process)

        _translate = QtCore.QCoreApplication.translate

        # Set Text For UI Element
        Dialog.setWindowTitle(_translate(ID_DIALOG, TEXT_WINDOW_TITLE))
        self.browse1.setText(_translate(ID_DIALOG, TEXT_BTN_BROWSE_1))
        self.browse2.setText(_translate(ID_DIALOG, TEXT_BTN_BROWSE_2))
        self.submit_button.setText(_translate(ID_DIALOG, TEXT_BTN_SUBMIT))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def on_click_select_1(self):
        # Get Image Path
        image1 = QFileDialog.getOpenFileName(None, 'OpenFile', '', IMAGE_FILE_TYPE_JPG)
        self.filename1.setText(image1[0])

    def on_click_select_2(self):
        # Get Image Path
        image2 = QFileDialog.getOpenFileName(None, 'OpenFile', '', IMAGE_FILE_TYPE_JPG)
        self.filename2.setText(image2[0])

    def on_click_process(self):
        # TODO For Processing Image
        # get path from filename1 -> self.filename1.text()
        # get path from filename1 -> self.filename2.text()
        self.filename1.setText()
        self.filename2.setText()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Window()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
