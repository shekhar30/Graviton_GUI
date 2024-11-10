# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DILJYOT\Desktop\Tabs Wala\keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KEYPAD(object):
    def setupUi(self, KEYPAD):
        KEYPAD.setObjectName("KEYPAD")
        KEYPAD.resize(800, 480)
        KEYPAD.setStyleSheet("QDialog{\n"
"    \n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"  border-width: 3px;\n"
"}")
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        KEYPAD.setWindowFlags(flags)
        self.PB_C = QtWidgets.QPushButton(KEYPAD)
        self.PB_C.setGeometry(QtCore.QRect(230, 330, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_C.setFont(font)
        self.PB_C.setObjectName("PB_C")
        self.PB_B = QtWidgets.QPushButton(KEYPAD)
        self.PB_B.setGeometry(QtCore.QRect(390, 330, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_B.setFont(font)
        self.PB_B.setObjectName("PB_B")
        self.PB_M = QtWidgets.QPushButton(KEYPAD)
        self.PB_M.setGeometry(QtCore.QRect(550, 330, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_M.setFont(font)
        self.PB_M.setObjectName("PB_M")
        self.PB_X = QtWidgets.QPushButton(KEYPAD)
        self.PB_X.setGeometry(QtCore.QRect(150, 330, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_X.setFont(font)
        self.PB_X.setObjectName("PB_X")
        self.PB_N = QtWidgets.QPushButton(KEYPAD)
        self.PB_N.setGeometry(QtCore.QRect(470, 330, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_N.setFont(font)
        self.PB_N.setObjectName("PB_N")
        self.PB_Z = QtWidgets.QPushButton(KEYPAD)
        self.PB_Z.setGeometry(QtCore.QRect(70, 330, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_Z.setFont(font)
        self.PB_Z.setObjectName("PB_Z")
        self.PB_V = QtWidgets.QPushButton(KEYPAD)
        self.PB_V.setGeometry(QtCore.QRect(310, 330, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_V.setFont(font)
        self.PB_V.setObjectName("PB_V")
        self.PB_E = QtWidgets.QPushButton(KEYPAD)
        self.PB_E.setGeometry(QtCore.QRect(170, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_E.setFont(font)
        self.PB_E.setObjectName("PB_E")
        self.PB_U = QtWidgets.QPushButton(KEYPAD)
        self.PB_U.setGeometry(QtCore.QRect(490, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_U.setFont(font)
        self.PB_U.setObjectName("PB_U")
        self.PB_O = QtWidgets.QPushButton(KEYPAD)
        self.PB_O.setGeometry(QtCore.QRect(650, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_O.setFont(font)
        self.PB_O.setObjectName("PB_O")
        self.PB_P = QtWidgets.QPushButton(KEYPAD)
        self.PB_P.setGeometry(QtCore.QRect(730, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_P.setFont(font)
        self.PB_P.setObjectName("PB_P")
        self.PB_T = QtWidgets.QPushButton(KEYPAD)
        self.PB_T.setGeometry(QtCore.QRect(330, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_T.setFont(font)
        self.PB_T.setObjectName("PB_T")
        self.PB_I = QtWidgets.QPushButton(KEYPAD)
        self.PB_I.setGeometry(QtCore.QRect(570, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_I.setFont(font)
        self.PB_I.setObjectName("PB_I")
        self.PB_W = QtWidgets.QPushButton(KEYPAD)
        self.PB_W.setGeometry(QtCore.QRect(90, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_W.setFont(font)
        self.PB_W.setObjectName("PB_W")
        self.PB_Q = QtWidgets.QPushButton(KEYPAD)
        self.PB_Q.setGeometry(QtCore.QRect(10, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_Q.setFont(font)
        self.PB_Q.setObjectName("PB_Q")
        self.PB_Y = QtWidgets.QPushButton(KEYPAD)
        self.PB_Y.setGeometry(QtCore.QRect(410, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_Y.setFont(font)
        self.PB_Y.setObjectName("PB_Y")
        self.PB_R = QtWidgets.QPushButton(KEYPAD)
        self.PB_R.setGeometry(QtCore.QRect(250, 210, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_R.setFont(font)
        self.PB_R.setObjectName("PB_R")
        self.PB_D = QtWidgets.QPushButton(KEYPAD)
        self.PB_D.setGeometry(QtCore.QRect(190, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_D.setFont(font)
        self.PB_D.setObjectName("PB_D")
        self.PB_J = QtWidgets.QPushButton(KEYPAD)
        self.PB_J.setGeometry(QtCore.QRect(510, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_J.setFont(font)
        self.PB_J.setObjectName("PB_J")
        self.PB_G = QtWidgets.QPushButton(KEYPAD)
        self.PB_G.setGeometry(QtCore.QRect(350, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_G.setFont(font)
        self.PB_G.setObjectName("PB_G")
        self.PB_K = QtWidgets.QPushButton(KEYPAD)
        self.PB_K.setGeometry(QtCore.QRect(590, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_K.setFont(font)
        self.PB_K.setObjectName("PB_K")
        self.PB_S = QtWidgets.QPushButton(KEYPAD)
        self.PB_S.setGeometry(QtCore.QRect(110, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_S.setFont(font)
        self.PB_S.setObjectName("PB_S")
        self.PB_A = QtWidgets.QPushButton(KEYPAD)
        self.PB_A.setGeometry(QtCore.QRect(30, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_A.setFont(font)
        self.PB_A.setObjectName("PB_A")
        self.PB_H = QtWidgets.QPushButton(KEYPAD)
        self.PB_H.setGeometry(QtCore.QRect(430, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_H.setFont(font)
        self.PB_H.setObjectName("PB_H")
        self.PB_F = QtWidgets.QPushButton(KEYPAD)
        self.PB_F.setGeometry(QtCore.QRect(270, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_F.setFont(font)
        self.PB_F.setObjectName("PB_F")
        self.PBK_2 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_2.setGeometry(QtCore.QRect(90, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_2.setFont(font)
        self.PBK_2.setObjectName("PBK_2")
        self.PBK_6 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_6.setGeometry(QtCore.QRect(410, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_6.setFont(font)
        self.PBK_6.setObjectName("PBK_6")
        self.PBK_8 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_8.setGeometry(QtCore.QRect(570, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_8.setFont(font)
        self.PBK_8.setObjectName("PBK_8")
        self.PBK_9 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_9.setGeometry(QtCore.QRect(650, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_9.setFont(font)
        self.PBK_9.setObjectName("PBK_9")
        self.PBK_4 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_4.setGeometry(QtCore.QRect(250, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_4.setFont(font)
        self.PBK_4.setObjectName("PBK_4")
        self.PBK_7 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_7.setGeometry(QtCore.QRect(490, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_7.setFont(font)
        self.PBK_7.setObjectName("PBK_7")
        self.PBK_1 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_1.setGeometry(QtCore.QRect(10, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_1.setFont(font)
        self.PBK_1.setObjectName("PBK_1")
        self.PBK_5 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_5.setGeometry(QtCore.QRect(330, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_5.setFont(font)
        self.PBK_5.setObjectName("PBK_5")
        self.PBK_3 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_3.setGeometry(QtCore.QRect(170, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_3.setFont(font)
        self.PBK_3.setObjectName("PBK_3")
        self.label = QtWidgets.QLabel(KEYPAD)
        self.label.setGeometry(QtCore.QRect(10, 15, 780, 115))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.PB_SPACE = QtWidgets.QPushButton(KEYPAD)
        self.PB_SPACE.setGeometry(QtCore.QRect(190, 395, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_SPACE.setFont(font)
        self.PB_SPACE.setObjectName("PB_SPACE")
        self.PB_BS = QtWidgets.QPushButton(KEYPAD)
        self.PB_BS.setGeometry(QtCore.QRect(630, 330, 131, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PB_BS.setFont(font)
        self.PB_BS.setStyleSheet("border-color: rgb(22, 151, 209);")
        self.PB_BS.setObjectName("PB_BS")
        self.PB_OK = QtWidgets.QPushButton(KEYPAD)
        self.PB_OK.setGeometry(QtCore.QRect(580, 395, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_OK.setFont(font)
        self.PB_OK.setStyleSheet("border-color: rgb(22, 151, 209);")
        self.PB_OK.setObjectName("PB_OK")
        self.PB_CANCEL = QtWidgets.QPushButton(KEYPAD)
        self.PB_CANCEL.setGeometry(QtCore.QRect(690, 395, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_CANCEL.setFont(font)
        self.PB_CANCEL.setStyleSheet("border-color: rgb(22, 151, 209);")
        self.PB_CANCEL.setObjectName("PB_CANCEL")
        self.PBK_0 = QtWidgets.QPushButton(KEYPAD)
        self.PBK_0.setGeometry(QtCore.QRect(730, 150, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PBK_0.setFont(font)
        self.PBK_0.setObjectName("PBK_0")
        self.PB_L = QtWidgets.QPushButton(KEYPAD)
        self.PB_L.setGeometry(QtCore.QRect(670, 270, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_L.setFont(font)
        self.PB_L.setObjectName("PB_L")

        self.retranslateUi(KEYPAD)
        self.PB_CANCEL.clicked.connect(KEYPAD.close)
        self.PB_OK.clicked.connect(KEYPAD.accept)
        QtCore.QMetaObject.connectSlotsByName(KEYPAD)
        self.PB_Q.clicked.connect(self.set_Q)
        self.PB_W.clicked.connect(self.set_W)
        self.PB_E.clicked.connect(self.set_E)
        self.PB_R.clicked.connect(self.set_R)
        self.PB_T.clicked.connect(self.set_T)
        self.PB_Y.clicked.connect(self.set_Y)
        self.PB_U.clicked.connect(self.set_U)
        self.PB_I.clicked.connect(self.set_I)
        self.PB_O.clicked.connect(self.set_O)
        self.PB_P.clicked.connect(self.set_P)
        self.PB_A.clicked.connect(self.set_A)
        self.PB_S.clicked.connect(self.set_S)
        self.PB_D.clicked.connect(self.set_D)
        self.PB_F.clicked.connect(self.set_F)
        self.PB_G.clicked.connect(self.set_G)
        self.PB_H.clicked.connect(self.set_H)
        self.PB_J.clicked.connect(self.set_J)
        self.PB_K.clicked.connect(self.set_K)
        self.PB_L.clicked.connect(self.set_L)
        self.PB_Z.clicked.connect(self.set_Z)
        self.PB_X.clicked.connect(self.set_X)
        self.PB_C.clicked.connect(self.set_C)
        self.PB_V.clicked.connect(self.set_V)
        self.PB_B.clicked.connect(self.set_B)
        self.PB_N.clicked.connect(self.set_N)
        self.PB_M.clicked.connect(self.set_M)
        self.PBK_0.clicked.connect(self.set_0)
        self.PBK_1.clicked.connect(self.set_1)
        self.PBK_2.clicked.connect(self.set_2)
        self.PBK_3.clicked.connect(self.set_3)
        self.PBK_4.clicked.connect(self.set_4)
        self.PBK_5.clicked.connect(self.set_5)
        self.PBK_6.clicked.connect(self.set_6)
        self.PBK_7.clicked.connect(self.set_7)
        self.PBK_8.clicked.connect(self.set_8)
        self.PBK_9.clicked.connect(self.set_9)
        self.PB_SPACE.clicked.connect(self.set_space)
        self.PB_BS.clicked.connect(self.set_backspace)

    global k
    k = ''

    def set_Q(self):
            global k
            self.label.setText('Q')
            k = str(k) + 'Q'

    def set_W(self):
            global k
            self.label.setText(str(k)+'W')
            k = str(k) + 'W'

    def set_E(self):
            global k
            self.label.setText(str(k)+'E')
            k = str(k) + 'E'

    def set_R(self):
            global k
            self.label.setText(str(k)+'R')
            k = str(k) + 'R'

    def set_T(self):
            global k
            self.label.setText(str(k)+'T')
            k = str(k) + 'T'

    def set_Y(self):
            global k
            self.label.setText(str(k)+'Y')
            k = str(k) + 'Y'

    def set_U(self):
            global k
            self.label.setText(str(k)+'U')
            k = str(k) + 'U'

    def set_I(self):
            global k
            self.label.setText(str(k)+'I')
            k = str(k) + 'I'

    def set_O(self):
            global k
            self.label.setText(str(k)+'O')
            k = str(k) + 'O'

    def set_P(self):
            global k
            self.label.setText(str(k)+'P')
            k = str(k) + 'P'

    def set_A(self):
            global k
            self.label.setText(str(k)+'A')
            k = str(k) + 'A'

    def set_S(self):
            global k
            self.label.setText(str(k)+'S')
            k = str(k) + 'S'

    def set_D(self):
            global k
            self.label.setText(str(k)+'D')
            k = str(k) + 'D'

    def set_F(self):
            global k
            self.label.setText(str(k)+'F')
            k = str(k) + 'F'

    def set_G(self):
            global k
            self.label.setText(str(k)+'G')
            k = str(k) + 'G'

    def set_H(self):
            global k
            self.label.setText(str(k)+'H')
            k = str(k) + 'H'

    def set_J(self):
            global k
            self.label.setText(str(k)+'J')
            k = str(k) + 'J'

    def set_K(self):
            global k
            self.label.setText(str(k)+'K')
            k = str(k) + 'K'

    def set_L(self):
            global k
            self.label.setText(str(k)+'L')
            k = str(k) + 'L'

    def set_Z(self):
            global k
            self.label.setText(str(k)+'Z')
            k = str(k) + 'Z'

    def set_X(self):
            global k
            self.label.setText(str(k)+'X')
            k = str(k) + 'X'

    def set_C(self):
            global k
            self.label.setText(str(k)+'C')
            k = str(k) + 'C'

    def set_V(self):
            global k
            self.label.setText(str(k)+'V')
            k = str(k) + 'V'

    def set_B(self):
            global k
            self.label.setText(str(k)+'B')
            k = str(k) + 'B'

    def set_N(self):
            global k
            self.label.setText(str(k)+'N')
            k = str(k) + 'N'

    def set_M(self):
            global k
            self.label.setText(str(k)+'M')
            k = str(k) + 'M'

    def set_1(self):
            global k
            self.label.setText(str(k)+'1')
            k = str(k) + '1'

    def set_2(self):
            global k
            self.label.setText(str(k)+'2')
            k = str(k) + '2'

    def set_3(self):
            global k
            self.label.setText(str(k)+'3')
            k = str(k) + '3'

    def set_4(self):
            global k
            self.label.setText(str(k)+'4')
            k = str(k) + '4'

    def set_5(self):
            global k
            self.label.setText(str(k)+'5')
            k = str(k) + '5'

    def set_6(self):
            global k
            self.label.setText(str(k)+'6')
            k = str(k) + '6'

    def set_7(self):
            global k
            self.label.setText(str(k)+'7')
            k = str(k) + '7'

    def set_8(self):
            global k
            self.label.setText(str(k)+'8')
            k = str(k) + '8'

    def set_9(self):
            global k
            self.label.setText(str(k)+'9')
            k = str(k) + '9'

    def set_0(self):
            global k
            self.label.setText(str(k)+'0')
            k = str(k) + '0'

    def set_space(self):
            global k
            self.label.setText(str(k)+' ')
            k = str(k) + ' '

    def set_backspace(self):
            global k
            self.label.setText(k[:-1])
            k = k[:-1]

    def retranslateUi(self, KEYPAD):
        _translate = QtCore.QCoreApplication.translate
        KEYPAD.setWindowTitle(_translate("KEYPAD", "Dialog"))
        self.PB_C.setText(_translate("KEYPAD", "C"))
        self.PB_B.setText(_translate("KEYPAD", "B"))
        self.PB_M.setText(_translate("KEYPAD", "M"))
        self.PB_X.setText(_translate("KEYPAD", "X"))
        self.PB_N.setText(_translate("KEYPAD", "N"))
        self.PB_Z.setText(_translate("KEYPAD", "Z"))
        self.PB_V.setText(_translate("KEYPAD", "V"))
        self.PB_E.setText(_translate("KEYPAD", "E"))
        self.PB_U.setText(_translate("KEYPAD", "U"))
        self.PB_O.setText(_translate("KEYPAD", "O"))
        self.PB_P.setText(_translate("KEYPAD", "P"))
        self.PB_T.setText(_translate("KEYPAD", "T"))
        self.PB_I.setText(_translate("KEYPAD", "I"))
        self.PB_W.setText(_translate("KEYPAD", "W"))
        self.PB_Q.setText(_translate("KEYPAD", "Q"))
        self.PB_Y.setText(_translate("KEYPAD", "Y"))
        self.PB_R.setText(_translate("KEYPAD", "R"))
        self.PB_D.setText(_translate("KEYPAD", "D"))
        self.PB_J.setText(_translate("KEYPAD", "J"))
        self.PB_G.setText(_translate("KEYPAD", "G"))
        self.PB_K.setText(_translate("KEYPAD", "K"))
        self.PB_S.setText(_translate("KEYPAD", "S"))
        self.PB_A.setText(_translate("KEYPAD", "A"))
        self.PB_H.setText(_translate("KEYPAD", "H"))
        self.PB_F.setText(_translate("KEYPAD", "F"))
        self.PBK_2.setText(_translate("KEYPAD", "2"))
        self.PBK_6.setText(_translate("KEYPAD", "6"))
        self.PBK_8.setText(_translate("KEYPAD", "8"))
        self.PBK_9.setText(_translate("KEYPAD", "9"))
        self.PBK_4.setText(_translate("KEYPAD", "4"))
        self.PBK_7.setText(_translate("KEYPAD", "7"))
        self.PBK_1.setText(_translate("KEYPAD", "1"))
        self.PBK_5.setText(_translate("KEYPAD", "5"))
        self.PBK_3.setText(_translate("KEYPAD", "3"))
        self.label.setText(_translate("KEYPAD", "Graviton"))
        self.PB_SPACE.setText(_translate("KEYPAD", "SPACE"))
        self.PB_BS.setText(_translate("KEYPAD", "⌫"))
        self.PB_OK.setText(_translate("KEYPAD", "OK"))
        self.PB_CANCEL.setText(_translate("KEYPAD", "Cancel"))
        self.PBK_0.setText(_translate("KEYPAD", "0"))
        self.PB_L.setText(_translate("KEYPAD", "L"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KEYPAD = QtWidgets.QDialog()
    ui = Ui_KEYPAD()
    ui.setupUi(KEYPAD)
    KEYPAD.show()
    sys.exit(app.exec_())

