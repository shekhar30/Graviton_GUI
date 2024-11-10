# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\shekh\PycharmProjects\Gravity\File_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Resources_1



class Ui_Dialog(object):
    def __init__(self, filename, date2, s, extension):
        self.filename = filename
        self.date2 = str(date2)
        self.extension = extension
        self.s = s


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 400)
        Dialog.setStyleSheet("background-image: url(:/resources/Resource Image/carbon-fiber-pattern1-png.png);")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.X_Lable_6 = QtWidgets.QLabel(Dialog)
        self.X_Lable_6.setGeometry(QtCore.QRect(230, 40, 21, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable_6.setFont(font)
        self.X_Lable_6.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 1px solid white;\n"
"border-radius: 10px;;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable_6.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_6.setObjectName("X_Lable_6")
        self.X_Lable_7 = QtWidgets.QLabel(Dialog)
        self.X_Lable_7.setGeometry(QtCore.QRect(230, 120, 21, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable_7.setFont(font)
        self.X_Lable_7.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 1px solid white;\n"
"border-radius: 10px;;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable_7.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_7.setObjectName("X_Lable_7")
        self.X_Lable_8 = QtWidgets.QLabel(Dialog)
        self.X_Lable_8.setGeometry(QtCore.QRect(230, 200, 21, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable_8.setFont(font)
        self.X_Lable_8.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 1px solid white;\n"
"border-radius: 10px;;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable_8.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_8.setObjectName("X_Lable_8")
        self.X_Lable_9 = QtWidgets.QLabel(Dialog)
        self.X_Lable_9.setGeometry(QtCore.QRect(230, 270, 21, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable_9.setFont(font)
        self.X_Lable_9.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 1px solid white;\n"
"border-radius: 10px;;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable_9.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_9.setObjectName("X_Lable_9")
        self.F_Name = QtWidgets.QLabel(Dialog)
        self.F_Name.setGeometry(QtCore.QRect(270, 40, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F_Name.setFont(font)
        self.F_Name.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.F_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.F_Name.setObjectName("F_Name")
        self.F_Size = QtWidgets.QLabel(Dialog)
        self.F_Size.setGeometry(QtCore.QRect(270, 120, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F_Size.setFont(font)
        self.F_Size.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.F_Size.setAlignment(QtCore.Qt.AlignCenter)
        self.F_Size.setObjectName("F_Size")
        self.F_Type = QtWidgets.QLabel(Dialog)
        self.F_Type.setGeometry(QtCore.QRect(270, 200, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F_Type.setFont(font)
        self.F_Type.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.F_Type.setAlignment(QtCore.Qt.AlignCenter)
        self.F_Type.setObjectName("F_Type")
        self.F_Created = QtWidgets.QLabel(Dialog)
        self.F_Created.setGeometry(QtCore.QRect(270, 270, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F_Created.setFont(font)
        self.F_Created.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.F_Created.setAlignment(QtCore.Qt.AlignCenter)
        self.F_Created.setObjectName("F_Created")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "File Name"))
        self.label_3.setText(_translate("Dialog", " Size"))
        self.label_4.setText(_translate("Dialog", " Type"))
        self.label_5.setText(_translate("Dialog", "Modified on"))
        self.X_Lable_6.setText(_translate("Dialog", ":"))
        self.X_Lable_7.setText(_translate("Dialog", ":"))
        self.X_Lable_8.setText(_translate("Dialog", ":"))
        self.X_Lable_9.setText(_translate("Dialog", ":"))
        self.F_Name.setText(_translate("Dialog", self.filename))
        self.F_Size.setText(_translate("Dialog", self.s))
        self.F_Type.setText(_translate("Dialog", self.extension))
        self.F_Created.setText(_translate("Dialog", self.date2))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.F_Name.setText(filename)
        self.F_Type.setText(extension)
        self.F_Created.setText(date2)
        self.F_Size.setText(size)







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    (filename, extension, date2, size) = Ui_MainWindow.File_Details_usb()
    sys.exit(app.exec_())
