# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Leonard/AppData/Local/Temp/splash_screenYpQTsA.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(254, 121, 200, 255), stop:0.750 rgba(170, 85, 255, 30));\n"
"}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 135px;\n"
"    background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QtWidgets.QWidget(self.container)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 191, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelLoadingInfo = QtWidgets.QLabel(self.layoutWidget)
        self.labelLoadingInfo.setMinimumSize(QtCore.QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelLoadingInfo.setFont(font)
        self.labelLoadingInfo.setStyleSheet("QLabel{\n"
"    border-radius: 10px;    \n"
"    background-color: rgb(93, 93, 154);\n"
"    color: #FFFFFF;\n"
"    margin-left: 40px;\n"
"    margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoadingInfo.setObjectName("labelLoadingInfo")
        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)
        self.labelPercentage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(68)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelAplicationName_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName_3.setFont(font)
        self.labelAplicationName_3.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName_3.setObjectName("labelAplicationName_3")
        self.gridLayout_2.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.labelLoadingInfo.setText(_translate("SplashScreen", "loading..."))
        self.labelPercentage.setText(_translate("SplashScreen", "<html><head/><body><p> 0<span style=\" font-size:58pt; vertical-align:super;\">%</span></p></body></html>"))
        self.labelAplicationName_3.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:18pt;\">Welcome!</span></p></body></html>"))

import files_rc
