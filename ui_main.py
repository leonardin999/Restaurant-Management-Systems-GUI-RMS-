# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Leonard/AppData/Local/Temp/mainXILLgP.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 480)
        MainWindow.setMinimumSize(QtCore.QSize(760, 480))
        MainWindow.setMaximumSize(QtCore.QSize(760, 480))
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBar_Main = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBar_Main.setGeometry(QtCore.QRect(10, 80, 240, 240))
        self.circularProgressBar_Main.setStyleSheet("background-color: none;")
        self.circularProgressBar_Main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_Main.setObjectName("circularProgressBar_Main")
        self.circularProgressCPU = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularProgressCPU.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularProgressCPU.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressCPU.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressCPU.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressCPU.setObjectName("circularProgressCPU")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.circularContainer = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularContainer.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer.setObjectName("circularContainer")
        self.layoutWidget = QtWidgets.QWidget(self.circularContainer)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 156))
        self.layoutWidget.setObjectName("layoutWidget")
        self.infoLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.labelAplicationName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName.setFont(font)
        self.labelAplicationName.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName.setObjectName("labelAplicationName")
        self.infoLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)
        self.labelPercentageCPU = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelPercentageCPU.setFont(font)
        self.labelPercentageCPU.setStyleSheet("color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageCPU.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCPU.setIndent(-1)
        self.labelPercentageCPU.setObjectName("labelPercentageCPU")
        self.infoLayout.addWidget(self.labelPercentageCPU, 1, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.infoLayout.addWidget(self.labelCredits, 2, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgressCPU.raise_()
        self.circularContainer.raise_()
        self.circularProgressBar_Main_2 = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBar_Main_2.setGeometry(QtCore.QRect(260, 80, 240, 240))
        self.circularProgressBar_Main_2.setStyleSheet("background-color: none;")
        self.circularProgressBar_Main_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_Main_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_Main_2.setObjectName("circularProgressBar_Main_2")
        self.circularProgressGPU = QtWidgets.QFrame(self.circularProgressBar_Main_2)
        self.circularProgressGPU.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularProgressGPU.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.600 rgba(85, 255, 127, 255), stop:0.595 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressGPU.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressGPU.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressGPU.setObjectName("circularProgressGPU")
        self.circularBg_2 = QtWidgets.QFrame(self.circularProgressBar_Main_2)
        self.circularBg_2.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg_2.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_2.setObjectName("circularBg_2")
        self.circularContainer_2 = QtWidgets.QFrame(self.circularProgressBar_Main_2)
        self.circularContainer_2.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer_2.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_2.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_2.setObjectName("circularContainer_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.circularContainer_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 171, 156))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.infoLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.infoLayout_2.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_2.setObjectName("infoLayout_2")
        self.labelPercentageGPU = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelPercentageGPU.setFont(font)
        self.labelPercentageGPU.setStyleSheet("color: rgb(115, 255, 171); padding: 0px; background-color: none;")
        self.labelPercentageGPU.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageGPU.setIndent(-1)
        self.labelPercentageGPU.setObjectName("labelPercentageGPU")
        self.infoLayout_2.addWidget(self.labelPercentageGPU, 1, 0, 1, 1)
        self.labelCredits_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.labelCredits_2.setFont(font)
        self.labelCredits_2.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits_2.setObjectName("labelCredits_2")
        self.infoLayout_2.addWidget(self.labelCredits_2, 2, 0, 1, 1)
        self.labelAplicationName_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName_2.setFont(font)
        self.labelAplicationName_2.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName_2.setObjectName("labelAplicationName_2")
        self.infoLayout_2.addWidget(self.labelAplicationName_2, 0, 0, 1, 1)
        self.circularBg_2.raise_()
        self.circularProgressGPU.raise_()
        self.circularContainer_2.raise_()
        self.circularProgressBar_Main_3 = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBar_Main_3.setGeometry(QtCore.QRect(510, 80, 240, 240))
        self.circularProgressBar_Main_3.setStyleSheet("background-color: none;")
        self.circularProgressBar_Main_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_Main_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_Main_3.setObjectName("circularProgressBar_Main_3")
        self.circularProgressRAM = QtWidgets.QFrame(self.circularProgressBar_Main_3)
        self.circularProgressRAM.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularProgressRAM.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(255, 0, 127, 255), stop:0.745 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressRAM.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressRAM.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressRAM.setObjectName("circularProgressRAM")
        self.circularBg_3 = QtWidgets.QFrame(self.circularProgressBar_Main_3)
        self.circularBg_3.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg_3.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_3.setObjectName("circularBg_3")
        self.circularContainer_3 = QtWidgets.QFrame(self.circularProgressBar_Main_3)
        self.circularContainer_3.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer_3.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_3.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_3.setObjectName("circularContainer_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.circularContainer_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 171, 156))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.infoLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_3.setObjectName("infoLayout_3")
        self.labelAplicationName_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName_3.setFont(font)
        self.labelAplicationName_3.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName_3.setObjectName("labelAplicationName_3")
        self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)
        self.labelPercentageRAM = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelPercentageRAM.setFont(font)
        self.labelPercentageRAM.setStyleSheet("color: rgb(255, 44, 174); padding: 0px; background-color: none;")
        self.labelPercentageRAM.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageRAM.setIndent(-1)
        self.labelPercentageRAM.setObjectName("labelPercentageRAM")
        self.infoLayout_3.addWidget(self.labelPercentageRAM, 1, 0, 1, 1)
        self.labelCredits_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.labelCredits_3.setFont(font)
        self.labelCredits_3.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits_3.setObjectName("labelCredits_3")
        self.infoLayout_3.addWidget(self.labelCredits_3, 2, 0, 1, 1)
        self.circularBg_3.raise_()
        self.circularProgressRAM.raise_()
        self.circularContainer_3.raise_()
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(724, 20, 17, 17))
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(90, 410, 582, 40))
        self.label_13.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.btn_maximize = QtWidgets.QPushButton(self.centralwidget)
        self.btn_maximize.setGeometry(QtCore.QRect(670, 20, 17, 17))
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.btn_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minimize.setGeometry(QtCore.QRect(697, 20, 17, 17))
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.sliderCPU = QtWidgets.QSlider(self.centralwidget)
        self.sliderCPU.setGeometry(QtCore.QRect(50, 340, 161, 22))
        self.sliderCPU.setStyleSheet("/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.sliderCPU.setMaximum(100)
        self.sliderCPU.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCPU.setObjectName("sliderCPU")
        self.sliderGPU = QtWidgets.QSlider(self.centralwidget)
        self.sliderGPU.setGeometry(QtCore.QRect(300, 340, 161, 22))
        self.sliderGPU.setStyleSheet("/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 255, 127);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(115, 255, 148);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 195, 95);\n"
"}")
        self.sliderGPU.setMaximum(100)
        self.sliderGPU.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGPU.setObjectName("sliderGPU")
        self.sliderRAM = QtWidgets.QSlider(self.centralwidget)
        self.sliderRAM.setGeometry(QtCore.QRect(550, 340, 161, 22))
        self.sliderRAM.setStyleSheet("/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(255, 0, 127);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(255, 55, 155);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(199, 0, 99);\n"
"}\n"
"")
        self.sliderRAM.setMaximum(100)
        self.sliderRAM.setOrientation(QtCore.Qt.Horizontal)
        self.sliderRAM.setObjectName("sliderRAM")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelAplicationName.setText(_translate("MainWindow", "<strong>CPU</strong> USAGE"))
        self.labelPercentageCPU.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:50pt;\">60</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>"))
        self.labelCredits.setText(_translate("MainWindow", "<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">40º</span></p></body></html>"))
        self.labelPercentageGPU.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:50pt;\">40</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>"))
        self.labelCredits_2.setText(_translate("MainWindow", "<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">60º</span></p></body></html>"))
        self.labelAplicationName_2.setText(_translate("MainWindow", "<strong>GPU</strong> USAGE"))
        self.labelAplicationName_3.setText(_translate("MainWindow", "<strong>RAM</strong> USAGE"))
        self.labelPercentageRAM.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:50pt;\">25</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>"))
        self.labelCredits_3.setText(_translate("MainWindow", "<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">20º</span></p></body></html>"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label_13.setText(_translate("MainWindow", "\"If you control the code, you control the world.\""))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))

