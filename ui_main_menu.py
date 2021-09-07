# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Leonard/AppData/Local/Temp/main_menuZZtfBW.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ui_menu(object):
    def setupUi(self, ui_menu):
        ui_menu.setObjectName("ui_menu")
        ui_menu.resize(1450, 811)
        ui_menu.setMaximumSize(QtCore.QSize(1450, 820))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        ui_menu.setFont(font)
        ui_menu.setStyleSheet("QFontDatabase::addApplicationFont(\":/fonts/fonts/roboto-mono/RobotoMono-Bold.ttf\");")
        ui_menu.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(ui_menu)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(8, 10, 1421, 791))
        self.frame.setStyleSheet("QFram{border:2px solid rgb(65, 64, 66);border-radius:5px;margin-top: 1ex;color: ;background-color:transparent;} ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_close_3 = QtWidgets.QPushButton(self.frame)
        self.btn_close_3.setGeometry(QtCore.QRect(1390, 10, 17, 17))
        self.btn_close_3.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close_3.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close_3.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close_3.setText("")
        self.btn_close_3.setObjectName("btn_close_3")
        self.btn_minimize_3 = QtWidgets.QPushButton(self.frame)
        self.btn_minimize_3.setGeometry(QtCore.QRect(1363, 10, 17, 17))
        self.btn_minimize_3.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize_3.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize_3.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_minimize_3.setText("")
        self.btn_minimize_3.setObjectName("btn_minimize_3")
        self.btn_maximize_3 = QtWidgets.QPushButton(self.frame)
        self.btn_maximize_3.setGeometry(QtCore.QRect(1336, 10, 17, 17))
        self.btn_maximize_3.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize_3.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize_3.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_maximize_3.setText("")
        self.btn_maximize_3.setObjectName("btn_maximize_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(0, 10, 951, 201))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setGeometry(QtCore.QRect(10, 180, 940, 10))
        self.frame_2.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(680, 146, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(680, 60, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 621, 111))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(680, 104, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setGeometry(QtCore.QRect(10, 50, 940, 5))
        self.frame_3.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(670, 96, 280, 2))
        self.frame_4.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(670, 140, 280, 2))
        self.frame_6.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(860, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_3.setObjectName("label_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 320, 961, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Appetizer = QtWidgets.QWidget()
        self.Appetizer.setObjectName("Appetizer")
        self.frame_13 = QtWidgets.QFrame(self.Appetizer)
        self.frame_13.setGeometry(QtCore.QRect(0, 0, 951, 481))
        self.frame_13.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_10 = QtWidgets.QFrame(self.frame_13)
        self.frame_10.setGeometry(QtCore.QRect(10, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_10.setFont(font)
        self.frame_10.setStyleSheet("image:url(:/foods/images/salad.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_8 = QtWidgets.QFrame(self.frame_13)
        self.frame_8.setGeometry(QtCore.QRect(330, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet("image: url(:/foods/images/french_soup.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_14 = QtWidgets.QLabel(self.frame_13)
        self.label_14.setGeometry(QtCore.QRect(250, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.frame_13)
        self.label_17.setGeometry(QtCore.QRect(340, 450, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.frame_9 = QtWidgets.QFrame(self.frame_13)
        self.frame_9.setGeometry(QtCore.QRect(650, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_9.setFont(font)
        self.frame_9.setStyleSheet("image:url(:/foods/images/pumpkin.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_15 = QtWidgets.QLabel(self.frame_13)
        self.label_15.setGeometry(QtCore.QRect(20, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_8 = QtWidgets.QLabel(self.frame_13)
        self.label_8.setGeometry(QtCore.QRect(20, 210, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_13)
        self.label_9.setGeometry(QtCore.QRect(250, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_16 = QtWidgets.QLabel(self.frame_13)
        self.label_16.setGeometry(QtCore.QRect(570, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.frame_11 = QtWidgets.QFrame(self.frame_13)
        self.frame_11.setGeometry(QtCore.QRect(330, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_11.setFont(font)
        self.frame_11.setStyleSheet("image: url(:/foods/images/lasana.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_18 = QtWidgets.QLabel(self.frame_13)
        self.label_18.setGeometry(QtCore.QRect(660, 450, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.frame_12 = QtWidgets.QFrame(self.frame_13)
        self.frame_12.setGeometry(QtCore.QRect(650, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet("image: url(:/foods/images/burger.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        self.label_10.setGeometry(QtCore.QRect(570, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.frame_13)
        self.label_12.setGeometry(QtCore.QRect(890, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(self.frame_13)
        self.label_19.setGeometry(QtCore.QRect(890, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_13 = QtWidgets.QLabel(self.frame_13)
        self.label_13.setGeometry(QtCore.QRect(660, 210, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.frame_7 = QtWidgets.QFrame(self.frame_13)
        self.frame_7.setGeometry(QtCore.QRect(10, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet("image: url(:/foods/images/roll.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_11 = QtWidgets.QLabel(self.frame_13)
        self.label_11.setGeometry(QtCore.QRect(340, 210, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 10, 281, 221))
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_12.setGeometry(QtCore.QRect(330, 250, 281, 221))
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_13.setGeometry(QtCore.QRect(650, 250, 281, 221))
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 250, 281, 221))
        self.pushButton_14.setStyleSheet("")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_15.setGeometry(QtCore.QRect(650, 10, 281, 221))
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 10, 281, 221))
        self.pushButton_16.setStyleSheet("")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.frame_10.raise_()
        self.frame_8.raise_()
        self.label_14.raise_()
        self.label_17.raise_()
        self.frame_9.raise_()
        self.label_15.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_16.raise_()
        self.frame_11.raise_()
        self.label_18.raise_()
        self.frame_12.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        self.label_19.raise_()
        self.label_13.raise_()
        self.frame_7.raise_()
        self.label_11.raise_()
        self.pushButton_14.raise_()
        self.pushButton_16.raise_()
        self.pushButton_12.raise_()
        self.pushButton_11.raise_()
        self.pushButton_15.raise_()
        self.pushButton_13.raise_()
        self.stackedWidget.addWidget(self.Appetizer)
        self.Main_Course = QtWidgets.QWidget()
        self.Main_Course.setObjectName("Main_Course")
        self.frame_14 = QtWidgets.QFrame(self.Main_Course)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 951, 481))
        self.frame_14.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setGeometry(QtCore.QRect(10, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_15.setFont(font)
        self.frame_15.setStyleSheet("image:url(:/main dishes/images/grilled salmon.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setGeometry(QtCore.QRect(330, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_16.setFont(font)
        self.frame_16.setStyleSheet("image: url(:/main dishes/images/Eggplant Lasagna.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_20 = QtWidgets.QLabel(self.frame_14)
        self.label_20.setGeometry(QtCore.QRect(250, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_14)
        self.label_21.setGeometry(QtCore.QRect(340, 450, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.frame_17 = QtWidgets.QFrame(self.frame_14)
        self.frame_17.setGeometry(QtCore.QRect(650, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_17.setFont(font)
        self.frame_17.setStyleSheet("image:url(:/main dishes/images/Fish Filled.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_22 = QtWidgets.QLabel(self.frame_14)
        self.label_22.setGeometry(QtCore.QRect(20, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_14)
        self.label_23.setGeometry(QtCore.QRect(20, 210, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_14)
        self.label_24.setGeometry(QtCore.QRect(250, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_14)
        self.label_25.setGeometry(QtCore.QRect(570, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.frame_18 = QtWidgets.QFrame(self.frame_14)
        self.frame_18.setGeometry(QtCore.QRect(330, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_18.setFont(font)
        self.frame_18.setStyleSheet("image:url(:/main dishes/images/meatball pasta.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_26 = QtWidgets.QLabel(self.frame_14)
        self.label_26.setGeometry(QtCore.QRect(660, 450, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.frame_19 = QtWidgets.QFrame(self.frame_14)
        self.frame_19.setGeometry(QtCore.QRect(650, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_19.setFont(font)
        self.frame_19.setStyleSheet("image: url(:/main dishes/images/roasted beef.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_27 = QtWidgets.QLabel(self.frame_14)
        self.label_27.setGeometry(QtCore.QRect(570, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_14)
        self.label_28.setGeometry(QtCore.QRect(890, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_14)
        self.label_29.setGeometry(QtCore.QRect(890, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_14)
        self.label_30.setGeometry(QtCore.QRect(660, 210, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.frame_20 = QtWidgets.QFrame(self.frame_14)
        self.frame_20.setGeometry(QtCore.QRect(10, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_20.setFont(font)
        self.frame_20.setStyleSheet("image: url(:/main dishes/images/Chicken Parmesan.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_31 = QtWidgets.QLabel(self.frame_14)
        self.label_31.setGeometry(QtCore.QRect(340, 210, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_17.setGeometry(QtCore.QRect(330, 10, 281, 221))
        self.pushButton_17.setStyleSheet("")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_18.setGeometry(QtCore.QRect(330, 250, 281, 221))
        self.pushButton_18.setStyleSheet("")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_19.setGeometry(QtCore.QRect(650, 250, 281, 221))
        self.pushButton_19.setStyleSheet("")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 250, 281, 221))
        self.pushButton_20.setStyleSheet("")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_21.setGeometry(QtCore.QRect(650, 10, 281, 221))
        self.pushButton_21.setStyleSheet("")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 10, 281, 221))
        self.pushButton_22.setStyleSheet("")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_18.raise_()
        self.pushButton_21.raise_()
        self.pushButton_19.raise_()
        self.pushButton_17.raise_()
        self.frame_15.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.frame_17.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.frame_18.raise_()
        self.label_26.raise_()
        self.frame_19.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.frame_20.raise_()
        self.label_31.raise_()
        self.pushButton_22.raise_()
        self.pushButton_20.raise_()
        self.frame_16.raise_()
        self.stackedWidget.addWidget(self.Main_Course)
        self.Desserts = QtWidgets.QWidget()
        self.Desserts.setObjectName("Desserts")
        self.frame_21 = QtWidgets.QFrame(self.Desserts)
        self.frame_21.setGeometry(QtCore.QRect(0, 0, 951, 481))
        self.frame_21.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setGeometry(QtCore.QRect(10, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_22.setFont(font)
        self.frame_22.setStyleSheet("image:url(:/Desserts/images/Desserts/Crumb Cake.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        self.frame_23.setGeometry(QtCore.QRect(330, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_23.setFont(font)
        self.frame_23.setStyleSheet("image:url(:/Desserts/images/Desserts/Blueberries Ice Cream.jpg);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.label_32 = QtWidgets.QLabel(self.frame_21)
        self.label_32.setGeometry(QtCore.QRect(250, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_21)
        self.label_33.setGeometry(QtCore.QRect(340, 450, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.frame_24 = QtWidgets.QFrame(self.frame_21)
        self.frame_24.setGeometry(QtCore.QRect(650, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_24.setFont(font)
        self.frame_24.setStyleSheet("image:url(:/Desserts/images/Desserts/Chocolate Chip.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.label_34 = QtWidgets.QLabel(self.frame_21)
        self.label_34.setGeometry(QtCore.QRect(20, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_21)
        self.label_35.setGeometry(QtCore.QRect(20, 210, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_21)
        self.label_36.setGeometry(QtCore.QRect(250, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_21)
        self.label_37.setGeometry(QtCore.QRect(570, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.frame_25 = QtWidgets.QFrame(self.frame_21)
        self.frame_25.setGeometry(QtCore.QRect(330, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_25.setFont(font)
        self.frame_25.setStyleSheet("image:url(:/Desserts/images/Desserts/Fruits Salad.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.label_38 = QtWidgets.QLabel(self.frame_21)
        self.label_38.setGeometry(QtCore.QRect(660, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.frame_26 = QtWidgets.QFrame(self.frame_21)
        self.frame_26.setGeometry(QtCore.QRect(650, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_26.setFont(font)
        self.frame_26.setStyleSheet("image: url(:/Desserts/images/Desserts/Strawberry Smothie.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.label_39 = QtWidgets.QLabel(self.frame_21)
        self.label_39.setGeometry(QtCore.QRect(570, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_21)
        self.label_40.setGeometry(QtCore.QRect(890, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_21)
        self.label_41.setGeometry(QtCore.QRect(890, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_21)
        self.label_42.setGeometry(QtCore.QRect(660, 210, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.frame_27 = QtWidgets.QFrame(self.frame_21)
        self.frame_27.setGeometry(QtCore.QRect(10, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_27.setFont(font)
        self.frame_27.setStyleSheet("image: url(:/Desserts/images/Desserts/Apple Pie.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.label_43 = QtWidgets.QLabel(self.frame_21)
        self.label_43.setGeometry(QtCore.QRect(340, 210, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_23.setGeometry(QtCore.QRect(330, 10, 281, 221))
        self.pushButton_23.setStyleSheet("")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_24.setGeometry(QtCore.QRect(330, 250, 281, 221))
        self.pushButton_24.setStyleSheet("")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_25.setGeometry(QtCore.QRect(650, 250, 281, 221))
        self.pushButton_25.setStyleSheet("")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_26.setGeometry(QtCore.QRect(10, 250, 281, 221))
        self.pushButton_26.setStyleSheet("")
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_27.setGeometry(QtCore.QRect(650, 10, 281, 221))
        self.pushButton_27.setStyleSheet("")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_28.setGeometry(QtCore.QRect(10, 10, 281, 221))
        self.pushButton_28.setStyleSheet("")
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_26.raise_()
        self.pushButton_25.raise_()
        self.pushButton_28.raise_()
        self.pushButton_23.raise_()
        self.pushButton_27.raise_()
        self.pushButton_24.raise_()
        self.frame_22.raise_()
        self.frame_23.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.frame_24.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.frame_25.raise_()
        self.label_38.raise_()
        self.frame_26.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.frame_27.raise_()
        self.label_43.raise_()
        self.stackedWidget.addWidget(self.Desserts)
        self.Drinks = QtWidgets.QWidget()
        self.Drinks.setObjectName("Drinks")
        self.frame_28 = QtWidgets.QFrame(self.Drinks)
        self.frame_28.setGeometry(QtCore.QRect(0, 0, 951, 481))
        self.frame_28.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setGeometry(QtCore.QRect(10, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_29.setFont(font)
        self.frame_29.setStyleSheet("image:url(:/Drinks/images/Drinks/Whiskey.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.frame_30 = QtWidgets.QFrame(self.frame_28)
        self.frame_30.setGeometry(QtCore.QRect(330, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_30.setFont(font)
        self.frame_30.setStyleSheet("image:url(:/Drinks/images/Drinks/Mojito.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.label_44 = QtWidgets.QLabel(self.frame_28)
        self.label_44.setGeometry(QtCore.QRect(250, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_28)
        self.label_45.setGeometry(QtCore.QRect(340, 450, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.frame_31 = QtWidgets.QFrame(self.frame_28)
        self.frame_31.setGeometry(QtCore.QRect(650, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_31.setFont(font)
        self.frame_31.setStyleSheet("image:url(:/Drinks/images/Drinks/Red wine.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.label_46 = QtWidgets.QLabel(self.frame_28)
        self.label_46.setGeometry(QtCore.QRect(20, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.frame_28)
        self.label_47.setGeometry(QtCore.QRect(20, 210, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame_28)
        self.label_48.setGeometry(QtCore.QRect(250, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame_28)
        self.label_49.setGeometry(QtCore.QRect(570, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.frame_32 = QtWidgets.QFrame(self.frame_28)
        self.frame_32.setGeometry(QtCore.QRect(330, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_32.setFont(font)
        self.frame_32.setStyleSheet("image:url(:/Drinks/images/Drinks/beer.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.label_50 = QtWidgets.QLabel(self.frame_28)
        self.label_50.setGeometry(QtCore.QRect(660, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.frame_33 = QtWidgets.QFrame(self.frame_28)
        self.frame_33.setGeometry(QtCore.QRect(650, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_33.setFont(font)
        self.frame_33.setStyleSheet("image:url(:/Drinks/images/Drinks/soda.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.label_51 = QtWidgets.QLabel(self.frame_28)
        self.label_51.setGeometry(QtCore.QRect(570, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame_28)
        self.label_52.setGeometry(QtCore.QRect(890, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.frame_28)
        self.label_53.setGeometry(QtCore.QRect(890, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.frame_28)
        self.label_54.setGeometry(QtCore.QRect(660, 210, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.frame_34 = QtWidgets.QFrame(self.frame_28)
        self.frame_34.setGeometry(QtCore.QRect(10, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_34.setFont(font)
        self.frame_34.setStyleSheet("image:url(:/Drinks/images/Drinks/Lemon tea.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.label_55 = QtWidgets.QLabel(self.frame_28)
        self.label_55.setGeometry(QtCore.QRect(340, 210, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_29.setGeometry(QtCore.QRect(330, 10, 281, 221))
        self.pushButton_29.setStyleSheet("")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_30.setGeometry(QtCore.QRect(330, 250, 281, 221))
        self.pushButton_30.setStyleSheet("")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_31.setGeometry(QtCore.QRect(650, 250, 281, 221))
        self.pushButton_31.setStyleSheet("")
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 250, 281, 221))
        self.pushButton_32.setStyleSheet("")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_33.setGeometry(QtCore.QRect(650, 10, 281, 221))
        self.pushButton_33.setStyleSheet("")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_34.setGeometry(QtCore.QRect(10, 10, 281, 221))
        self.pushButton_34.setStyleSheet("")
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.frame_30.raise_()
        self.label_44.raise_()
        self.label_45.raise_()
        self.frame_31.raise_()
        self.label_46.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.label_49.raise_()
        self.frame_32.raise_()
        self.label_50.raise_()
        self.frame_33.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.label_54.raise_()
        self.frame_34.raise_()
        self.label_55.raise_()
        self.frame_29.raise_()
        self.pushButton_34.raise_()
        self.pushButton_31.raise_()
        self.pushButton_30.raise_()
        self.pushButton_32.raise_()
        self.pushButton_33.raise_()
        self.pushButton_29.raise_()
        self.stackedWidget.addWidget(self.Drinks)
        self.Special_Menus = QtWidgets.QWidget()
        self.Special_Menus.setObjectName("Special_Menus")
        self.frame_35 = QtWidgets.QFrame(self.Special_Menus)
        self.frame_35.setGeometry(QtCore.QRect(0, 0, 951, 481))
        self.frame_35.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"    border: 3px solid rgb(65, 64, 66);\n"
"    border-radius: 5px;\n"
"}")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.frame_36 = QtWidgets.QFrame(self.frame_35)
        self.frame_36.setGeometry(QtCore.QRect(10, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_36.setFont(font)
        self.frame_36.setStyleSheet("image:url(:/Special Menus/images/Special Menus/Ricotta Pie.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.frame_37 = QtWidgets.QFrame(self.frame_35)
        self.frame_37.setGeometry(QtCore.QRect(330, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_37.setFont(font)
        self.frame_37.setStyleSheet("image:url(:/Special Menus/images/Special Menus/Chicken Ranch.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.label_56 = QtWidgets.QLabel(self.frame_35)
        self.label_56.setGeometry(QtCore.QRect(250, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.frame_35)
        self.label_57.setGeometry(QtCore.QRect(340, 450, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.frame_38 = QtWidgets.QFrame(self.frame_35)
        self.frame_38.setGeometry(QtCore.QRect(650, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_38.setFont(font)
        self.frame_38.setStyleSheet("image:url(:/Special Menus/images/Special Menus/Mushroom Pie.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.label_58 = QtWidgets.QLabel(self.frame_35)
        self.label_58.setGeometry(QtCore.QRect(20, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.frame_35)
        self.label_59.setGeometry(QtCore.QRect(20, 210, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frame_35)
        self.label_60.setGeometry(QtCore.QRect(250, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.frame_35)
        self.label_61.setGeometry(QtCore.QRect(570, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.frame_39 = QtWidgets.QFrame(self.frame_35)
        self.frame_39.setGeometry(QtCore.QRect(330, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_39.setFont(font)
        self.frame_39.setStyleSheet("image:url(:/Special Menus/images/Special Menus/Tenderloin Steak.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.label_62 = QtWidgets.QLabel(self.frame_35)
        self.label_62.setGeometry(QtCore.QRect(660, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.frame_40 = QtWidgets.QFrame(self.frame_35)
        self.frame_40.setGeometry(QtCore.QRect(650, 250, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_40.setFont(font)
        self.frame_40.setStyleSheet("image:url(:/Special Menus/images/Special Menus/Vegetarian Curry.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.label_63 = QtWidgets.QLabel(self.frame_35)
        self.label_63.setGeometry(QtCore.QRect(570, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.frame_35)
        self.label_64.setGeometry(QtCore.QRect(890, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.frame_35)
        self.label_65.setGeometry(QtCore.QRect(890, 450, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Light")
        font.setPointSize(10)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.frame_35)
        self.label_66.setGeometry(QtCore.QRect(660, 210, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.frame_41 = QtWidgets.QFrame(self.frame_35)
        self.frame_41.setGeometry(QtCore.QRect(10, 10, 281, 191))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        self.frame_41.setFont(font)
        self.frame_41.setStyleSheet("image:url(:/Special Menus/images/Special Menus/Bruschetta Salad.png);\n"
"border: 3px solid rgb(65, 64, 66);\n"
"border-radius: 5px;")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.label_67 = QtWidgets.QLabel(self.frame_35)
        self.label_67.setGeometry(QtCore.QRect(340, 210, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_35.setGeometry(QtCore.QRect(330, 10, 281, 221))
        self.pushButton_35.setStyleSheet("")
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_36.setGeometry(QtCore.QRect(330, 250, 281, 221))
        self.pushButton_36.setStyleSheet("")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_37.setGeometry(QtCore.QRect(650, 250, 281, 221))
        self.pushButton_37.setStyleSheet("")
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_38.setGeometry(QtCore.QRect(10, 250, 281, 221))
        self.pushButton_38.setStyleSheet("")
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_39.setGeometry(QtCore.QRect(650, 10, 281, 221))
        self.pushButton_39.setStyleSheet("")
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_40.setGeometry(QtCore.QRect(10, 10, 281, 221))
        self.pushButton_40.setStyleSheet("")
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.frame_36.raise_()
        self.frame_37.raise_()
        self.label_56.raise_()
        self.label_57.raise_()
        self.frame_38.raise_()
        self.label_58.raise_()
        self.label_59.raise_()
        self.label_60.raise_()
        self.label_61.raise_()
        self.frame_39.raise_()
        self.label_62.raise_()
        self.frame_40.raise_()
        self.label_63.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.label_66.raise_()
        self.frame_41.raise_()
        self.label_67.raise_()
        self.pushButton_40.raise_()
        self.pushButton_35.raise_()
        self.pushButton_39.raise_()
        self.pushButton_38.raise_()
        self.pushButton_36.raise_()
        self.pushButton_37.raise_()
        self.stackedWidget.addWidget(self.Special_Menus)
        self.SideDishes = QtWidgets.QWidget()
        self.SideDishes.setObjectName("SideDishes")
        self.frame_42 = QtWidgets.QFrame(self.SideDishes)
        self.frame_42.setGeometry(QtCore.QRect(0, 10, 951, 471))
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.frame_43 = QtWidgets.QFrame(self.frame_42)
        self.frame_43.setGeometry(QtCore.QRect(10, 20, 411, 181))
        self.frame_43.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.label_70 = QtWidgets.QLabel(self.frame_43)
        self.label_70.setGeometry(QtCore.QRect(370, 70, 41, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond Light")
        font.setPointSize(12)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.label_68 = QtWidgets.QLabel(self.frame_43)
        self.label_68.setGeometry(QtCore.QRect(10, 14, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.frame_43)
        self.label_69.setGeometry(QtCore.QRect(10, 44, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(12)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_43)
        self.pushButton_41.setGeometry(QtCore.QRect(0, 0, 411, 181))
        self.pushButton_41.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.frame_44 = QtWidgets.QFrame(self.frame_42)
        self.frame_44.setGeometry(QtCore.QRect(10, 240, 411, 181))
        self.frame_44.setStyleSheet("QPushButton:{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.label_71 = QtWidgets.QLabel(self.frame_44)
        self.label_71.setGeometry(QtCore.QRect(370, 70, 41, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond Light")
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.frame_44)
        self.label_72.setGeometry(QtCore.QRect(10, 14, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.frame_44)
        self.label_73.setGeometry(QtCore.QRect(10, 44, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(12)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_44)
        self.pushButton_42.setGeometry(QtCore.QRect(0, 0, 411, 181))
        self.pushButton_42.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_42.raise_()
        self.label_71.raise_()
        self.label_72.raise_()
        self.label_73.raise_()
        self.frame_45 = QtWidgets.QFrame(self.frame_42)
        self.frame_45.setGeometry(QtCore.QRect(440, 80, 501, 381))
        self.frame_45.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid rpg(0,0,0);")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.label_78 = QtWidgets.QLabel(self.frame_45)
        self.label_78.setGeometry(QtCore.QRect(10, 360, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(6)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;\n"
"border: 2px solid transparent;")
        self.label_78.setObjectName("label_78")
        self.label_75 = QtWidgets.QLabel(self.frame_45)
        self.label_75.setGeometry(QtCore.QRect(2, 4, 221, 321))
        self.label_75.setStyleSheet("image: url(:/side dishes/images/side dishes/crump.png);\n"
"border-color: transparent;\n"
"")
        self.label_75.setText("")
        self.label_75.setObjectName("label_75")
        self.label_77 = QtWidgets.QLabel(self.frame_45)
        self.label_77.setGeometry(QtCore.QRect(80, 340, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(8)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;\n"
"border: 2px solid transparent;")
        self.label_77.setObjectName("label_77")
        self.label_74 = QtWidgets.QLabel(self.frame_45)
        self.label_74.setGeometry(QtCore.QRect(217, 4, 281, 191))
        self.label_74.setStyleSheet("image: url(:/side dishes/images/side dishes/Fried_chicken.png);\n"
"border-color: transparent;")
        self.label_74.setText("")
        self.label_74.setObjectName("label_74")
        self.label_76 = QtWidgets.QLabel(self.frame_45)
        self.label_76.setGeometry(QtCore.QRect(217, 189, 281, 191))
        self.label_76.setStyleSheet("image: url(:/side dishes/images/side dishes/crisps.png);\n"
"border-color: transparent;")
        self.label_76.setText("")
        self.label_76.setObjectName("label_76")
        self.frame_46 = QtWidgets.QFrame(self.frame_45)
        self.frame_46.setGeometry(QtCore.QRect(10, 320, 200, 2))
        self.frame_46.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.frame_47 = QtWidgets.QFrame(self.frame_42)
        self.frame_47.setGeometry(QtCore.QRect(14, 220, 405, 5))
        self.frame_47.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.label_86 = QtWidgets.QLabel(self.frame_42)
        self.label_86.setGeometry(QtCore.QRect(460, 30, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("border: 2px solid rgb(65, 64, 66);\n"
"background-color: rgb(65, 64, 66);\n"
"color: rgb(240, 235, 225);")
        self.label_86.setObjectName("label_86")
        self.stackedWidget.addWidget(self.SideDishes)
        self.More = QtWidgets.QWidget()
        self.More.setObjectName("More")
        self.frame_58 = QtWidgets.QFrame(self.More)
        self.frame_58.setGeometry(QtCore.QRect(0, 0, 951, 471))
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.frame_105 = QtWidgets.QFrame(self.frame_58)
        self.frame_105.setGeometry(QtCore.QRect(10, 20, 411, 131))
        self.frame_105.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.frame_105.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_105.setObjectName("frame_105")
        self.label_183 = QtWidgets.QLabel(self.frame_105)
        self.label_183.setGeometry(QtCore.QRect(350, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond Light")
        font.setPointSize(15)
        self.label_183.setFont(font)
        self.label_183.setObjectName("label_183")
        self.label_184 = QtWidgets.QLabel(self.frame_105)
        self.label_184.setGeometry(QtCore.QRect(10, 14, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.label_184.setFont(font)
        self.label_184.setObjectName("label_184")
        self.label_185 = QtWidgets.QLabel(self.frame_105)
        self.label_185.setGeometry(QtCore.QRect(10, 50, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_185.setFont(font)
        self.label_185.setObjectName("label_185")
        self.pushButton_79 = QtWidgets.QPushButton(self.frame_105)
        self.pushButton_79.setGeometry(QtCore.QRect(0, 0, 411, 131))
        self.pushButton_79.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.pushButton_79.setText("")
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_79.raise_()
        self.label_183.raise_()
        self.label_184.raise_()
        self.label_185.raise_()
        self.frame_107 = QtWidgets.QFrame(self.frame_58)
        self.frame_107.setGeometry(QtCore.QRect(440, 80, 501, 381))
        self.frame_107.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid rpg(0,0,0);")
        self.frame_107.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_107.setObjectName("frame_107")
        self.label_189 = QtWidgets.QLabel(self.frame_107)
        self.label_189.setGeometry(QtCore.QRect(10, 360, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(6)
        self.label_189.setFont(font)
        self.label_189.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;\n"
"border: 2px solid transparent;")
        self.label_189.setObjectName("label_189")
        self.label_190 = QtWidgets.QLabel(self.frame_107)
        self.label_190.setGeometry(QtCore.QRect(2, 4, 221, 321))
        self.label_190.setStyleSheet("image: url(:/side dishes/images/side dishes/sushi.png);\n"
"border-color: transparent;\n"
"")
        self.label_190.setText("")
        self.label_190.setObjectName("label_190")
        self.label_191 = QtWidgets.QLabel(self.frame_107)
        self.label_191.setGeometry(QtCore.QRect(80, 340, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(8)
        self.label_191.setFont(font)
        self.label_191.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;\n"
"border: 2px solid transparent;")
        self.label_191.setObjectName("label_191")
        self.label_192 = QtWidgets.QLabel(self.frame_107)
        self.label_192.setGeometry(QtCore.QRect(217, 2, 281, 161))
        self.label_192.setStyleSheet("image:url(:/side dishes/images/side dishes/Shrimp.png);\n"
"border-color: transparent;")
        self.label_192.setText("")
        self.label_192.setObjectName("label_192")
        self.label_193 = QtWidgets.QLabel(self.frame_107)
        self.label_193.setGeometry(QtCore.QRect(218, 157, 281, 191))
        self.label_193.setStyleSheet("image:url(:/side dishes/images/side dishes/rices.png);\n"
"border-color: transparent;")
        self.label_193.setText("")
        self.label_193.setObjectName("label_193")
        self.frame_108 = QtWidgets.QFrame(self.frame_107)
        self.frame_108.setGeometry(QtCore.QRect(10, 330, 200, 2))
        self.frame_108.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_108.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_108.setObjectName("frame_108")
        self.frame_109 = QtWidgets.QFrame(self.frame_58)
        self.frame_109.setGeometry(QtCore.QRect(14, 160, 405, 5))
        self.frame_109.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_109.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_109.setObjectName("frame_109")
        self.label_194 = QtWidgets.QLabel(self.frame_58)
        self.label_194.setGeometry(QtCore.QRect(446, 30, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.label_194.setFont(font)
        self.label_194.setStyleSheet("border: 2px solid rgb(65, 64, 66);    \n"
"background-color: rgb(65, 64, 66);\n"
"color: rgb(240, 235, 225);")
        self.label_194.setObjectName("label_194")
        self.frame_106 = QtWidgets.QFrame(self.frame_58)
        self.frame_106.setGeometry(QtCore.QRect(10, 180, 411, 131))
        self.frame_106.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.frame_106.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_106.setObjectName("frame_106")
        self.label_186 = QtWidgets.QLabel(self.frame_106)
        self.label_186.setGeometry(QtCore.QRect(350, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond Light")
        font.setPointSize(15)
        self.label_186.setFont(font)
        self.label_186.setObjectName("label_186")
        self.label_187 = QtWidgets.QLabel(self.frame_106)
        self.label_187.setGeometry(QtCore.QRect(10, 14, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.label_187.setFont(font)
        self.label_187.setObjectName("label_187")
        self.label_188 = QtWidgets.QLabel(self.frame_106)
        self.label_188.setGeometry(QtCore.QRect(10, 50, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_188.setFont(font)
        self.label_188.setObjectName("label_188")
        self.pushButton_80 = QtWidgets.QPushButton(self.frame_106)
        self.pushButton_80.setGeometry(QtCore.QRect(0, 0, 411, 131))
        self.pushButton_80.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.pushButton_80.setText("")
        self.pushButton_80.setObjectName("pushButton_80")
        self.frame_110 = QtWidgets.QFrame(self.frame_58)
        self.frame_110.setGeometry(QtCore.QRect(10, 320, 405, 5))
        self.frame_110.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_110.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_110.setObjectName("frame_110")
        self.frame_111 = QtWidgets.QFrame(self.frame_58)
        self.frame_111.setGeometry(QtCore.QRect(10, 330, 411, 131))
        self.frame_111.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.frame_111.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_111.setObjectName("frame_111")
        self.label_195 = QtWidgets.QLabel(self.frame_111)
        self.label_195.setGeometry(QtCore.QRect(350, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond Light")
        font.setPointSize(15)
        self.label_195.setFont(font)
        self.label_195.setObjectName("label_195")
        self.label_196 = QtWidgets.QLabel(self.frame_111)
        self.label_196.setGeometry(QtCore.QRect(10, 14, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.label_196.setFont(font)
        self.label_196.setObjectName("label_196")
        self.label_197 = QtWidgets.QLabel(self.frame_111)
        self.label_197.setGeometry(QtCore.QRect(10, 50, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.label_197.setFont(font)
        self.label_197.setObjectName("label_197")
        self.pushButton_81 = QtWidgets.QPushButton(self.frame_111)
        self.pushButton_81.setGeometry(QtCore.QRect(0, 10, 411, 121))
        self.pushButton_81.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"border: 3px solid rgb(59, 112, 112);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(59, 112, 112);\n"
"}")
        self.pushButton_81.setText("")
        self.pushButton_81.setObjectName("pushButton_81")
        self.stackedWidget.addWidget(self.More)
        self.frame_48 = QtWidgets.QFrame(self.frame)
        self.frame_48.setGeometry(QtCore.QRect(0, 220, 951, 51))
        self.frame_48.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.pushButton = QtWidgets.QPushButton(self.frame_48)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    border-top-left-radius: 15px;    \n"
"    border-bottom-left-radius: 15px;\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    border-top-left-radius: 15px;    \n"
"    border-bottom-left-radius: 15px;\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 0, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 0, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 0, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 0, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 0, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 0, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_8.setGeometry(QtCore.QRect(890, 0, 51, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    border-top-right-radius: 15px;    \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    border-top-left-radius: 15px;    \n"
"    border-bottom-left-radius: 15px;\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_8.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-chevron-double-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_48)
        self.pushButton_9.setGeometry(QtCore.QRect(800, 0, 91, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(90, 280, 841, 31))
        self.textEdit.setStyleSheet("    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    color: rgb(65, 64, 66);\n"
"    border-radius: 10px;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 280, 91, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: transparent;\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(953, 40, 461, 741))
        self.groupBox.setStyleSheet("QGroupBox{border:2px solid  rgb(65, 64, 66);border-radius:5px;margin-top: 1ex;color: ;background-color:rgb(240, 235, 225);} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top left;padding:0 3px;}\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(5, 80, 451, 251))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(200, 200))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_45 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_45.setGeometry(QtCore.QRect(370, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_45.setObjectName("pushButton_45")
        self.frame_52 = QtWidgets.QFrame(self.groupBox)
        self.frame_52.setGeometry(QtCore.QRect(20, 41, 420, 2))
        self.frame_52.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.label_87 = QtWidgets.QLabel(self.groupBox)
        self.label_87.setGeometry(QtCore.QRect(20, 45, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_87.setObjectName("label_87")
        self.frame_53 = QtWidgets.QFrame(self.groupBox)
        self.frame_53.setGeometry(QtCore.QRect(10, 80, 440, 2))
        self.frame_53.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.frame_54 = QtWidgets.QFrame(self.groupBox)
        self.frame_54.setGeometry(QtCore.QRect(10, 329, 440, 2))
        self.frame_54.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.pushButton_48 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_48.setGeometry(QtCore.QRect(20, 669, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    border-radius: 15px;    \n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 235, 225);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    border-radius: 15px;    \n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.pushButton_48.setObjectName("pushButton_48")
        self.label_94 = QtWidgets.QLabel(self.groupBox)
        self.label_94.setGeometry(QtCore.QRect(20, 330, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_94.setObjectName("label_94")
        self.frame_64 = QtWidgets.QFrame(self.groupBox)
        self.frame_64.setGeometry(QtCore.QRect(10, 350, 431, 71))
        self.frame_64.setStyleSheet("QPushButton {\n"
"    background-color: rgb(193, 193, 193);\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    color: rgb(65, 64, 66);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(65, 64, 66);\n"
"    background-color: rgb(65, 64, 66);\n"
"    color: rgb(240, 235, 225);\n"
"}")
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.pushButton_58 = QtWidgets.QPushButton(self.frame_64)
        self.pushButton_58.setGeometry(QtCore.QRect(290, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setStyleSheet("")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.frame_64)
        self.pushButton_59.setGeometry(QtCore.QRect(100, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setStyleSheet("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.frame_64)
        self.pushButton_60.setGeometry(QtCore.QRect(200, 10, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setStyleSheet("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.frame_64)
        self.pushButton_61.setGeometry(QtCore.QRect(9, 10, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setStyleSheet("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.label_95 = QtWidgets.QLabel(self.groupBox)
        self.label_95.setGeometry(QtCore.QRect(20, 480, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_95.setFont(font)
        self.label_95.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_95.setObjectName("label_95")
        self.frame_65 = QtWidgets.QFrame(self.groupBox)
        self.frame_65.setGeometry(QtCore.QRect(20, 500, 421, 161))
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.label_90 = QtWidgets.QLabel(self.frame_65)
        self.label_90.setGeometry(QtCore.QRect(340, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("color: rgb(144, 144, 144);\n"
"background-color:transparent;")
        self.label_90.setObjectName("label_90")
        self.label_89 = QtWidgets.QLabel(self.frame_65)
        self.label_89.setGeometry(QtCore.QRect(20, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("color: rgb(144, 144, 144);\n"
"background-color:transparent;")
        self.label_89.setObjectName("label_89")
        self.frame_59 = QtWidgets.QFrame(self.frame_65)
        self.frame_59.setGeometry(QtCore.QRect(10, 40, 400, 2))
        self.frame_59.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.label_96 = QtWidgets.QLabel(self.frame_65)
        self.label_96.setGeometry(QtCore.QRect(340, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("color: rgb(144, 144, 144);\n"
"background-color:transparent;")
        self.label_96.setObjectName("label_96")
        self.label_97 = QtWidgets.QLabel(self.frame_65)
        self.label_97.setGeometry(QtCore.QRect(20, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_97.setFont(font)
        self.label_97.setStyleSheet("color: rgb(144, 144, 144);\n"
"background-color:transparent;")
        self.label_97.setObjectName("label_97")
        self.frame_66 = QtWidgets.QFrame(self.frame_65)
        self.frame_66.setGeometry(QtCore.QRect(10, 90, 400, 2))
        self.frame_66.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.label_98 = QtWidgets.QLabel(self.frame_65)
        self.label_98.setGeometry(QtCore.QRect(340, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("color: rgb(144, 144, 144);\n"
"background-color:transparent;")
        self.label_98.setObjectName("label_98")
        self.frame_67 = QtWidgets.QFrame(self.frame_65)
        self.frame_67.setGeometry(QtCore.QRect(10, 140, 400, 2))
        self.frame_67.setStyleSheet("background-color: rgb(65, 64, 66);")
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.label_99 = QtWidgets.QLabel(self.frame_65)
        self.label_99.setGeometry(QtCore.QRect(20, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_99.setFont(font)
        self.label_99.setStyleSheet("color: rgb(144, 144, 144);\n"
"background-color:transparent;")
        self.label_99.setObjectName("label_99")
        self.frame_68 = QtWidgets.QFrame(self.groupBox)
        self.frame_68.setGeometry(QtCore.QRect(10, 420, 431, 61))
        self.frame_68.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.label_100 = QtWidgets.QLabel(self.frame_68)
        self.label_100.setGeometry(QtCore.QRect(10, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("color: rgb(65, 64, 66);\n"
"background-color:transparent;")
        self.label_100.setObjectName("label_100")
        self.comboBox = QtWidgets.QComboBox(self.frame_68)
        self.comboBox.setGeometry(QtCore.QRect(260, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    background-color: rgb(240, 235, 225);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(240, 235, 225);\n"
"    padding: 5px;\n"
"    padding-left: 20px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(65, 64, 66);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color:  rgb(65, 64, 66);\n"
"    background-color: rgb(240, 235, 225);\n"
"    padding: 10px;\n"
"    selection-background-color:  rgb(240, 235, 225);\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        ui_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(ui_menu)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(ui_menu)

    def retranslateUi(self, ui_menu):
        _translate = QtCore.QCoreApplication.translate
        ui_menu.setWindowTitle(_translate("ui_menu", "MainWindow"))
        self.btn_close_3.setToolTip(_translate("ui_menu", "Close"))
        self.btn_minimize_3.setToolTip(_translate("ui_menu", "Minimize"))
        self.btn_maximize_3.setToolTip(_translate("ui_menu", "Maximize"))
        self.label_2.setText(_translate("ui_menu", "123 Anywhere St., Any City,ST 12345"))
        self.label_7.setText(_translate("ui_menu", "Dine in"))
        self.label.setText(_translate("ui_menu", "L\'s RESTAURANT"))
        self.label_5.setText(_translate("ui_menu", "Opening Hours"))
        self.label_4.setText(_translate("ui_menu", "FOOD MENU"))
        self.label_6.setText(_translate("ui_menu", "07.30 - 23.00"))
        self.label_3.setText(_translate("ui_menu", "Est 2021"))
        self.label_14.setText(_translate("ui_menu", "$15"))
        self.label_17.setText(_translate("ui_menu", "MEAT LASAGNA:"))
        self.label_15.setText(_translate("ui_menu", "CAESER SALAD:"))
        self.label_8.setText(_translate("ui_menu", "SPRING ROLLS:"))
        self.label_9.setText(_translate("ui_menu", "$15"))
        self.label_16.setText(_translate("ui_menu", "$22"))
        self.label_18.setText(_translate("ui_menu", "BURGER"))
        self.label_10.setText(_translate("ui_menu", "$20"))
        self.label_12.setText(_translate("ui_menu", "$17"))
        self.label_19.setText(_translate("ui_menu", "$10"))
        self.label_13.setText(_translate("ui_menu", "PUMPKIN SOUP:"))
        self.label_11.setText(_translate("ui_menu", "FRENCH ONION SOUP:"))
        self.label_20.setText(_translate("ui_menu", "$35"))
        self.label_21.setText(_translate("ui_menu", "MEATBALL PASTA:"))
        self.label_22.setText(_translate("ui_menu", "GRILLED SALMON:"))
        self.label_23.setText(_translate("ui_menu", "CHICKEN PARMESAN:"))
        self.label_24.setText(_translate("ui_menu", "$26"))
        self.label_25.setText(_translate("ui_menu", "$21"))
        self.label_26.setText(_translate("ui_menu", "ROASTED BEEF:"))
        self.label_27.setText(_translate("ui_menu", "$20"))
        self.label_28.setText(_translate("ui_menu", "$27"))
        self.label_29.setText(_translate("ui_menu", "$30"))
        self.label_30.setText(_translate("ui_menu", "FISH FILLED:"))
        self.label_31.setText(_translate("ui_menu", "EGGPLANT LASAGNA:"))
        self.label_32.setText(_translate("ui_menu", "$22"))
        self.label_33.setText(_translate("ui_menu", "FRUITS SALAD:"))
        self.label_34.setText(_translate("ui_menu", "CRUMB CAKE:"))
        self.label_35.setText(_translate("ui_menu", "APPLE PIE:"))
        self.label_36.setText(_translate("ui_menu", "$18"))
        self.label_37.setText(_translate("ui_menu", "$21"))
        self.label_38.setText(_translate("ui_menu", "STRAWBERRY SMOTHIE:"))
        self.label_39.setText(_translate("ui_menu", "$20"))
        self.label_40.setText(_translate("ui_menu", "$23"))
        self.label_41.setText(_translate("ui_menu", "$24"))
        self.label_42.setText(_translate("ui_menu", "CHOCOLATE CHIP:"))
        self.label_43.setText(_translate("ui_menu", "BLUEBERRIES ICE CREAM:"))
        self.label_44.setText(_translate("ui_menu", "$40"))
        self.label_45.setText(_translate("ui_menu", "DRAFT BEER:"))
        self.label_46.setText(_translate("ui_menu", "WHISKEY:"))
        self.label_47.setText(_translate("ui_menu", "LEMON TEA:"))
        self.label_48.setText(_translate("ui_menu", "$18"))
        self.label_49.setText(_translate("ui_menu", "$11"))
        self.label_50.setText(_translate("ui_menu", "SODA:"))
        self.label_51.setText(_translate("ui_menu", "$23"))
        self.label_52.setText(_translate("ui_menu", "$35"))
        self.label_53.setText(_translate("ui_menu", "$8"))
        self.label_54.setText(_translate("ui_menu", "RED WINE:"))
        self.label_55.setText(_translate("ui_menu", "MOJITO:"))
        self.label_56.setText(_translate("ui_menu", "$40"))
        self.label_57.setText(_translate("ui_menu", "TENDERLOIN STEAK:"))
        self.label_58.setText(_translate("ui_menu", "RICOTTA PIE:"))
        self.label_59.setText(_translate("ui_menu", "BRUSCHETTA SALAD:"))
        self.label_60.setText(_translate("ui_menu", "$18"))
        self.label_61.setText(_translate("ui_menu", "$11"))
        self.label_62.setText(_translate("ui_menu", "VEGETARIAN CURY:"))
        self.label_63.setText(_translate("ui_menu", "$23"))
        self.label_64.setText(_translate("ui_menu", "$35"))
        self.label_65.setText(_translate("ui_menu", "$8"))
        self.label_66.setText(_translate("ui_menu", "MUSHROOM PIE:"))
        self.label_67.setText(_translate("ui_menu", "CHICKEN RANCH:"))
        self.label_70.setText(_translate("ui_menu", "$4.00\n"
"$4.00\n"
"$4.00\n"
"$4.00"))
        self.label_68.setText(_translate("ui_menu", "Winnin\' Chicken:"))
        self.label_69.setText(_translate("ui_menu", "Cheesy Chicken and Fries Combo\n"
"Cajun Chicken and Chips\n"
"Chicken Fingers and Baked Fries\n"
"Ranch Chicken and Herb Crisps"))
        self.label_71.setText(_translate("ui_menu", "$8.00\n"
"$8.00\n"
"$8.00\n"
"$8.00"))
        self.label_72.setText(_translate("ui_menu", "The Crew\'s Choice:"))
        self.label_73.setText(_translate("ui_menu", "Baked Fries & Chicken Fingers\n"
"Burger, Crisps, and Chicken\n"
"Burger and Fries Platter\n"
"Fried Chicken and Fries"))
        self.label_78.setText(_translate("ui_menu", "123 Anywhere St., Any City,ST 12345"))
        self.label_77.setText(_translate("ui_menu", "L\'s RESTAURANT"))
        self.label_86.setText(_translate("ui_menu", "50% OFF WEEKLY LUNCH!"))
        self.label_183.setText(_translate("ui_menu", "$8.99"))
        self.label_184.setText(_translate("ui_menu", "Dragon Roll"))
        self.label_185.setText(_translate("ui_menu", "Tempura shrimp, cucumber, crab meat, \n"
"avocato, tobiko and choice of salmon, \n"
"white tuna, BBQ eel or avocado on top"))
        self.label_189.setText(_translate("ui_menu", "123 Anywhere St., Any City,ST 12345"))
        self.label_191.setText(_translate("ui_menu", "L\'s RESTAURANT"))
        self.label_194.setText(_translate("ui_menu", "50% OFF MONDAY DINNER!"))
        self.label_186.setText(_translate("ui_menu", "$8.99"))
        self.label_187.setText(_translate("ui_menu", "Spider Roll"))
        self.label_188.setText(_translate("ui_menu", "Deep fried soft shell crab, crab meat,\n"
"cucumber, avocado topped with tobiko"))
        self.label_195.setText(_translate("ui_menu", "$8.99"))
        self.label_196.setText(_translate("ui_menu", "Sakura Roll"))
        self.label_197.setText(_translate("ui_menu", "Crab tempura, avocado, topped with\n"
"salmon, crispy flakes, special sauce"))
        self.pushButton.setText(_translate("ui_menu", "All"))
        self.pushButton_2.setText(_translate("ui_menu", "Appetizer"))
        self.pushButton_3.setText(_translate("ui_menu", "Main Course"))
        self.pushButton_4.setText(_translate("ui_menu", "Desserts"))
        self.pushButton_5.setText(_translate("ui_menu", "Drinks"))
        self.pushButton_6.setText(_translate("ui_menu", "Special Menus"))
        self.pushButton_7.setText(_translate("ui_menu", "Side Dishes"))
        self.pushButton_9.setText(_translate("ui_menu", "Mores..."))
        self.pushButton_10.setText(_translate("ui_menu", "Search"))
        self.pushButton_45.setText(_translate("ui_menu", "Cancel"))
        self.label_87.setText(_translate("ui_menu", "PURCHASED ITEMS:"))
        self.pushButton_48.setText(_translate("ui_menu", "CONFIRM PAY ......$ SECURELY"))
        self.label_94.setText(_translate("ui_menu", "SELECT YOUR TIPS:"))
        self.pushButton_58.setText(_translate("ui_menu", "Others"))
        self.pushButton_59.setText(_translate("ui_menu", "25%"))
        self.pushButton_60.setText(_translate("ui_menu", "15%"))
        self.pushButton_61.setText(_translate("ui_menu", "20%"))
        self.label_95.setText(_translate("ui_menu", "SUMMARY:"))
        self.label_90.setText(_translate("ui_menu", "$0.00"))
        self.label_89.setText(_translate("ui_menu", "Your Portition:"))
        self.label_96.setText(_translate("ui_menu", "$0.00"))
        self.label_97.setText(_translate("ui_menu", "Tip(%)"))
        self.label_98.setText(_translate("ui_menu", "$0.00"))
        self.label_99.setText(_translate("ui_menu", "Taxes:"))
        self.label_100.setText(_translate("ui_menu", "PAYMENT METHOD:"))
        self.comboBox.setItemText(0, _translate("ui_menu", "Cash -$-"))
        self.comboBox.setItemText(1, _translate("ui_menu", "Credit Card"))
        self.comboBox.setItemText(2, _translate("ui_menu", "Visa Card"))

import files_menu_rc
