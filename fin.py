from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os
class Ui_Dialog(object):
    def pyGame(self):
        os.system('pygame.bat')
    def cv2(self):
        os.system('cv2.bat')
    def kalk(self):
        os.system('kalk.bat')
    def djando(self):
        os.system('Django.bat')
    def runBarPQ(self):
        for i in range(0,98):
            self.percent += 2
            time.sleep(0.015)
            self.progressBar_2.setProperty("value", self.percent)
    def runBarCV(self):
        for i in range(0,98):
            self.percent += 2
            time.sleep(0.015)
            self.progressBar_4.setProperty("value", self.percent)
    def runBarDJ(self):
        for i in range(0,98):
            self.percent += 2
            time.sleep(0.015)
            self.progressBar_3.setProperty("value", self.percent)
    def runBarPG(self):
        for i in range(0,98):
            self.percent += 2
            time.sleep(0.015)
            self.progressBar.setProperty("value", self.percent)
    def setupUi(self, Dialog):
        self.percent = 0
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 600)
        Dialog.setStyleSheet("background-color: rgb(79, 200, 255);")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 180, 181, 16))
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(370, 310, 181, 16))
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 100, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 350, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgb(28, 255, 255);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.runBarDJ)
        self.pushButton_1.clicked.connect(self.djando)


        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 90, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(28, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 480, 311, 71))
        self.pushButton_2.clicked.connect(self.runBarPG)
        self.pushButton_2.clicked.connect(self.pyGame)



        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_6")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(40, 440, 181, 16))
        self.progressBar_3.setObjectName("progressBar_3")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 220, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(28, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.runBarPQ)
        self.pushButton_3.clicked.connect(self.kalk)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 480, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(28, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.runBarCV)
        self.pushButton_4.clicked.connect(self.cv2)

        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(370, 570, 181, 16))
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 370, 320, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 390, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "PyGame - это билиотека для создания игр."))
        self.label_3.setText(_translate("Dialog", "PyQT - библиотека для работы с GUI."))
        self.pushButton_3.setText(_translate("Dialog", "PyQT"))
        self.pushButton_1.setText(_translate("Dialog", "Django"))
        self.label_5.setText(_translate("Dialog", "CV2 - библиотека для работы с фото/видео"))
        self.label.setText(_translate("Dialog", "Мои творения"))
        self.pushButton_2.setText(_translate("Dialog", "PyGame"))
        self.pushButton_4.setText(_translate("Dialog", "CV2 и другие"))
        self.label_4.setText(_translate("Dialog", "Django является одной из лучших библиотек"))
        self.label_6.setText(_translate("Dialog", " для создания сайтов. "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
