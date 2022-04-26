
from PyQt5 import QtCore, QtGui, QtWidgets
# str(a = '0')
# str(b = '0')

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        self.a = ''
        self.b = ''
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 559)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 50, 50))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 270, 50, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 470, 91, 81))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 260, 50, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 270, 50, 50))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 340, 50, 50))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 340, 50, 50))
        self.pushButton_7.setObjectName("pushButton_7")

        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 30, 251, 111))
        self.lcdNumber.setObjectName("lcdNumber")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 340, 50, 50))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(40, 410, 50, 50))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(130, 410, 50, 50))
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 410, 50, 50))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 470, 50, 50))
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(330, 310, 50, 50))
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(330, 360, 50, 50))
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(330, 410, 50, 50))
        self.pushButton_15.setObjectName("pushButton_15")

        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 170, 411, 71))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pl = False
        self.mi = False
    def plus(self):
        print(self.a + self.b)
        self.pl = True
    def minus(self):
        print(self.a-self.b)
        self.mi = True
    def umn(self):
        print(self.a*self.b)
    def delit(self):
        print(self.a/self.b)

    def a1(self):
        self.a = str(self.a) + '1'
        print(self.a)
    def b1(self):
        self.b = str(self.b) + '1'
        print('b',self.b)
    def a2(self):
        self.a = str(self.a) + '2'
    def b2(self):
        self.b = str(self.b) + '2'
    def retranslateUi(self, Dialog):
        self.pl = False
        self.mi = False
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "1"))
        if self.pl or self.mi:
            self.pushButton.clicked.connect(self.b1)
        else:
            self.pushButton.clicked.connect(self.a1)
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_2.clicked.connect
        self.pushButton_3.setText(_translate("Dialog", "="))
        self.pushButton_3.clicked.connect
        self.pushButton_4.setText(_translate("Dialog", "+"))
        self.pushButton_4.clicked.connect(self.plus)
        self.pushButton_5.setText(_translate("Dialog", "3"))
        self.pushButton_5.clicked.connect
        self.pushButton_6.setText(_translate("Dialog", "4"))
        self.pushButton_6.clicked.connect
        self.pushButton_7.setText(_translate("Dialog", "5"))
        self.pushButton_7.clicked.connect
        self.pushButton_8.setText(_translate("Dialog", "6"))
        self.pushButton_8.clicked.connect
        self.pushButton_9.setText(_translate("Dialog", "7"))
        self.pushButton_9.clicked.connect
        self.pushButton_10.setText(_translate("Dialog", "8"))
        self.pushButton_10.clicked.connect
        self.pushButton_11.setText(_translate("Dialog", "9"))
        self.pushButton_11.clicked.connect
        self.pushButton_12.setText(_translate("Dialog", "0"))
        self.pushButton_12.clicked.connect
        self.pushButton_13.setText(_translate("Dialog", "-"))
        self.pushButton_13.clicked.connect
        self.pushButton_14.setText(_translate("Dialog", "*"))
        self.pushButton_14.clicked.connect
        self.pushButton_15.setText(_translate("Dialog", "/"))
        self.pushButton_15.clicked.connect

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
