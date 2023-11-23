import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.exemple)
    def exemple(self):
        a = string.ascii_letters if self.ui.cb_alphabete.isChecked() else ""
        b = string.digits if self.ui.cb_number.isChecked() else ""
        c = a+b+string.punctuation
        password = "".join(random.choice(c) for i in range(16))
        self.ui.result.setText(password)
        print (1)
        
        
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
