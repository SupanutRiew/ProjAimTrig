import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

class Firstpage(QDialog):
    def __init__(self):
        super(Firstpage, self).__init__()
        loadUi("Firstpage.ui",self)
        self.gotologinpage.clicked.connect(self.login)
        self.setup.clicked.connect(self.setupchyt)
    #go to login page
    def login(self):
        login = Loginpage()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def setupchyt(self):
        setup = setuppage()
        widget.addWidget(setup)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Loginpage(QDialog):
    def __init__(self):
        super(Loginpage, self).__init__()
        loadUi("Loginpage.ui",self)
        self.gobackfromlogin.clicked.connect(self.goback)
        self.loginbutton.clicked.connect(self.loginfunc)
    #back to first page
    def goback(self):
        back = Firstpage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def loginfunc(self):
        proid = self.productid.text()
        password = self.password.text()
        if proid == "" or password == "":
            self.errormessage.setText("All fields are required")

class setuppage(QDialog):
    def __init__(self):
        super(setuppage, self).__init__()
        loadUi("setuppage.ui",self)
        self.gobackfromsetup.clicked.connect(self.goback)
    def goback(self):
        back = Firstpage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
first = Firstpage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(first)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_())
