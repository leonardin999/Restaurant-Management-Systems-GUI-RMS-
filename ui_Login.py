# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Leonard/AppData/Local/Temp/LoginYsaFOl.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_area = QtWidgets.QFrame(self.centralwidget)
        self.login_area.setGeometry(QtCore.QRect(530, 10, 381, 571))
        self.login_area.setMaximumSize(QtCore.QSize(450, 660))
        self.login_area.setStyleSheet("border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"background-color: rgb(214, 214, 214);")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.label_credits = QtWidgets.QLabel(self.login_area)
        self.label_credits.setGeometry(QtCore.QRect(10, 540, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.stackedWidget = QtWidgets.QStackedWidget(self.login_area)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 80, 361, 461))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Sign_up = QtWidgets.QWidget()
        self.Sign_up.setObjectName("Sign_up")
        self.label = QtWidgets.QLabel(self.Sign_up)
        self.label.setGeometry(QtCore.QRect(20, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.Sign_Up = QtWidgets.QPushButton(self.Sign_up)
        self.Sign_Up.setGeometry(QtCore.QRect(40, 320, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sign_Up.setFont(font)
        self.Sign_Up.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 30px;\n"
"    \n"
"    color: rgb(214, 214, 214);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150, 150, 150);\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.Sign_Up.setObjectName("Sign_Up")
        self.fullname_edit = QtWidgets.QLineEdit(self.Sign_up)
        self.fullname_edit.setGeometry(QtCore.QRect(40, 130, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.fullname_edit.setFont(font)
        self.fullname_edit.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    background-color: transparent;    \n"
"    color: rgb(90, 90, 90);\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(241, 241, 241);\n"
"    border: 5px solid rgb(241, 241, 241);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid transparent;    \n"
"    color:rgb(0, 0, 0);\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"}")
        self.fullname_edit.setText("")
        self.fullname_edit.setMaxLength(32)
        self.fullname_edit.setObjectName("fullname_edit")
        self.label_2 = QtWidgets.QLabel(self.Sign_up)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 341, 51))
        self.label_2.setStyleSheet("color: rgb(194, 194, 194);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Sign_up)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(93, 93, 93);")
        self.label_3.setObjectName("label_3")
        self.email_edit = QtWidgets.QLineEdit(self.Sign_up)
        self.email_edit.setGeometry(QtCore.QRect(40, 200, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.email_edit.setFont(font)
        self.email_edit.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    background-color: transparent;    \n"
"    color: rgb(74, 74, 74);\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(241, 241, 241);\n"
"    border: 5px solid rgb(241, 241, 241);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid transparent;    \n"
"    color:rgb(0, 0, 0);\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"}")
        self.email_edit.setText("")
        self.email_edit.setMaxLength(32)
        self.email_edit.setObjectName("email_edit")
        self.label_5 = QtWidgets.QLabel(self.Sign_up)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(93, 93, 93);")
        self.label_5.setObjectName("label_5")
        self.number_edit = QtWidgets.QLineEdit(self.Sign_up)
        self.number_edit.setGeometry(QtCore.QRect(40, 270, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.number_edit.setFont(font)
        self.number_edit.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    background-color: transparent;    \n"
"    color: rgb(74, 74, 74);\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(241, 241, 241);\n"
"    border: 5px solid rgb(241, 241, 241);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid transparent;    \n"
"    color:rgb(0, 0, 0);\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"}")
        self.number_edit.setText("")
        self.number_edit.setMaxLength(32)
        self.number_edit.setObjectName("number_edit")
        self.label_6 = QtWidgets.QLabel(self.Sign_up)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(93, 93, 93);")
        self.label_6.setObjectName("label_6")
        self.Fb_SignUp = QtWidgets.QPushButton(self.Sign_up)
        self.Fb_SignUp.setGeometry(QtCore.QRect(150, 420, 32, 32))
        self.Fb_SignUp.setStyleSheet("background-image: url(:/social icons/icons/social/facebook.png);")
        self.Fb_SignUp.setText("")
        self.Fb_SignUp.setObjectName("Fb_SignUp")
        self.GG_SignUp = QtWidgets.QPushButton(self.Sign_up)
        self.GG_SignUp.setGeometry(QtCore.QRect(190, 420, 32, 32))
        self.GG_SignUp.setStyleSheet("background-image: url(:/social icons/icons/social/google.png);")
        self.GG_SignUp.setText("")
        self.GG_SignUp.setObjectName("GG_SignUp")
        self.TW_SignUp = QtWidgets.QPushButton(self.Sign_up)
        self.TW_SignUp.setGeometry(QtCore.QRect(230, 420, 32, 32))
        self.TW_SignUp.setStyleSheet("background-image: url(:/social icons/icons/social/twitter.png);")
        self.TW_SignUp.setText("")
        self.TW_SignUp.setObjectName("TW_SignUp")
        self.Log_In_Page = QtWidgets.QPushButton(self.Sign_up)
        self.Log_In_Page.setGeometry(QtCore.QRect(240, 380, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Log_In_Page.setFont(font)
        self.Log_In_Page.setStyleSheet("QPushButton {    \n"
"    background-color:transparent;\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {    \n"
"    color:rgb(186, 186, 186);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.Log_In_Page.setObjectName("Log_In_Page")
        self.label_4 = QtWidgets.QLabel(self.Sign_up)
        self.label_4.setGeometry(QtCore.QRect(95, 389, 147, 16))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.IG_SignUp = QtWidgets.QPushButton(self.Sign_up)
        self.IG_SignUp.setGeometry(QtCore.QRect(270, 420, 32, 32))
        self.IG_SignUp.setStyleSheet("background-image: url(:/social icons/icons/social/instagram.png);")
        self.IG_SignUp.setText("")
        self.IG_SignUp.setObjectName("IG_SignUp")
        self.label_7 = QtWidgets.QLabel(self.Sign_up)
        self.label_7.setGeometry(QtCore.QRect(60, 430, 71, 16))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.Sign_up)
        self.Sign_in = QtWidgets.QWidget()
        self.Sign_in.setObjectName("Sign_in")
        self.label_12 = QtWidgets.QLabel(self.Sign_in)
        self.label_12.setGeometry(QtCore.QRect(30, 210, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(93, 93, 93);")
        self.label_12.setObjectName("label_12")
        self.Username = QtWidgets.QLineEdit(self.Sign_in)
        self.Username.setGeometry(QtCore.QRect(40, 160, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.Username.setFont(font)
        self.Username.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    background-color: transparent;    \n"
"    color: rgb(90, 90, 90);\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(241, 241, 241);\n"
"    border: 5px solid rgb(241, 241, 241);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid transparent;    \n"
"    color:rgb(0, 0, 0);\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"}")
        self.Username.setText("")
        self.Username.setMaxLength(32)
        self.Username.setObjectName("Username")
        self.label_14 = QtWidgets.QLabel(self.Sign_in)
        self.label_14.setGeometry(QtCore.QRect(30, 140, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(93, 93, 93);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Sign_in)
        self.label_15.setGeometry(QtCore.QRect(20, 8, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.password = QtWidgets.QLineEdit(self.Sign_in)
        self.password.setGeometry(QtCore.QRect(40, 230, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    background-color: transparent;    \n"
"    color: rgb(74, 74, 74);\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(241, 241, 241);\n"
"    border: 5px solid rgb(241, 241, 241);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid transparent;    \n"
"    color:rgb(0, 0, 0);\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"}")
        self.password.setText("")
        self.password.setMaxLength(32)
        self.password.setObjectName("password")
        self.label_16 = QtWidgets.QLabel(self.Sign_in)
        self.label_16.setGeometry(QtCore.QRect(20, 60, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.Log_In = QtWidgets.QPushButton(self.Sign_in)
        self.Log_In.setGeometry(QtCore.QRect(40, 300, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Log_In.setFont(font)
        self.Log_In.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 30px;\n"
"    \n"
"    color: rgb(214, 214, 214);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150, 150, 150);\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.Log_In.setObjectName("Log_In")
        self.Sign_Up_Pages = QtWidgets.QPushButton(self.Sign_in)
        self.Sign_Up_Pages.setGeometry(QtCore.QRect(69, 365, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Sign_Up_Pages.setFont(font)
        self.Sign_Up_Pages.setStyleSheet("QPushButton {    \n"
"    background-color:transparent;\n"
"    border-radius: 5px;\n"
"    color: rgb(38, 38, 38);\n"
"}\n"
"QPushButton:hover {    \n"
"    color:rgb(186, 186, 186);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.Sign_Up_Pages.setObjectName("Sign_Up_Pages")
        self.pushButton_login_4 = QtWidgets.QPushButton(self.Sign_in)
        self.pushButton_login_4.setGeometry(QtCore.QRect(140, 510, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_login_4.setFont(font)
        self.pushButton_login_4.setStyleSheet("QPushButton {    \n"
"    background-color:transparent;\n"
"    border-radius: 5px;\n"
"    color: rgb(139, 139, 139);\n"
"}\n"
"QPushButton:hover {    \n"
"    color:rgb(186, 186, 186);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_login_4.setObjectName("pushButton_login_4")
        self.IG_Log_In = QtWidgets.QPushButton(self.Sign_in)
        self.IG_Log_In.setGeometry(QtCore.QRect(280, 420, 32, 32))
        self.IG_Log_In.setStyleSheet("background-image: url(:/social icons/icons/social/instagram.png);")
        self.IG_Log_In.setText("")
        self.IG_Log_In.setObjectName("IG_Log_In")
        self.GG_Log_In = QtWidgets.QPushButton(self.Sign_in)
        self.GG_Log_In.setGeometry(QtCore.QRect(200, 420, 32, 32))
        self.GG_Log_In.setStyleSheet("background-image: url(:/social icons/icons/social/google.png);")
        self.GG_Log_In.setText("")
        self.GG_Log_In.setObjectName("GG_Log_In")
        self.label_9 = QtWidgets.QLabel(self.Sign_in)
        self.label_9.setGeometry(QtCore.QRect(70, 430, 71, 16))
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.TW_Log_In = QtWidgets.QPushButton(self.Sign_in)
        self.TW_Log_In.setGeometry(QtCore.QRect(240, 420, 32, 32))
        self.TW_Log_In.setStyleSheet("background-image: url(:/social icons/icons/social/twitter.png);")
        self.TW_Log_In.setText("")
        self.TW_Log_In.setObjectName("TW_Log_In")
        self.FB_Log_In = QtWidgets.QPushButton(self.Sign_in)
        self.FB_Log_In.setGeometry(QtCore.QRect(160, 420, 32, 32))
        self.FB_Log_In.setStyleSheet("background-image: url(:/social icons/icons/social/facebook.png);")
        self.FB_Log_In.setText("")
        self.FB_Log_In.setObjectName("FB_Log_In")
        self.label_12.raise_()
        self.Username.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.password.raise_()
        self.label_16.raise_()
        self.Log_In.raise_()
        self.pushButton_login_4.raise_()
        self.Sign_Up_Pages.raise_()
        self.IG_Log_In.raise_()
        self.GG_Log_In.raise_()
        self.label_9.raise_()
        self.TW_Log_In.raise_()
        self.FB_Log_In.raise_()
        self.stackedWidget.addWidget(self.Sign_in)
        self.frame_error = QtWidgets.QFrame(self.login_area)
        self.frame_error.setGeometry(QtCore.QRect(10, 40, 361, 30))
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius: 5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setGeometry(QtCore.QRect(50, 5, 231, 21))
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.close_popup = QtWidgets.QPushButton(self.frame_error)
        self.close_popup.setGeometry(QtCore.QRect(330, 5, 20, 20))
        self.close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.close_popup.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;    \n"
"    background-image:url(:/20x20/icons/20x20/cil-x.png);\n"
"    background-position: center;    \n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);    \n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.close_popup.setText("")
        self.close_popup.setObjectName("close_popup")
        self.btn_close = QtWidgets.QPushButton(self.login_area)
        self.btn_close.setGeometry(QtCore.QRect(350, 10, 17, 17))
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
        self.btn_minimize = QtWidgets.QPushButton(self.login_area)
        self.btn_minimize.setGeometry(QtCore.QRect(323, 10, 17, 17))
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
        self.btn_maximize = QtWidgets.QPushButton(self.login_area)
        self.btn_maximize.setGeometry(QtCore.QRect(296, 10, 17, 17))
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 521, 571))
        self.frame.setStyleSheet("background-image: url(:/images/images/Special Healthy Salad Restaurant Menu Instagram Post.png);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_credits.setText(_translate("MainWindow", "Created by: Phung Hung Binh"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.Sign_Up.setText(_translate("MainWindow", "Get Stared"))
        self.fullname_edit.setPlaceholderText(_translate("MainWindow", "Enter your full name"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Direct from the best service coffee all over the world. </p><p>Delivered right to your door step.</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "FULL NAME"))
        self.email_edit.setPlaceholderText(_translate("MainWindow", "Enter your email address"))
        self.label_5.setText(_translate("MainWindow", "PERSONAL MAIL"))
        self.number_edit.setPlaceholderText(_translate("MainWindow", "Enter your phone number"))
        self.label_6.setText(_translate("MainWindow", "PHONE NUMBER"))
        self.Log_In_Page.setText(_translate("MainWindow", "Log In"))
        self.label_4.setText(_translate("MainWindow", "Already have a Account ?"))
        self.label_7.setText(_translate("MainWindow", "Sign up with"))
        self.label_12.setText(_translate("MainWindow", "PASSWORD"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.label_14.setText(_translate("MainWindow", "USERNAME"))
        self.label_15.setText(_translate("MainWindow", "Welcome"))
        self.password.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.label_16.setText(_translate("MainWindow", "Back!"))
        self.Log_In.setText(_translate("MainWindow", "Sign in"))
        self.Sign_Up_Pages.setText(_translate("MainWindow", "Create a new account ?"))
        self.pushButton_login_4.setText(_translate("MainWindow", "Forgot Password ?"))
        self.label_9.setText(_translate("MainWindow", "Sign in with"))
        self.label_error.setText(_translate("MainWindow", "Error"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))

import files_rc
