# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\shekh\PycharmProjects\GRAVITON 3.0\All.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Resources_1
from octorest import *
import datetime
from keypad import Ui_Temperature_Setup_dialog
from File_Dialog import Ui_Dialog
import json
from qroundprogressbar import QRoundProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush,QColor,QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from keyboard import Ui_KEYPAD
import os
import os.path
import pathlib
from os import listdir
from os.path import isfile, join
import sys
import glob
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    \n"
"    \n"
"    background-image: url(:/NEW/Icons/carbon-fiber-pattern1-png.png);\n"
"border: none;\n"
"}\n"
"QTabBar::tab{\n"
"background: transparent;\n"
"border: none;\n"
"\n"
"}\n"
"QTabWidget::pane{\n"
"background: transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"border-bottom: 4px solid;\n"
"border-bottom-color: rgb(22, 151, 209);\n"
"}")
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlags(flags)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 480))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QWidget\n"
"{\n"
"border: none;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(125, 70))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.File_PB = QtWidgets.QPushButton(self.Home)
        self.File_PB.setGeometry(QtCore.QRect(160, 340, 491, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.File_PB.setFont(font)
        self.File_PB.setStyleSheet("\n"
"QPushButton {\n"
"color: rgb(255,255,255);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    color:rgb(22, 151, 209)\n"
"}")
        self.File_PB.setObjectName("File_PB")
        self.ProgressBar = QRoundProgressBar(self.Home)
        self.ProgressBar.setGeometry(QtCore.QRect(300, 140, 241, 121))
        self.palette = QPalette()
        brush = QBrush(QColor(0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.palette.setColor(QPalette.Text, QColor(255, 255, 255))
        self.palette.setColor(QPalette.WindowText, Qt.white)
        self.palette.setColor(QPalette.AlternateBase, QColor(0, 0, 0))
        self.palette.setColor(QPalette.ToolTipBase, Qt.white)
        self.palette.setColor(QPalette.ToolTipText, Qt.white)
        self.palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        self.palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        self.ProgressBar.setPalette(self.palette)

        self.ProgressBar.setStyleSheet("QProgressBar {\n"
                                       "\n"
                                       "color: rgb(255,255,255);\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.ProgressBar.setValue(0)
        self.ProgressBar.setDataColors([(0., QtGui.QColor.fromRgb(255, 0, 0)), (0.5, QtGui.QColor.fromRgb(255, 255, 0)),
                                        (1., QtGui.QColor.fromRgb(0, 255, 0))])
        self.ProgressBar.setObjectName("ProgressBar")
        self.layoutWidget = QtWidgets.QWidget(self.Home)
        self.layoutWidget.setGeometry(QtCore.QRect(560, 20, 221, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Start_TB = QtWidgets.QToolButton(self.layoutWidget)
        self.Start_TB.setStyleSheet("QToolButton:open {\n"
"image: url(:/resources/Resource Image/pause (3).png);\n"
"}\n"
"QToolButton:closed {\n"
"image: url(:/IMG/IMG/play.png);\n"
"\n"
"}\n"
"")
        self.Start_TB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/pause-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Start_TB.setIcon(icon)
        self.Start_TB.setIconSize(QtCore.QSize(90, 90))
        self.Start_TB.setCheckable(True)
        self.Start_TB.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Start_TB.setObjectName("Start_TB")
        self.horizontalLayout.addWidget(self.Start_TB)
        self.Stop_TB = QtWidgets.QToolButton(self.layoutWidget)
        self.Stop_TB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/NEW/Icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop_TB.setIcon(icon1)
        self.Stop_TB.setIconSize(QtCore.QSize(90, 90))
        self.Stop_TB.setCheckable(True)
        self.Stop_TB.setObjectName("Stop_TB")
        self.horizontalLayout.addWidget(self.Stop_TB)
        self.TE_Box = QtWidgets.QLabel(self.Home)
        self.TE_Box.setGeometry(QtCore.QRect(685, 140, 101, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TE_Box.setFont(font)
        self.TE_Box.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(0, 170, 255);\n"
"border-right: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"")
        self.TE_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.TE_Box.setObjectName("TE_Box")
        self.TR_Box = QtWidgets.QLabel(self.Home)
        self.TR_Box.setGeometry(QtCore.QRect(685, 220, 101, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TR_Box.setFont(font)
        self.TR_Box.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(0, 170, 255);\n"
"border-right: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"")
        self.TR_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.TR_Box.setObjectName("TR_Box")
        self.Nozzle_1_Temp = QtWidgets.QLabel(self.Home)
        self.Nozzle_1_Temp.setGeometry(QtCore.QRect(130, 50, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Nozzle_1_Temp.setFont(font)
        self.Nozzle_1_Temp.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.Nozzle_1_Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.Nozzle_1_Temp.setObjectName("Nozzle_1_Temp")
        self.Nozzle_2_Temp = QtWidgets.QLabel(self.Home)
        self.Nozzle_2_Temp.setGeometry(QtCore.QRect(130, 150, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Nozzle_2_Temp.setFont(font)
        self.Nozzle_2_Temp.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.Nozzle_2_Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.Nozzle_2_Temp.setObjectName("Nozzle_2_Temp")
        self.Bed_Temp = QtWidgets.QLabel(self.Home)
        self.Bed_Temp.setGeometry(QtCore.QRect(130, 250, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Bed_Temp.setFont(font)
        self.Bed_Temp.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.Bed_Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.Bed_Temp.setObjectName("Bed_Temp")
        self.Time_E_Label_2 = QtWidgets.QLabel(self.Home)
        self.Time_E_Label_2.setGeometry(QtCore.QRect(665, 140, 20, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time_E_Label_2.setFont(font)
        self.Time_E_Label_2.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.Time_E_Label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_E_Label_2.setObjectName("Time_E_Label_2")
        self.Time_E_Label_3 = QtWidgets.QLabel(self.Home)
        self.Time_E_Label_3.setGeometry(QtCore.QRect(665, 220, 20, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time_E_Label_3.setFont(font)
        self.Time_E_Label_3.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.Time_E_Label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_E_Label_3.setObjectName("Time_E_Label_3")
        self.Time_E_Label = QtWidgets.QLabel(self.Home)
        self.Time_E_Label.setGeometry(QtCore.QRect(510, 140, 155, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time_E_Label.setFont(font)
        self.Time_E_Label.setAutoFillBackground(False)
        self.Time_E_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"border-left: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.Time_E_Label.setScaledContents(True)
        self.Time_E_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_E_Label.setObjectName("Time_E_Label")
        self.Time_R_Label = QtWidgets.QLabel(self.Home)
        self.Time_R_Label.setGeometry(QtCore.QRect(510, 220, 155, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time_R_Label.setFont(font)
        self.Time_R_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"border-left: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.Time_R_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_R_Label.setObjectName("Time_R_Label")
        self.label_3 = QtWidgets.QLabel(self.Home)
        self.label_3.setGeometry(QtCore.QRect(25, 50, 81, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("image: url(:/resources/0690fa67-890a-4296-a412-f2e701473940.jpg);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/NEW/Icons/nozzle_up-256.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.Home)
        self.label_5.setGeometry(QtCore.QRect(25, 250, 81, 71))
        self.label_5.setStyleSheet("image: url(:/resources/Heated-Bed.png);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/NEW/Icons/bed_hot-256.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.Home)
        self.label_4.setGeometry(QtCore.QRect(25, 150, 81, 71))
        self.label_4.setStyleSheet("image: url(:/resources/0690fa67-890a-4296-a412-f2e701473940.jpg);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/NEW/Icons/nozzle_x2-512.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/NEW/Icons/home (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Home, icon2, "")
        self.Controls = QtWidgets.QWidget()
        self.Controls.setObjectName("Controls")
        self.Y_Up_Label = QtWidgets.QLabel(self.Controls)
        self.Y_Up_Label.setGeometry(QtCore.QRect(370, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Y_Up_Label.setFont(font)
        self.Y_Up_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Y_Up_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Y_Up_Label.setObjectName("Y_Up_Label")
        self.Z_Down_Label = QtWidgets.QLabel(self.Controls)
        self.Z_Down_Label.setGeometry(QtCore.QRect(660, 365, 31, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Z_Down_Label.setFont(font)
        self.Z_Down_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Z_Down_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Z_Down_Label.setObjectName("Z_Down_Label")
        self.Y_Up_PB = QtWidgets.QPushButton(self.Controls)
        self.Y_Up_PB.setGeometry(QtCore.QRect(340, 110, 90, 70))
        self.Y_Up_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Y_Up_PB.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.Y_Up_PB.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/NEW/Icons/up-arrow-angle (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Y_Up_PB.setIcon(icon3)
        self.Y_Up_PB.setIconSize(QtCore.QSize(80, 70))
        self.Y_Up_PB.setObjectName("Y_Up_PB")
        self.X_Lable = QtWidgets.QLabel(self.Controls)
        self.X_Lable.setGeometry(QtCore.QRect(260, 20, 50, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable.setFont(font)
        self.X_Lable.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"border-left: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable.setObjectName("X_Lable")
        self.Y_Value = QtWidgets.QLabel(self.Controls)
        self.Y_Value.setGeometry(QtCore.QRect(500, 20, 61, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Y_Value.setFont(font)
        self.Y_Value.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(0, 170, 255);\n"
"border-right: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"")
        self.Y_Value.setAlignment(QtCore.Qt.AlignCenter)
        self.Y_Value.setObjectName("Y_Value")
        self.X_Down_Label = QtWidgets.QLabel(self.Controls)
        self.X_Down_Label.setGeometry(QtCore.QRect(210, 220, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Down_Label.setFont(font)
        self.X_Down_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.X_Down_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Down_Label.setObjectName("X_Down_Label")
        self.X_Up_Label = QtWidgets.QLabel(self.Controls)
        self.X_Up_Label.setGeometry(QtCore.QRect(520, 220, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Up_Label.setFont(font)
        self.X_Up_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.X_Up_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Up_Label.setObjectName("X_Up_Label")
        self.XY_Home_PB = QtWidgets.QPushButton(self.Controls)
        self.XY_Home_PB.setGeometry(QtCore.QRect(340, 190, 90, 90))
        self.XY_Home_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.XY_Home_PB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.XY_Home_PB.setText("")
        self.XY_Home_PB.setIcon(icon2)
        self.XY_Home_PB.setIconSize(QtCore.QSize(90, 90))
        self.XY_Home_PB.setObjectName("XY_Home_PB")
        self.Z_Home_PB = QtWidgets.QPushButton(self.Controls)
        self.Z_Home_PB.setGeometry(QtCore.QRect(630, 190, 90, 90))
        self.Z_Home_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_Home_PB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.Z_Home_PB.setText("")
        self.Z_Home_PB.setIcon(icon2)
        self.Z_Home_PB.setIconSize(QtCore.QSize(90, 90))
        self.Z_Home_PB.setObjectName("Z_Home_PB")
        self.Z_up_Label = QtWidgets.QLabel(self.Controls)
        self.Z_up_Label.setGeometry(QtCore.QRect(660, 80, 31, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Z_up_Label.setFont(font)
        self.Z_up_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Z_up_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Z_up_Label.setObjectName("Z_up_Label")
        self.Z_Down_PB = QtWidgets.QPushButton(self.Controls)
        self.Z_Down_PB.setGeometry(QtCore.QRect(630, 290, 90, 70))
        self.Z_Down_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_Down_PB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.Z_Down_PB.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/NEW/Icons/descendant-arrow-angle (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Z_Down_PB.setIcon(icon4)
        self.Z_Down_PB.setIconSize(QtCore.QSize(80, 70))
        self.Z_Down_PB.setObjectName("Z_Down_PB")
        self.Y_Label = QtWidgets.QLabel(self.Controls)
        self.Y_Label.setGeometry(QtCore.QRect(430, 20, 50, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Y_Label.setFont(font)
        self.Y_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"border-left: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.Y_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Y_Label.setObjectName("Y_Label")
        self.Z_Up_PB = QtWidgets.QPushButton(self.Controls)
        self.Z_Up_PB.setGeometry(QtCore.QRect(630, 110, 90, 70))
        self.Z_Up_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_Up_PB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.Z_Up_PB.setText("")
        self.Z_Up_PB.setIcon(icon3)
        self.Z_Up_PB.setIconSize(QtCore.QSize(80, 70))
        self.Z_Up_PB.setObjectName("Z_Up_PB")
        self.X_Down_PB = QtWidgets.QPushButton(self.Controls)
        self.X_Down_PB.setGeometry(QtCore.QRect(260, 190, 70, 90))
        self.X_Down_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.X_Down_PB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.X_Down_PB.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/NEW/Icons/left-arrow-angle (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.X_Down_PB.setIcon(icon5)
        self.X_Down_PB.setIconSize(QtCore.QSize(80, 70))
        self.X_Down_PB.setObjectName("X_Down_PB")
        self.X_Value = QtWidgets.QLabel(self.Controls)
        self.X_Value.setGeometry(QtCore.QRect(330, 20, 61, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Value.setFont(font)
        self.X_Value.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(0, 170, 255);\n"
"border-right: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"")
        self.X_Value.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Value.setObjectName("X_Value")
        self.X_Up_PB = QtWidgets.QPushButton(self.Controls)
        self.X_Up_PB.setGeometry(QtCore.QRect(440, 190, 70, 90))
        self.X_Up_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.X_Up_PB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.X_Up_PB.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/NEW/Icons/arrow-angle-pointing-to-right (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.X_Up_PB.setIcon(icon6)
        self.X_Up_PB.setIconSize(QtCore.QSize(80, 70))
        self.X_Up_PB.setObjectName("X_Up_PB")
        self.PB_01 = QtWidgets.QPushButton(self.Controls)
        self.PB_01.setGeometry(QtCore.QRect(20, 50, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PB_01.setFont(font)
        self.PB_01.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_01.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 1px solid white;\n"
"}\n"
"QPushButton:open {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:closed {\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 31, 31);\n"
"}\n"
"")
        self.PB_01.setCheckable(True)
        self.PB_01.setChecked(False)
        self.PB_01.setAutoExclusive(True)
        self.PB_01.setObjectName("PB_01")
        self.Y_Down_PB = QtWidgets.QPushButton(self.Controls)
        self.Y_Down_PB.setGeometry(QtCore.QRect(340, 290, 90, 70))
        self.Y_Down_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Y_Down_PB.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.Y_Down_PB.setText("")
        self.Y_Down_PB.setIcon(icon4)
        self.Y_Down_PB.setIconSize(QtCore.QSize(80, 70))
        self.Y_Down_PB.setObjectName("Y_Down_PB")
        self.Z_Label = QtWidgets.QLabel(self.Controls)
        self.Z_Label.setGeometry(QtCore.QRect(600, 20, 50, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Z_Label.setFont(font)
        self.Z_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"border-left: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.Z_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Z_Label.setObjectName("Z_Label")
        self.Z_Value = QtWidgets.QLabel(self.Controls)
        self.Z_Value.setGeometry(QtCore.QRect(670, 20, 61, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Z_Value.setFont(font)
        self.Z_Value.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(0, 170, 255);\n"
"border-right: 1px solid white;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"")
        self.Z_Value.setAlignment(QtCore.Qt.AlignCenter)
        self.Z_Value.setObjectName("Z_Value")
        self.Y_Down_Label = QtWidgets.QLabel(self.Controls)
        self.Y_Down_Label.setGeometry(QtCore.QRect(370, 370, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Y_Down_Label.setFont(font)
        self.Y_Down_Label.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Y_Down_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Y_Down_Label.setObjectName("Y_Down_Label")
        self.PB_100 = QtWidgets.QPushButton(self.Controls)
        self.PB_100.setGeometry(QtCore.QRect(20, 290, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PB_100.setFont(font)
        self.PB_100.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_100.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 1px solid white;\n"
"}\n"
"QPushButton:open {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:closed {\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 31, 31);\n"
"}\n"
"")
        self.PB_100.setCheckable(True)
        self.PB_100.setAutoExclusive(True)
        self.PB_100.setObjectName("PB_100")
        self.PB_1 = QtWidgets.QPushButton(self.Controls)
        self.PB_1.setGeometry(QtCore.QRect(20, 130, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PB_1.setFont(font)
        self.PB_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_1.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 1px solid white;\n"
"}\n"
"QPushButton:open {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:closed {\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 31, 31);\n"
"}\n"
"")
        self.PB_1.setCheckable(True)
        self.PB_1.setAutoExclusive(True)
        self.PB_1.setObjectName("PB_1")
        self.PB_10 = QtWidgets.QPushButton(self.Controls)
        self.PB_10.setGeometry(QtCore.QRect(20, 210, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PB_10.setFont(font)
        self.PB_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_10.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border: 1px solid white;\n"
"}\n"
"QPushButton:open {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:closed {\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 31, 31);\n"
"}\n"
"")
        self.PB_10.setCheckable(True)
        self.PB_10.setAutoExclusive(True)
        self.PB_10.setObjectName("PB_10")
        self.X_Lable_3 = QtWidgets.QLabel(self.Controls)
        self.X_Lable_3.setGeometry(QtCore.QRect(310, 20, 21, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable_3.setFont(font)
        self.X_Lable_3.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable_3.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_3.setObjectName("X_Lable_3")
        self.X_Lable_4 = QtWidgets.QLabel(self.Controls)
        self.X_Lable_4.setGeometry(QtCore.QRect(480, 20, 21, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable_4.setFont(font)
        self.X_Lable_4.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable_4.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_4.setObjectName("X_Lable_4")
        self.X_Lable_5 = QtWidgets.QLabel(self.Controls)
        self.X_Lable_5.setGeometry(QtCore.QRect(650, 20, 21, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.X_Lable_5.setFont(font)
        self.X_Lable_5.setStyleSheet("QLabel {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"\n"
"}\n"
"\n"
"")
        self.X_Lable_5.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_5.setObjectName("X_Lable_5")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/NEW/Icons/levels (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Controls, icon7, "")
        self.Temperature = QtWidgets.QWidget()
        self.Temperature.setObjectName("Temperature")
        self.CT_Label = QtWidgets.QLabel(self.Temperature)
        self.CT_Label.setGeometry(QtCore.QRect(220, 50, 110, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CT_Label.setFont(font)
        self.CT_Label.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 170, 255);\n"
"border: 1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"")
        self.CT_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_Label.setObjectName("CT_Label")
        self.CT_Label_3 = QtWidgets.QLabel(self.Temperature)
        self.CT_Label_3.setGeometry(QtCore.QRect(380, 50, 120, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CT_Label_3.setFont(font)
        self.CT_Label_3.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 170, 255);\n"
"border: 1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"")
        self.CT_Label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_Label_3.setObjectName("CT_Label_3")
        self.ST_E1_Temp = QtWidgets.QPushButton(self.Temperature)
        self.ST_E1_Temp.setGeometry(QtCore.QRect(380, 130, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ST_E1_Temp.setFont(font)
        self.ST_E1_Temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ST_E1_Temp.setStyleSheet("QPushButton{\n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.ST_E1_Temp.setObjectName("ST_E1_Temp")
        self.ST_Bed_Temp = QtWidgets.QPushButton(self.Temperature)
        self.ST_Bed_Temp.setGeometry(QtCore.QRect(380, 290, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ST_Bed_Temp.setFont(font)
        self.ST_Bed_Temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ST_Bed_Temp.setStyleSheet("QPushButton{\n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.ST_Bed_Temp.setObjectName("ST_Bed_Temp")
        self.ST_E2_Temp = QtWidgets.QPushButton(self.Temperature)
        self.ST_E2_Temp.setGeometry(QtCore.QRect(380, 210, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ST_E2_Temp.setFont(font)
        self.ST_E2_Temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ST_E2_Temp.setStyleSheet("QPushButton{\n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.ST_E2_Temp.setObjectName("ST_E2_Temp")
        self.ABS_Temp = QtWidgets.QPushButton(self.Temperature)
        self.ABS_Temp.setGeometry(QtCore.QRect(610, 50, 150, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ABS_Temp.setFont(font)
        self.ABS_Temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ABS_Temp.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:open {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:closed {\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 31, 31);\n"
"}")
        self.ABS_Temp.setCheckable(True)
        self.ABS_Temp.setAutoExclusive(True)
        self.ABS_Temp.setObjectName("ABS_Temp")
        self.PLA_Temp = QtWidgets.QPushButton(self.Temperature)
        self.PLA_Temp.setGeometry(QtCore.QRect(610, 130, 150, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PLA_Temp.setFont(font)
        self.PLA_Temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PLA_Temp.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:open {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:closed {\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 31, 31);\n"
"}")
        self.PLA_Temp.setCheckable(True)
        self.PLA_Temp.setAutoExclusive(True)
        self.PLA_Temp.setObjectName("PLA_Temp")
        self.PETG_Temp = QtWidgets.QPushButton(self.Temperature)
        self.PETG_Temp.setGeometry(QtCore.QRect(610, 210, 150, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PETG_Temp.setFont(font)
        self.PETG_Temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PETG_Temp.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:open {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:closed {\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 31, 31);\n"
"}")
        self.PETG_Temp.setCheckable(True)
        self.PETG_Temp.setAutoExclusive(True)
        self.PETG_Temp.setObjectName("PETG_Temp")
        self.Cooldown_Temp = QtWidgets.QPushButton(self.Temperature)
        self.Cooldown_Temp.setGeometry(QtCore.QRect(610, 290, 150, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Cooldown_Temp.setFont(font)
        self.Cooldown_Temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cooldown_Temp.setStyleSheet("QPushButton{\n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Cooldown_Temp.setCheckable(True)
        self.Cooldown_Temp.setAutoExclusive(True)
        self.Cooldown_Temp.setObjectName("Cooldown_Temp")
        self.CT_E1_Temp = QtWidgets.QLabel(self.Temperature)
        self.CT_E1_Temp.setGeometry(QtCore.QRect(220, 130, 110, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CT_E1_Temp.setFont(font)
        self.CT_E1_Temp.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.CT_E1_Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_E1_Temp.setObjectName("CT_E1_Temp")
        self.CT_E2_Temp = QtWidgets.QLabel(self.Temperature)
        self.CT_E2_Temp.setGeometry(QtCore.QRect(220, 210, 110, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CT_E2_Temp.setFont(font)
        self.CT_E2_Temp.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.CT_E2_Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_E2_Temp.setObjectName("CT_E2_Temp")
        self.CT_Bed_Temp = QtWidgets.QLabel(self.Temperature)
        self.CT_Bed_Temp.setGeometry(QtCore.QRect(220, 290, 110, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CT_Bed_Temp.setFont(font)
        self.CT_Bed_Temp.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.CT_Bed_Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_Bed_Temp.setObjectName("CT_Bed_Temp")
        self.label_16 = QtWidgets.QLabel(self.Temperature)
        self.label_16.setGeometry(QtCore.QRect(100, 130, 81, 71))
        self.label_16.setStyleSheet("image: url(:/resources/0690fa67-890a-4296-a412-f2e701473940.jpg);")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/NEW/Icons/nozzle_up-256.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.Temperature)
        self.label_18.setGeometry(QtCore.QRect(100, 290, 81, 71))
        self.label_18.setStyleSheet("image: url(:/resources/Heated-Bed.png);")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/NEW/Icons/bed_hot-256.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_6 = QtWidgets.QLabel(self.Temperature)
        self.label_6.setGeometry(QtCore.QRect(100, 210, 81, 71))
        self.label_6.setStyleSheet("image: url(:/resources/0690fa67-890a-4296-a412-f2e701473940.jpg);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/NEW/Icons/nozzle_x2-512.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/NEW/Icons/thermometer (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Temperature, icon8, "")
        self.Files = QtWidgets.QWidget()
        self.Files.setObjectName("Files")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.Files)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 0, 790, 400))
        self.tabWidget_3.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_3.setIconSize(QtCore.QSize(70, 86))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.USB_Print_PB = QtWidgets.QPushButton(self.tab)
        self.USB_Print_PB.setGeometry(QtCore.QRect(20, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.USB_Print_PB.setFont(font)
        self.USB_Print_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.USB_Print_PB.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.USB_Print_PB.setObjectName("USB_Print_PB")
        self.USB_Upload_PB = QtWidgets.QPushButton(self.tab)
        self.USB_Upload_PB.setGeometry(QtCore.QRect(270, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.USB_Upload_PB.setFont(font)
        self.USB_Upload_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.USB_Upload_PB.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.USB_Upload_PB.setObjectName("USB_Upload_PB")
        self.USB_FD_PB = QtWidgets.QPushButton(self.tab)
        self.USB_FD_PB.setGeometry(QtCore.QRect(520, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.USB_FD_PB.setFont(font)
        self.USB_FD_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.USB_FD_PB.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.USB_FD_PB.setObjectName("USB_FD_PB")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 160, 681, 241))
        self.listWidget.setStyleSheet("background: transparent")
        self.listWidget.setObjectName("listWidget")
        self.USB_Back_PB = QtWidgets.QPushButton(self.tab)
        self.USB_Back_PB.setGeometry(QtCore.QRect(15, 100, 71, 31))
        self.USB_Back_PB.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.USB_Back_PB.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/NEW/Icons/reply-all-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.USB_Back_PB.setIcon(icon9)
        self.USB_Back_PB.setIconSize(QtCore.QSize(40, 40))
        self.USB_Back_PB.setObjectName("USB_Back_PB")
        self.USB_File_Home_PB = QtWidgets.QPushButton(self.tab)
        self.USB_File_Home_PB.setGeometry(QtCore.QRect(90, 100, 71, 31))
        self.USB_File_Home_PB.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.USB_File_Home_PB.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/NEW/Icons/web-page-home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.USB_File_Home_PB.setIcon(icon10)
        self.USB_File_Home_PB.setIconSize(QtCore.QSize(40, 35))
        self.USB_File_Home_PB.setObjectName("USB_File_Home_PB")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/NEW/Icons/usb (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab, icon11, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.FD_PB = QtWidgets.QPushButton(self.tab_2)
        self.FD_PB.setGeometry(QtCore.QRect(520, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FD_PB.setFont(font)
        self.FD_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FD_PB.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.FD_PB.setObjectName("FD_PB")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 160, 681, 241))
        self.listWidget_2.setStyleSheet("background: transparent")
        self.listWidget_2.setObjectName("listWidget_2")
        self.Print_PB = QtWidgets.QPushButton(self.tab_2)
        self.Print_PB.setGeometry(QtCore.QRect(20, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Print_PB.setFont(font)
        self.Print_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Print_PB.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.Print_PB.setObjectName("Print_PB")
        self.File_Home_PB = QtWidgets.QPushButton(self.tab_2)
        self.File_Home_PB.setGeometry(QtCore.QRect(90, 100, 71, 31))
        self.File_Home_PB.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.File_Home_PB.setText("")
        self.File_Home_PB.setIcon(icon10)
        self.File_Home_PB.setIconSize(QtCore.QSize(40, 35))
        self.File_Home_PB.setObjectName("File_Home_PB")
        self.Back_PB = QtWidgets.QPushButton(self.tab_2)
        self.Back_PB.setGeometry(QtCore.QRect(15, 100, 71, 31))
        self.Back_PB.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.Back_PB.setText("")
        self.Back_PB.setIcon(icon9)
        self.Back_PB.setIconSize(QtCore.QSize(40, 40))
        self.Back_PB.setObjectName("Back_PB")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/NEW/Icons/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_2, icon12, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/NEW/Icons/folder (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Files, icon13, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Settings)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 791, 401))
        self.tabWidget_2.setStyleSheet("border:none;")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_2.setIconSize(QtCore.QSize(70, 86))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.WiFi = QtWidgets.QWidget()
        self.WiFi.setObjectName("WiFi")
        self.listWidget_3 = QtWidgets.QListWidget(self.WiFi)
        self.listWidget_3.setGeometry(QtCore.QRect(5, 81, 691, 311))
        self.listWidget_3.setStyleSheet("background: transparent")
        self.listWidget_3.setObjectName("listWidget_3")
        self.wifi_connect_PB = QtWidgets.QPushButton(self.WiFi)
        self.wifi_connect_PB.setGeometry(QtCore.QRect(220, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.wifi_connect_PB.setFont(font)
        self.wifi_connect_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wifi_connect_PB.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.wifi_connect_PB.setObjectName("wifi_connect_PB")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/NEW/Icons/wifi (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.WiFi, icon14, "")
        self.Printer_Settings = QtWidgets.QWidget()
        self.Printer_Settings.setObjectName("Printer_Settings")
        self.Connect_PB = QtWidgets.QPushButton(self.Printer_Settings)
        self.Connect_PB.setGeometry(QtCore.QRect(220, 260, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Connect_PB.setFont(font)
        self.Connect_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Connect_PB.setStyleSheet("QPushButton{\n"
"border: 1px solid white;\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.Connect_PB.setObjectName("Connect_PB")
        self.label = QtWidgets.QLabel(self.Printer_Settings)
        self.label.setGeometry(QtCore.QRect(60, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.C_Status = QtWidgets.QLabel(self.Printer_Settings)
        self.C_Status.setGeometry(QtCore.QRect(290, 160, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.C_Status.setFont(font)
        self.C_Status.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.C_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.C_Status.setObjectName("C_Status")
        self.P_Name = QtWidgets.QLabel(self.Printer_Settings)
        self.P_Name.setGeometry(QtCore.QRect(290, 70, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.P_Name.setFont(font)
        self.P_Name.setStyleSheet("QLabel {\n"
"    \n"
"background-color: rgb(31, 31, 31);\n"
"border: 1px solid white;\n"
"color: rgb(0, 170, 255);\n"
"border-radius: 10px;;\n"
"}\n"
"\n"
"")
        self.P_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.P_Name.setObjectName("P_Name")
        self.Edit_PB = QtWidgets.QPushButton(self.Printer_Settings)
        self.Edit_PB.setGeometry(QtCore.QRect(590, 70, 51, 41))
        self.Edit_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Edit_PB.setStyleSheet("QPushButton {\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.Edit_PB.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/NEW/Icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Edit_PB.setIcon(icon15)
        self.Edit_PB.setIconSize(QtCore.QSize(40, 40))
        self.Edit_PB.setObjectName("Edit_PB")
        self.label_2 = QtWidgets.QLabel(self.Printer_Settings)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 171, 41))
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
        self.X_Lable_6 = QtWidgets.QLabel(self.Printer_Settings)
        self.X_Lable_6.setGeometry(QtCore.QRect(250, 70, 21, 40))
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
"}\n"
"\n"
"")
        self.X_Lable_6.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_6.setObjectName("X_Lable_6")
        self.X_Lable_7 = QtWidgets.QLabel(self.Printer_Settings)
        self.X_Lable_7.setGeometry(QtCore.QRect(250, 160, 21, 40))
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
"\n"
"}\n"
"\n"
"")
        self.X_Lable_7.setAlignment(QtCore.Qt.AlignCenter)
        self.X_Lable_7.setObjectName("X_Lable_7")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/NEW/Icons/3d-printer-settings-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.Printer_Settings, icon16, "")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/NEW/Icons/gears.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Settings, icon17, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.File_PB.setText(_translate("MainWindow", "File Name"))
        self.Stop_TB.setText(_translate("MainWindow", "..."))
        self.TE_Box.setText(_translate("MainWindow", "2:23:45"))
        self.TR_Box.setText(_translate("MainWindow", "2:23:45"))
        self.Nozzle_1_Temp.setText(_translate("MainWindow", "200"))
        self.Nozzle_2_Temp.setText(_translate("MainWindow", "200"))
        self.Bed_Temp.setText(_translate("MainWindow", "200"))
        self.Time_E_Label_2.setText(_translate("MainWindow", ":"))
        self.Time_E_Label_3.setText(_translate("MainWindow", ":"))
        self.Time_E_Label.setText(_translate("MainWindow", "Time Elapsed"))
        self.Time_R_Label.setText(_translate("MainWindow", "Time Remaining"))
        self.Y_Up_Label.setText(_translate("MainWindow", "Y+"))
        self.Z_Down_Label.setText(_translate("MainWindow", "Z-"))
        self.X_Lable.setText(_translate("MainWindow", "X"))
        self.Y_Value.setText(_translate("MainWindow", "00"))
        self.X_Down_Label.setText(_translate("MainWindow", "X-"))
        self.X_Up_Label.setText(_translate("MainWindow", "X+"))
        self.Z_up_Label.setText(_translate("MainWindow", "Z+"))
        self.Y_Label.setText(_translate("MainWindow", "Y"))
        self.X_Value.setText(_translate("MainWindow", "00"))
        self.PB_01.setText(_translate("MainWindow", "0.1 mm"))
        self.Z_Label.setText(_translate("MainWindow", "Z"))
        self.Z_Value.setText(_translate("MainWindow", "00"))
        self.Y_Down_Label.setText(_translate("MainWindow", "Y-"))
        self.PB_100.setText(_translate("MainWindow", "100 mm"))
        self.PB_1.setText(_translate("MainWindow", "1 mm"))
        self.PB_10.setText(_translate("MainWindow", "10 mm"))
        self.X_Lable_3.setText(_translate("MainWindow", ":"))
        self.X_Lable_4.setText(_translate("MainWindow", ":"))
        self.X_Lable_5.setText(_translate("MainWindow", ":"))
        self.CT_Label.setText(_translate("MainWindow", "Actual"))
        self.CT_Label_3.setText(_translate("MainWindow", "Target"))
        self.ST_E1_Temp.setText(_translate("MainWindow", "0"))
        self.ST_Bed_Temp.setText(_translate("MainWindow", "0"))
        self.ST_E2_Temp.setText(_translate("MainWindow", "0"))
        self.ABS_Temp.setText(_translate("MainWindow", "ABS "))
        self.PLA_Temp.setText(_translate("MainWindow", " PLA "))
        self.PETG_Temp.setText(_translate("MainWindow", " PETG "))
        self.Cooldown_Temp.setText(_translate("MainWindow", "OFF"))
        self.CT_E1_Temp.setText(_translate("MainWindow", "200"))
        self.CT_E2_Temp.setText(_translate("MainWindow", "200"))
        self.CT_Bed_Temp.setText(_translate("MainWindow", "200"))
        self.USB_Print_PB.setText(_translate("MainWindow", "Print"))
        self.USB_Upload_PB.setText(_translate("MainWindow", "Upload "))
        self.USB_FD_PB.setText(_translate("MainWindow", "File Details"))
        self.FD_PB.setText(_translate("MainWindow", "File Details"))
        self.Print_PB.setText(_translate("MainWindow", "Print"))
        self.wifi_connect_PB.setText(_translate("MainWindow", "Connect"))
        self.Connect_PB.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Status "))
        self.C_Status.setText(_translate("MainWindow", "Online"))
        self.P_Name.setText(_translate("MainWindow", "Graviton"))
        self.label_2.setText(_translate("MainWindow", "Printer Name "))
        self.X_Lable_6.setText(_translate("MainWindow", ":"))
        self.X_Lable_7.setText(_translate("MainWindow", ":"))
        self.Start_TB.clicked.connect(self.pause_pressed)
        self.Stop_TB.clicked.connect(self.stop_pressed)
        self.PB_01.clicked.connect(self.set_value_01)
        self.PB_1.clicked.connect(self.set_value_1)
        self.PB_10.clicked.connect(self.set_value_10)
        self.PB_100.clicked.connect(self.set_value_100)
        self.X_Up_PB.clicked.connect(self.jog_x)
        self.X_Up_PB.clicked.connect(self.update_x_label)
        self.X_Down_PB.clicked.connect(self.jog_x1)
        self.X_Down_PB.clicked.connect(self.update_x2_label)
        self.Y_Up_PB.clicked.connect(self.jog_y)
        self.Y_Up_PB.clicked.connect(self.update_y_label)
        self.Y_Down_PB.clicked.connect(self.jog_y1)
        self.Y_Down_PB.clicked.connect(self.update_y2_label)
        self.Z_Up_PB.clicked.connect(self.jog_z)
        self.Z_Up_PB.clicked.connect(self.update_z_label)
        self.Z_Down_PB.clicked.connect(self.jog_z1)
        self.Z_Down_PB.clicked.connect(self.update_z2_label)
        self.ST_E1_Temp.clicked.connect(self.OpenKeypad)
        self.ST_Bed_Temp.clicked.connect(self.Open_Key_pad)
        self.Edit_PB.clicked.connect(self.openKeyboard)
        self.Connect_PB.clicked.connect(self.Gravity_Main)
        self.ABS_Temp.clicked.connect(self.set_ABS)
        self.PLA_Temp.clicked.connect(self.set_PLA)
        self.PETG_Temp.clicked.connect(self.set_PETG)
        self.Cooldown_Temp.clicked.connect(self.set_off)
        self.Back_PB.clicked.connect(self.file_back)
        self.File_Home_PB.clicked.connect(self.dir)
        self.listWidget_2.itemClicked.connect(self.selectionChanged)
        self.Print_PB.clicked.connect(self.print_file)
        self.USB_Back_PB.clicked.connect(self.usb_back)
        self.USB_File_Home_PB.clicked.connect(self.usb_dir)
        self.listWidget.itemClicked.connect(self.selection_usb_changed)
        self.XY_Home_PB.clicked.connect(self.XY_Home_Clicked)
        self.Z_Home_PB.clicked.connect(self.Z_Home_clicked)
        self.FD_PB.clicked.connect(partial(self.File_Details_file))
        self.USB_FD_PB.clicked.connect(partial(self.File_Details_usb))


    def OpenKeypad(self):
            """ THIS OPENS THE KEYPAD TO SET THE NOZZLE 1 TEMPERATURE """
            try:
                    self.key = QtWidgets.QDialog()
                    self.ui = Ui_Temperature_Setup_dialog()
                    self.ui.setupUi(self.key)
                    self.key.show()
                    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
                    self.key.setWindowFlags(flags)
                    if self.key.exec():
                            value = self.ui.Key_Value.text()
                    self.ST_E1_Temp.setText(value)
                    tool = int(self.ST_E1_Temp.text())
                    client.tool_target(tool)
            except Exception as ex:
                    print(ex)

    def Open_Keypad(self):
            """ THIS OPENS THE KEYPAD TO SET THE NOZZLE 2 TEMPERATURE """
            try:
                    self.key = QtWidgets.QDialog()
                    self.ui = Ui_Temperature_Setup_dialog()
                    self.ui.setupUi(self.key)
                    self.key.show()
                    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
                    self.key.setWindowFlags(flags)
                    if self.key.exec():
                            value = self.ui.Key_Value.text()
                    self.ST_E2_Temp.setText(value)
            except Exception as ex:
                    print(ex)

    def Open_Key_pad(self):
            """ THIS OPENS THE KEYPAD TO SET THE BED TEMPERATURE """
            try:
                    self.key = QtWidgets.QDialog()
                    self.ui = Ui_Temperature_Setup_dialog()
                    self.ui.setupUi(self.key)
                    self.key.show()
                    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
                    self.key.setWindowFlags(flags)
                    if self.key.exec():
                            value = self.ui.Key_Value.text()
                    self.ST_Bed_Temp.setText(value)
                    bed = int(self.ST_Bed_Temp.text())
                    client.bed_target(bed)
            except Exception as ex:
                    print(ex)

    def openKeyboard(self):
            """ THIS OPENS THE KEYBOARD TO CHANGE THE PRINTER'S NAME """
            try:
                    self.keyboard = QtWidgets.QDialog()
                    self.op = Ui_KEYPAD()
                    self.op.setupUi(self.keyboard)
                    self.keyboard.show()
                    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
                    self.keyboard.setWindowFlags(flags)
                    if self.keyboard.exec():
                            value4 = self.op.label.text()
                            self.P_Name.setText(str(value4))
            except Exception as ex:
                    print(ex)

    def Gravity_Main(self):
            """ THIS FUNCTION MAKES THE CONNECTION WITH OCTOPRINT AND RETRIEVES AND UPDATES ALL THE
            OBJECTS LIKE TEMPERATURE TIME PROGRESS ETC"""


            URL = file1.readline()
            PORT = '5000'
            APIKEY = '02E6D6E88D1F4700A47A1F9BDEDFF259'

            dir = '0'
            ui.update_n2temp(str(dir))
            """ui.hide_extruder2()"""
            try:
                    client = Ui_MainWindow.make_client(URL, APIKEY)
                    while True:
                            self.usb_dir()
                            state = client.printer()
                            temp_N1 = state['temperature']['tool0']['actual']
                            temp_bed = state['temperature']['bed']['actual']
                            printer_state = state['state']['text']
                            self.C_Status.setText(str(printer_state))
                            time = client.job_info()
                            time_elapsed = time['progress']['printTime']
                            time_remain = time['progress']['printTimeLeft']
                            file_nm = time['job']['file']['name']
                            est_time = time['job']['estimatedPrintTime']
                            progrs = time['progress']['completion']
                            file_details = client.files()
                            QtGui.QGuiApplication.processEvents()
                            ui.update_n1temp(str(temp_N1))
                            ui.update_bedtemp(str(temp_bed))
                            ui.update_timeelapsed(time_elapsed)
                            ui.update_timeremaining(time_remain)
                            ui.update_filename(str(file_nm))
                            ui.progress(progrs)
            except Exception as ex:
                    ui.Nozzle_1_Temp.setText("00")
                    ui.Nozzle_2_Temp.setText("00")
                    ui.Bed_Temp.setText("00")
                    ui.TE_Box.setText("00:00:00")
                    ui.TR_Box.setText("00:00:00")
                    ui.ProgressBar.setValue(0)
                    print(ex)

    def make_client(url, apikey):
            """ ESTABLISHES A CONNECTION TO OCTOPRINT THROUGH OCTOREST """

            try:
                    client = OctoRest(url=URL, apikey='02E6D6E88D1F4700A47A1F9BDEDFF259')
                    print("it is done")
                    return client
            except Exception as err:
                    print("not done")
                    print(err)

    def progress(self, a):
            """ UPDATES THE PROGRESS OF A PRINT """
            if a == None:
                    self.ProgressBar.setValue(0)
            else:
                    self.ProgressBar.setValue(a)

    def update_n1temp(self, x):
            """ UPDATES THE NOZZLE 1 TEMPERATURE"""
            self.Nozzle_1_Temp.setText(x)
            self.CT_E1_Temp.setText(x)

    def update_n2temp(self, x):
            """ UPDATES THE NOZZLE 2 TEMPERATURE """
            self.Nozzle_2_Temp.setText(x)

    def update_bedtemp(self, x):
            """ UPDATES THE BED TEMPERATURE """
            self.Bed_Temp.setText(x)
            self.CT_Bed_Temp.setText(x)

    def update_timeelapsed(self, x):
            """ UPDATES THE PRINT TIME ELAPSED """
            if x == None:
                    self.TE_Box.setText('00:00:00')
            else:
                    self.TE_Box.setText(str(datetime.timedelta(seconds=x)))

    def update_timeremaining(self, x):
            """ UPDATES THE PRINT TIME REMAINING """
            if x == None:
                    self.TR_Box.setText('00:00:00')
            else:
                    self.TR_Box.setText(str(datetime.timedelta(seconds=x)))



    def pause_pressed(self):
            """ PAUSES THE ONGOING PRINT OR STARTS IT IF ALREADY PAUSED """
            try:
                    client.pause()
            except Exception as ex:
                    print(ex)

    def stop_pressed(self):
            """ STOPS/CANCELS THE ON GOING PRINT"""
            try:
                    client.cancel()
            except Exception as ex:
                    print(ex)

    def XY_Home_Clicked(self):
            """ HOMES THE NOZZLE IN X-Y PLAIN"""
            try:
                    client.home()

            except Exception as ex:
                    print(ex)

    def Z_Home_clicked(self):
            """ HOMES THE NOZZLE IN Z PLAIN"""
            try:
                    client.home()
            except Exception as ex:
                    print(ex)

    def update_filename(self, x):
            """ UPDATES THE NAME OF THE FILE WHICH IS BEING PRINTED """
            self.File_PB.setText(x)

    def set_ABS(self):
            """ SETS NOZZLE AND BED TEMPERATURE FOR ABS PRINTING """
            try:
                    client.tool_target(230)
                    self.ST_E1_Temp.setText("230")
                    client.bed_target(110)
                    self.ST_Bed_Temp.setText("110")
            except Exception as ex:
                    print(ex)

    def set_PLA(self):
            """ SETS NOZZLE AND BED TEMPERATURE FOR PLA PRINTING """
            try:
                    client.tool_target(205)
                    self.ST_E1_Temp.setText("205")
                    client.bed_target(60)
                    self.ST_Bed_Temp.setText("60")
            except Exception as ex:
                    print(ex)

    def set_PETG(self):
            """ SETS NOZZLE AND BED TEMPERATURE FOR PETG PRINTING """
            try:
                    client.tool_target(230)
                    self.ST_E1_Temp.setText("230")
                    client.bed_target(80)
                    self.ST_Bed_Temp.setText("80")
            except Exception as ex:
                    print(ex)

    def set_off(self):
            """ SETS NOZZLE AND BED TEMPERATURE TO OFF STATE """
            try:
                    client.tool_target(0)
                    self.ST_E1_Temp.setText("0")
                    client.bed_target(0)
                    self.ST_Bed_Temp.setText("0")
            except Exception as ex:
                    print(ex)


    """ JOG CONTROLS CODE STARTS """
    global y
    y = 0

    def set_value_01(self):
            global y
            y = 0.1

    def set_value_1(self):
            global y
            y = 1.0

    def set_value_10(self):
            global y
            y = 10.0

    def set_value_100(self):
            global y
            y = 100.0

    def jog_x(self):
           try:
                   client.jog(y, 0, 0)
           except Exception as ex:
                   print(ex)

    def jog_x1(self):
            try:
                    client.jog(-y, 0, 0)
            except Exception as ex:
                    print(ex)

    def jog_y(self):
           try:
                   client.jog(0, y, 0)
           except Exception as ex:
                   print(ex)

    def jog_y1(self):
           try:
                   client.jog(0, -y, 0)

           except Exception as ex:
                   print(ex)

    def jog_z(self):
           try:
                   client.jog(0, 0, y)

           except Exception as ex:
                   print(ex)

    def jog_z1(self):
           try:
                   client.jog(0, 0, -y)
           except Exception as ex:
                   print(ex)


    """ JOG CONTROLS CODE ENDS """

    """UPDATE X Y Z LABEL ACCORDING TO JOG COMMANDS"""

    def update_x_label(self):
            label_value = float(self.X_Value.text())
            final_value = label_value + y
            self.X_Value.setText(str(final_value))

    def update_x2_label(self):
            label_value = float(self.X_Value.text())
            final_value = label_value - y
            self.X_Value.setText(str(final_value))

    def update_y_label(self):
            label_value = float(self.Y_Value.text())
            final_value = label_value + y
            self.Y_Value.setText(str(final_value))

    def update_y2_label(self):
            label_value = float(self.Y_Value.text())
            final_value = label_value - y
            self.Y_Value.setText(str(final_value))

    def update_z_label(self):
            label_value = float(self.Z_Value.text())
            final_value = label_value + y
            self.Z_Value.setText(str(final_value))

    def update_z2_label(self):
            label_value = float(self.Z_Value.text())
            final_value = label_value - y
            self.Z_Value.setText(str(final_value))


    """def hide_extruder2(self):
            try:
                    prntprofile = client.printer_profiles()
                    extrud_count = prntprofile['profiles']['_default']['extruder']['count']
                    print(extrud_count)
                    if extrud_count == 1:
                            self.ST_E2_Temp.hide()

                            self.CT_E2_Temp.hide()

                            self.label_6.hide()
                            self.label_4.hide()
                            self.Nozzle_2_Temp.hide()

                            self.CT_Bed_Temp.setGeometry(QtCore.QRect(220, 210, 110, 60))

                            self.ST_Bed_Temp.setGeometry(QtCore.QRect(380, 210, 120, 60))

                            self.label_18.setGeometry(QtCore.QRect(100, 210, 81, 71))
                            self.label_3.setGeometry(QtCore.QRect(20, 140, 81, 71))
                            self.Nozzle_1_Temp.setGeometry(QtCore.QRect(130, 140, 90, 60))
                            self.label_5.setGeometry(QtCore.QRect(25, 220, 81, 71))
                            self.Bed_Temp.setGeometry(QtCore.QRect(130, 220, 90, 60))

            except Exception as ex:
                    print(ex)"""

    """ FILES TAB CODE STARTS """

    global rdir
    rdir = ''
    global rdir1
    rdir1 = ''
    global rdir2
    rdir2 = 'C:\\Users'
    global b
    b = ''
    global rdir_usb
    rdir_usb = ''
    global rdir1_usb
    rdir1_usb = ''
    global rdir2_usb
    rdir2_usb = 'D:\\'
    global c
    c = ''

    def selection_usb_changed(self):
            global rdir_usb
            global rdir1_usb
            global rdir2_usb
            global c
            try:
                    a = self.listWidget.currentItem().text()
                    c = '\\' + a
                    rdir1_usb = rdir_usb + c
                    if os.path.isdir(rdir1_usb):
                            print(rdir1_usb)
                            self.listWidget.clear()
                            for filename in glob.iglob(rdir1_usb + '**/*', recursive=True):
                                    file = QtWidgets.QListWidgetItem(filename)
                                    file.setForeground(QColor('white'))
                                    file.setText(
                                            '{}'.format(str(os.path.basename(filename)), str(self.listWidget.count())))
                                    if os.path.isdir(filename):
                                            icon = QtGui.QIcon()
                                            icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/folder1.png"))
                                            file.setIcon(icon)
                                            font = QtGui.QFont()
                                            font.setPointSize(16)
                                            file.setFont(font)
                                            self.listWidget.addItem(file)
                                    if os.path.isfile(filename):
                                            icon1 = QtGui.QIcon()
                                            icon1.addPixmap(QtGui.QPixmap(":/NEW/Icons/file.png"))
                                            file.setIcon(icon1)
                                            font1 = QtGui.QFont()
                                            font1.setPointSize(16)
                                            file.setFont(font1)
                                            self.listWidget.addItem(file)
                                    rdir_usb = rdir1_usb
                    elif os.path.isfile(rdir1_usb):
                            print("\nIt is a normal file")
                            print(rdir1_usb)
            except Exception as ex:
                    print(ex)

    def usb_dir(self):
            global rdir1_usb
            rdir1 = ''
            global rdir_usb
            rdir_usb = 'D:\\'
            try:
                    self.listWidget.clear()
                    for filename in glob.iglob('D:\\' + '**/*', recursive=True):
                            file = QtWidgets.QListWidgetItem(filename)
                            file.setText('{}'.format(str(os.path.basename(filename)), str(self.listWidget.count())))
                            file.setForeground(QColor('white'))
                            if os.path.isdir(filename):
                                    icon = QtGui.QIcon()
                                    icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/folder1.png"))
                                    file.setIcon(icon)
                                    font = QtGui.QFont()
                                    font.setPointSize(16)
                                    file.setFont(font)
                                    self.listWidget.addItem(file)
                                    self.listWidget.setIconSize(QSize(80, 80))
                            if os.path.isfile(filename):
                                    icon1 = QtGui.QIcon()
                                    icon1.addPixmap(QtGui.QPixmap(":/NEW/Icons/file.png"))
                                    file.setIcon(icon1)
                                    font1 = QtGui.QFont()
                                    font1.setPointSize(16)
                                    file.setFont(font1)
                                    self.listWidget.addItem(file)
                                    self.listWidget.setIconSize(QSize(80, 80))

            except Exception as ex:
                    print(ex)

    def usb_back(self):
            global rdir2_usb
            global rdir1_usb
            global rdir_usb
            try:
                    if rdir1_usb == 'D:\\' or rdir_usb == 'D:\\':
                            self.usb_dir()
                    else:
                            self.listWidget.clearSelection()
                            c = os.path.basename(rdir1_usb)
                            if os.path.isfile(rdir1_usb):
                                    d = os.path.dirname(rdir1_usb)
                                    e = os.path.basename(d)
                                    rdir2_usb = rdir1_usb.replace('\\' + e + '\\' + c, "")
                            else:
                                    rdir2_usb = rdir1_usb.replace('\\' + c, "")
                            rdir1_usb = rdir2_usb
                            rdir_usb = rdir2_usb
                            print(rdir2_usb)
                            self.listWidget.clear()
                            for filename in glob.iglob(rdir2_usb + '**/*', recursive=True):
                                    file = QtWidgets.QListWidgetItem(filename)
                                    file.setForeground(QColor('white'))
                                    if os.path.isdir(filename):
                                            icon = QtGui.QIcon()
                                            icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/folder1.png"))
                                            font = QtGui.QFont()
                                            font.setPointSize(16)
                                            file.setFont(font)
                                            file.setIcon(icon)
                                            self.listWidget.addItem(file)
                                    if os.path.isfile(filename):
                                            icon1 = QtGui.QIcon()
                                            icon1.addPixmap(QtGui.QPixmap(":/NEW/Icons/file.png"))
                                            file.setIcon(icon1)
                                            font1 = QtGui.QFont()
                                            font1.setPointSize(16)
                                            file.setFont(font1)
                                            self.listWidget.addItem(file)
                                    file.setText('{}'.format(str(os.path.basename(filename)), str(self.listWidget.count())))
                                    self.listWidget.addItem(file)


            except Exception as ex:
                    print(ex)

    def selectionChanged(self):
            global rdir
            global rdir1
            global rdir2
            global b
            try:
                    a = self.listWidget_2.currentItem().text()
                    b = '\\' + a
                    rdir1 = rdir + b
                    if os.path.isdir(rdir1):
                            print(rdir1)
                            self.listWidget_2.clear()
                            for filename in glob.iglob(rdir1 + '**/*', recursive=True):
                                    file = QtWidgets.QListWidgetItem(filename)
                                    file.setForeground(QColor('white'))
                                    file.setText('{}'.format(str(os.path.basename(filename)),
                                                             str(self.listWidget_2.count())))
                                    if os.path.isdir(filename):
                                            icon = QtGui.QIcon()
                                            icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/folder1.png"))
                                            file.setIcon(icon)
                                            font = QtGui.QFont()
                                            font.setPointSize(16)
                                            file.setFont(font)
                                            self.listWidget_2.addItem(file)
                                    if os.path.isfile(filename):
                                            icon1 = QtGui.QIcon()
                                            icon1.addPixmap(QtGui.QPixmap(":/NEW/Icons/file.png"))
                                            file.setIcon(icon1)
                                            font1 = QtGui.QFont()
                                            font1.setPointSize(16)
                                            file.setFont(font1)
                                            self.listWidget_2.addItem(file)
                                    rdir = rdir1
                    elif os.path.isfile(rdir1):
                            print("\nIt is a normal file")
                            print(rdir1)
            except Exception as ex:
                    print(ex)

    def dir(self):
            global rdir1
            rdir1 = ''
            global rdir
            rdir = 'C:\\Users'
            try:
                    self.listWidget_2.clear()
                    for filename in glob.iglob('C:\\Users' + '**/*', recursive=True):
                            file = QtWidgets.QListWidgetItem(filename)
                            file.setText('{}'.format(str(os.path.basename(filename)), str(self.listWidget_2.count())))
                            file.setForeground(QColor('white'))
                            if os.path.isdir(filename):
                                    icon = QtGui.QIcon()
                                    icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/folder1.png"))
                                    file.setIcon(icon)
                                    font = QtGui.QFont()
                                    font.setPointSize(16)
                                    file.setFont(font)
                                    self.listWidget_2.addItem(file)
                                    self.listWidget_2.setIconSize(QSize(80, 80))
                            if os.path.isfile(filename):
                                    icon1 = QtGui.QIcon()
                                    icon1.addPixmap(QtGui.QPixmap(":/NEW/Icons/file.png"))
                                    file.setIcon(icon1)
                                    font1 = QtGui.QFont()
                                    font1.setPointSize(16)
                                    file.setFont(font1)
                                    self.listWidget_2.addItem(file)

            except Exception as ex:
                    print(ex)

    def file_back(self):
            global rdir2
            global rdir1
            global rdir

            try:
                    if rdir1 == 'C:\\Users' or rdir == 'C:\\Users':
                            self.dir()
                    else:
                            self.listWidget_2.clearSelection()
                            c = os.path.basename(rdir1)
                            if os.path.isfile(rdir1):
                                    d = os.path.dirname(rdir1)
                                    e = os.path.basename(d)
                                    rdir2 = rdir1.replace('\\' + e + '\\' + c, "")
                            else:
                                    rdir2 = rdir1.replace('\\' + c, "")

                            rdir1 = rdir2
                            rdir = rdir2
                            print(rdir2)
                            self.listWidget_2.clear()
                            for filename in glob.iglob(rdir2 + '**/*', recursive=True):
                                    file = QtWidgets.QListWidgetItem(filename)
                                    file.setForeground(QColor('white'))
                                    if os.path.isdir(filename):
                                            icon = QtGui.QIcon()
                                            icon.addPixmap(QtGui.QPixmap(":/NEW/Icons/folder1.png"))
                                            font = QtGui.QFont()
                                            font.setPointSize(16)
                                            file.setFont(font)
                                            file.setIcon(icon)
                                            self.listWidget_2.addItem(file)
                                    if os.path.isfile(filename):
                                            icon1 = QtGui.QIcon()
                                            icon1.addPixmap(QtGui.QPixmap(":/NEW/Icons/file.png"))
                                            file.setIcon(icon1)
                                            font1 = QtGui.QFont()
                                            font1.setPointSize(16)
                                            file.setFont(font1)
                                            self.listWidget_2.addItem(file)
                                    file.setText('{}'.format(str(os.path.basename(filename)),
                                                             str(self.listWidget_2.count())))
                                    self.listWidget_2.addItem(file)


            except Exception as ex:
                    print(ex)

    def File_Details_file(self):
            try:
                    global rdir1
                    self.filename = os.path.basename(rdir1)
                    self.extension = os.path.splitext(self.filename)[1][1:]
                    date1 = os.path.getmtime(rdir1)
                    self.date2 = datetime.datetime.fromtimestamp(date1)
                    size = os.path.getsize(rdir1)
                    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                            if size < 1024.0:
                                    self.s = "%3.1f %s" % (size, x)
                                    break
                            else:
                                    size /= 1024.0
                    self.file_details = QtWidgets.QDialog()
                    self.file_ui = Ui_Dialog(self.filename, self.date2, self.s, self.extension)
                    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
                    self.file_details.setWindowFlags(flags)
                    self.file_ui.setupUi(self.file_details)
                    self.file_details.show()
                    self.file_details.exec()

            except Exception as ex:
                    print(ex)


    def File_Details_usb(self):
            try:
                    global rdir1_usb
                    self.filename = os.path.basename(rdir1_usb)
                    self.extension = os.path.splitext(self.filename)[1][1:]
                    date1 = os.path.getmtime(rdir1_usb)
                    self.date2 = datetime.datetime.fromtimestamp(date1)
                    size = os.path.getsize(rdir1_usb)
                    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                            if size < 1024.0:
                                    self.s = "%3.1f %s" % (size, x)
                                    break
                            else:
                                    size /= 1024.0
                    self.file_details = QtWidgets.QDialog()
                    self.file_ui = Ui_Dialog(self.filename, self.date2, self.s, self.extension)
                    self.file_ui.setupUi(self.file_details)
                    self.file_details.show()
                    self.file_details.exec()


            except Exception as ex:
                    print(ex)




    def print_file(self):
            try:
                    global rdir1
                    filename = os.path.basename(rdir1)
                    client.upload(filename,rdir1)
                    client.select(filename)
            except Exception as ex:
                    print(ex)

""" FILES TAB CODE ENDS"""



if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        file1 = open("URL.txt")
        URL = file1.readline()
        PORT = '5000'
        APIKEY = '02E6D6E88D1F4700A47A1F9BDEDFF259'
        ui.dir()
        try:
                client = Ui_MainWindow.make_client(URL, APIKEY)
                ui.Gravity_Main()

        except Exception as ex:
                ui.Nozzle_1_Temp.setText("00")
                ui.Nozzle_2_Temp.setText("00")
                ui.Bed_Temp.setText("00")
                ui.TE_Box.setText("00:00:00")
                ui.TR_Box.setText("00:00:00")
                ui.CT_E1_Temp.setText("00")
                ui.CT_E2_Temp.setText("00")
                ui.CT_Bed_Temp.setText("00")
                ui.ProgressBar.setValue(0)
                print(ex)
        sys.exit(app.exec_())
