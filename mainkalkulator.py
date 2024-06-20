import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from kalkulator import Ui_Form  # Mengimport class Ui_Form dari file kalkulator.py

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Kalkulator")

        # Menghubungkan tombol-tombol dengan fungsi-fungsinya
        self.ui.pushButton.clicked.connect(self.clear_lcd)
        self.ui.pushButton_2.clicked.connect(lambda: self.add_to_lcd("7"))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_to_lcd("4"))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_to_lcd("0"))
        self.ui.pushButton_5.clicked.connect(lambda: self.add_to_lcd("1"))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_to_lcd("M"))
        self.ui.pushButton_7.clicked.connect(lambda: self.add_to_lcd("8"))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_to_lcd("5"))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_to_lcd("2"))
        self.ui.pushButton_10.clicked.connect(lambda: self.add_to_lcd("%"))
        self.ui.pushButton_11.clicked.connect(lambda: self.add_to_lcd("MR"))
        self.ui.pushButton_12.clicked.connect(lambda: self.add_to_lcd("9"))
        self.ui.pushButton_13.clicked.connect(lambda: self.add_to_lcd("6"))
        self.ui.pushButton_14.clicked.connect(lambda: self.add_to_lcd("3"))
        self.ui.pushButton_15.clicked.connect(self.calculate)
        self.ui.pushButton_16.clicked.connect(lambda: self.add_to_lcd(":"))
        self.ui.pushButton_17.clicked.connect(lambda: self.add_to_lcd("X"))
        self.ui.pushButton_18.clicked.connect(lambda: self.add_to_lcd("-"))
        self.ui.pushButton_19.clicked.connect(lambda: self.add_to_lcd("+"))

    def clear_lcd(self):
        self.ui.lcdNumber.display("")

    def add_to_lcd(self, text):
        current_text = self.ui.lcdNumber.intValue()  # Menggunakan intValue() untuk mendapatkan nilai integer
        new_text = str(current_text) + text
        self.ui.lcdNumber.display(new_text)

    def calculate(self):
        # Implement your calculation logic here
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
