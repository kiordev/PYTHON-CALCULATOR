# Python Calculator
# Creator: Alexandr Kior kiordev@gmail.com
# Date: April 12 2022

import sys
import PySide6.QtCore
import PySide6.QtGui
from PySide6.QtWidgets import QApplication, QMainWindow


from design import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()
    sys.exit(app.exec())
