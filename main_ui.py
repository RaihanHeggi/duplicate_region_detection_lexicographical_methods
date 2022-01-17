from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

from detect import detect, create_dir, DIRECTORY_OUTPUT, get_uri_image, TIME_STAMP

ID_DIALOG = "dialog"
ID_FIELD_FILE_NAME = "filename"
ID_BTN_BROWSE = "browse"
ID_BTN_SUBMIT = "submit_button"
ID_BTN_SHOW_RESULT = "show_result"

TEXT_NAMA_KELOMPOK = "Kelompok 3"
TEXT_NAMA_HEGGI = "- 1301184219 - Sya Raihan Heggi"
TEXT_NAMA_ADABI = "- 1301180379 - Adabi Raihan Muhammad"
TEXT_NAMA_AMIR = "- 1301198497 - Muhammad Faisal Amir"
TEXT_NAMA_IRFAN = "- 1301174524 - Muhammad Irfan Aldi"
TEXT_NAMA_GIA = "- 1301184005 - Gia Nusantara"

TEXT_DESC_ORIGINAL = "Original Image (Pre Processing)"
TEXT_DESC_GROUND_TRUTH = "Ground Truth Image (After Processing)"
TEXT_DESC_OUTPUT = "Output Image (After Processing)"

TEXT_WINDOW_TITLE = "Duplicated Image Regions"
TEXT_BTN_BROWSE = "Browse"
TEXT_BTN_SUBMIT = "Submit Data"
TEXT_BTN_SHOW_RESULT = "Show Result"

IMAGE_FILE_TYPE_FILTER = "Image file(*.png *.jpg *.jpeg)"


class Window(object):
    def setupUi(self, dialog):
        dialog.setObjectName(ID_DIALOG)
        dialog.resize(1024, 652)
        dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # Init UI
        self.filename = QtWidgets.QLineEdit(dialog)
        self.browse = QtWidgets.QPushButton(dialog)
        self.submit_button = QtWidgets.QPushButton(dialog)
        self.show_result_button = QtWidgets.QPushButton(dialog)

        self.txt_nama_kelompok = QtWidgets.QLabel(dialog)
        self.txt_nama_heggi = QtWidgets.QLabel(dialog)
        self.txt_nama_adabi = QtWidgets.QLabel(dialog)
        self.txt_nama_amir = QtWidgets.QLabel(dialog)
        self.txt_nama_irfan = QtWidgets.QLabel(dialog)
        self.txt_nama_gia = QtWidgets.QLabel(dialog)

        self.txt_desc_original = QtWidgets.QLabel(dialog)
        self.txt_desc_ground_truth = QtWidgets.QLabel(dialog)
        self.txt_desc_output = QtWidgets.QLabel(dialog)

        self.image_view_0 = QtWidgets.QLabel(dialog)
        self.image_view_1 = QtWidgets.QLabel(dialog)
        self.image_view_2 = QtWidgets.QLabel(dialog)

        # Set ID For UI Element
        self.filename.setObjectName(ID_FIELD_FILE_NAME)
        self.browse.setObjectName(ID_BTN_BROWSE)
        self.submit_button.setObjectName(ID_BTN_SUBMIT)
        self.show_result_button.setObjectName(ID_BTN_SHOW_RESULT)

        # Set Size For UI Element
        # QRect (x,y,a,b)
        # x = x absis position
        # y = y absis position
        # a = width
        # b = height
        self.filename.setGeometry(QtCore.QRect(180, 20, 511, 28))
        self.browse.setGeometry(QtCore.QRect(20, 20, 150, 28))
        self.submit_button.setGeometry(QtCore.QRect(20, 50, 150, 28))

        self.show_result_button.setGeometry(QtCore.QRect(170, 50, 150, 28))

        self.txt_nama_kelompok.setGeometry(QtCore.QRect(560, 100, 150, 28))
        self.txt_nama_heggi.setGeometry(QtCore.QRect(560, 120, 500, 28))
        self.txt_nama_adabi.setGeometry(QtCore.QRect(560, 140, 500, 28))
        self.txt_nama_amir.setGeometry(QtCore.QRect(560, 160, 500, 28))
        self.txt_nama_irfan.setGeometry(QtCore.QRect(560, 180, 500, 28))
        self.txt_nama_gia.setGeometry(QtCore.QRect(560, 200, 500, 28))

        self.txt_desc_original.setGeometry(QtCore.QRect(30, 100, 500, 28))
        self.image_view_0.setGeometry(QtCore.QRect(20, 135, 500, 300))

        self.txt_desc_ground_truth.setGeometry(QtCore.QRect(30, 455, 500, 28))
        self.image_view_1.setGeometry(QtCore.QRect(20, 485, 500, 300))

        self.txt_desc_output.setGeometry(QtCore.QRect(550, 455, 500, 28))
        self.image_view_2.setGeometry(QtCore.QRect(550, 485, 500, 300))

        # Set Function To Do For UI Element
        self.browse.clicked.connect(self.on_click_select)
        self.submit_button.clicked.connect(self.on_click_process)
        self.show_result_button.clicked.connect(self.show_result_image)

        _translate = QtCore.QCoreApplication.translate

        # Set Text For UI Element
        dialog.setWindowTitle(_translate(ID_DIALOG, TEXT_WINDOW_TITLE))
        self.browse.setText(_translate(ID_DIALOG, TEXT_BTN_BROWSE))
        self.submit_button.setText(_translate(ID_DIALOG, TEXT_BTN_SUBMIT))
        self.show_result_button.setText(_translate(ID_DIALOG, TEXT_BTN_SHOW_RESULT))

        self.txt_desc_original.setText(TEXT_DESC_ORIGINAL)
        self.txt_desc_ground_truth.setText(TEXT_DESC_GROUND_TRUTH)
        self.txt_desc_output.setText(TEXT_DESC_OUTPUT)

        QtCore.QMetaObject.connectSlotsByName(dialog)

    def on_click_select(self):
        # Get Image Path
        image_pre_process = QFileDialog.getOpenFileName(None, 'OpenFile', '', IMAGE_FILE_TYPE_FILTER)
        self.filename.setText(image_pre_process[0])
        self.create_image0(self.filename.text())
        self.txt_nama_kelompok.setText(TEXT_NAMA_KELOMPOK)
        self.txt_nama_heggi.setText(TEXT_NAMA_HEGGI)
        self.txt_nama_adabi.setText(TEXT_NAMA_ADABI)
        self.txt_nama_amir.setText(TEXT_NAMA_AMIR)
        self.txt_nama_irfan.setText(TEXT_NAMA_IRFAN)
        self.txt_nama_gia.setText(TEXT_NAMA_GIA)

    def create_image0(self, image_path):
        self.pixmap0 = QPixmap(image_path)
        self.image_view_0.setPixmap(self.pixmap0)

    def create_image1(self, image_path):
        self.pixmap1 = QPixmap(image_path)
        self.image_view_1.setPixmap(self.pixmap1)

    def create_image2(self, image_path):
        self.pixmap2 = QPixmap(image_path)
        self.image_view_2.setPixmap(self.pixmap2)

    def show_result_image(self):
        image_path_uri = self.filename.text()  # Image Path dari Selected Browse Image

        image_path_uri_arr = image_path_uri.split("/")
        image_path_name = image_path_uri_arr[-1]

        output_image_path_uri_1 = get_uri_image("output_" + TIME_STAMP + "_" + image_path_name)
        output_image_path_uri_2 = get_uri_image("output_" + TIME_STAMP + "_lined_" + image_path_name)

        print(output_image_path_uri_1)
        print(output_image_path_uri_2)

        self.create_image1(output_image_path_uri_1)  # Ini Buat Nampilin Gambar Pertama
        self.create_image2(output_image_path_uri_2)  # Ini Buat Nampilin Gambar Kedua

    # ------------------------------------------------------------------------------------------------------------------

    def on_click_process(self):
        # TODO For Processing Image

        # Directory
        create_dir(DIRECTORY_OUTPUT)

        image_path_uri = self.filename.text()  # Image Path dari Selected Browse Image

        image_path_uri_arr = image_path_uri.split("/")
        image_path_name = image_path_uri_arr[-1]

        print("Get Image Uri : " + image_path_uri)

        detect_model = detect(image_path_uri, 32)
        detect_model.show_image()
        detect_model.show_metadata()

        detect_model.compute_block()
        detect_model.lexicographic_sort()
        detect_model.analyze()
        result_path = detect_model.reconstruct()

        output_image_path_uri_1 = get_uri_image("output_" + TIME_STAMP + "_" + image_path_name)
        output_image_path_uri_2 = get_uri_image("output_" + TIME_STAMP + "_lined_" + image_path_name)

        print(output_image_path_uri_1)
        print(output_image_path_uri_2)

        self.create_image1(output_image_path_uri_1)  # Ini Buat Nampilin Gambar Pertama
        self.create_image2(output_image_path_uri_2)  # Ini Buat Nampilin Gambar Kedua


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Window()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
