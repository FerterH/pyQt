import time
from PyQt5 import QtCore, QtGui, QtWidgets
# str(a = '0')
# str(b = '0')

class Ui_Dialog(object):



    def setupUi(self, Dialog):
        self.percent = 0
        self.flag = 0
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
        self.progressBar.setProperty("value", self.percent)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def plus(self):
        self.flag = 1
        # print(int(self.a) + int(self.b))
    def minus(self):
        self.flag = 2
        # print(self.a-self.b)
    def umn(self):
        self.flag = 3
        # print(self.a*self.b)
    def delit(self):
        self.flag = 4
        # print(self.a/self.b)
    def ch1(self):
        if self.flag == 0:
            self.a = str(self.a) + '1'
        else:
            self.b = str(self.b) + '1'
    def ch2(self):
        if self.flag == 0:
            self.a = str(self.a) + '2'
        else:
            self.b = str(self.b) + '2'
    def ch3(self):
        if self.flag == 0:
            self.a = str(self.a) + '3'
        else:
            self.b = str(self.b) + '3'
    def ch4(self):
        if self.flag == 0:
            self.a = str(self.a) + '4'
        else:
            self.b = str(self.b) + '4'
    def ch5(self):
        if self.flag == 0:
            self.a = str(self.a) + '5'
        else:
            self.b = str(self.b) + '5'
    def ch6(self):
        if self.flag == 0:
            self.a = str(self.a) + '6'
        else:
            self.b = str(self.b) + '6'
    def ch7(self):
        if self.flag == 0:
            self.a = str(self.a) + '7'
        else:
            self.b = str(self.b) + '7'
    def ch8(self):
        if self.flag == 0:
            self.a = str(self.a) + '8'
        else:
            self.b = str(self.b) + '8'
    def ch9(self):
        if self.flag == 0:
            self.a = str(self.a) + '9'
        else:
            self.b = str(self.b) + '9'


    def prnt(self):
        print('a',self.a)
        print('b',self.b)
        print('flag', self.flag)
        for i in range(0, 51):
            self.progressBar.setProperty("value", self.percent)
            self.percent = self.percent +2
            time.sleep(0.01)
        if self.flag == 1:
             self.res = int(self.a) + int(self.b)
             print('Ответ:', int(self.a) + int(self.b))
             self.lcdNumber.setProperty("intValue", self.res)

        elif self.flag == 2:
             self.res = int(self.a) - int(self.b)
             print('Ответ:', int(self.a) - int(self.b))
             self.lcdNumber.setProperty("intValue", self.res)

        elif self.flag == 3:
             self.res = int(self.a) * int(self.b)
             print('Ответ:', int(self.a) * int(self.b))
             self.lcdNumber.setProperty("intValue", self.res)

        elif self.flag == 4:
             self.res = int(self.a) / int(self.b)
             print('Ответ:', int(self.a) / int(self.b))
             self.lcdNumber.setProperty("intValue", self.res)

    def a2(self):
        self.a = str(self.a) + '2'
    def b2(self):
        self.b = str(self.b) + '2'
    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "1"))
        self.pushButton.clicked.connect(self.ch1)

        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_2.clicked.connect(self.ch2)

        self.pushButton_3.setText(_translate("Dialog", "="))
        self.pushButton_3.clicked.connect(self.prnt)
        self.pushButton_4.setText(_translate("Dialog", "+"))
        self.pushButton_4.clicked.connect(self.plus)
        self.pushButton_5.setText(_translate("Dialog", "3"))
        self.pushButton_5.clicked.connect(self.ch3)

        self.pushButton_6.setText(_translate("Dialog", "4"))
        self.pushButton_6.clicked.connect(self.ch4)

        self.pushButton_7.setText(_translate("Dialog", "5"))
        self.pushButton_7.clicked.connect(self.ch5)

        self.pushButton_8.setText(_translate("Dialog", "6"))
        self.pushButton_8.clicked.connect(self.ch6)

        self.pushButton_9.setText(_translate("Dialog", "7"))
        self.pushButton_9.clicked.connect(self.ch7)

        self.pushButton_10.setText(_translate("Dialog", "8"))
        self.pushButton_10.clicked.connect(self.ch8)

        self.pushButton_11.setText(_translate("Dialog", "9"))
        self.pushButton_11.clicked.connect(self.ch9)

        self.pushButton_12.setText(_translate("Dialog", "0"))
        self.pushButton_12.clicked.connect(self.ch2)

        self.pushButton_13.setText(_translate("Dialog", "-"))
        self.pushButton_13.clicked.connect(self.minus)
        self.pushButton_14.setText(_translate("Dialog", "*"))
        self.pushButton_14.clicked.connect(self.umn)
        self.pushButton_15.setText(_translate("Dialog", "/"))
        self.pushButton_15.clicked.connect(self.delit)


        # if self.flag == 0:
        #     self.pushButton.clicked.connect(self.a1)
        #     self.pushButton_2.clicked.connect(self.a2)
        #
        #     # self.pushButton_5.clicked.connect(self.b3)
        #     # self.pushButton_6.clicked.connect(self.b4)
        #     # self.pushButton_7.clicked.connect(self.b5)
        #     # self.pushButton_8.clicked.connect(self.b6)
        #     # self.pushButton_9.clicked.connect(self.b7)
        #     # self.pushButton_10.clicked.connect(self.b8)
        #     # self.pushButton_11.clicked.connect(self.b9)
        # else:
        #     self.pushButton.clicked.connect(self.b1)
        #     self.pushButton_2.clicked.connect(self.b2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
