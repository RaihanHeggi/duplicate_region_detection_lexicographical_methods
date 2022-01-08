from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog


ID_DIALOG = "dialog"
ID_FIELD_FILE_NAME_1 = "filename1"
ID_BTN_BROWSE_1 = "browse1"
ID_BTN_SUBMIT = "submit_button"

TEXT_WINDOW_TITLE = "Duplicated Image Regions"
TEXT_BTN_BROWSE_1 = "Browse"
TEXT_BTN_SUBMIT = "Submit Data"

IMAGE_FILE_TYPE_JPG = "Image file(*.jpg)"
IMAGE_FILE_TYPE_PNG = "Image file(*.png)"

class Window(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(ID_DIALOG)
        Dialog.resize(1007, 652)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # Init UI
        self.filename1 = QtWidgets.QLineEdit(Dialog)
        self.browse1 = QtWidgets.QPushButton(Dialog)
        self.submit_button = QtWidgets.QPushButton(Dialog)

        # Set ID For UI Element
        self.filename1.setObjectName(ID_FIELD_FILE_NAME_1)
        self.browse1.setObjectName(ID_BTN_BROWSE_1)
        self.submit_button.setObjectName(ID_BTN_SUBMIT)

        # Set Size For UI Element
        # QRect (w,x,y,z)
        # w = left position
        # x = top position
        # y = width
        # z = height
        self.filename1.setGeometry(QtCore.QRect(180, 20, 511, 28))
        self.browse1.setGeometry(QtCore.QRect(20, 20, 150, 28))
        self.submit_button.setGeometry(QtCore.QRect(20, 50, 150, 28))

        # Set Function To Do For UI Element
        self.browse1.clicked.connect(self.on_click_select_1)
        self.submit_button.clicked.connect(self.on_click_process)

        _translate = QtCore.QCoreApplication.translate

        # Set Text For UI Element
        Dialog.setWindowTitle(_translate(ID_DIALOG, TEXT_WINDOW_TITLE))
        self.browse1.setText(_translate(ID_DIALOG, TEXT_BTN_BROWSE_1))
        self.submit_button.setText(_translate(ID_DIALOG, TEXT_BTN_SUBMIT))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def on_click_select_1(self):
        # Get Image Path
        image1 = QFileDialog.getOpenFileName(None, 'OpenFile', '', IMAGE_FILE_TYPE_JPG)
        self.filename1.setText(image1[0])

    def on_click_process(self):
        # TODO For Processing Image
        # get path from filename1 -> self.filename1.text()
        # get path from filename1 -> self.filename2.text()
        self.filename1.setText()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Window()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
