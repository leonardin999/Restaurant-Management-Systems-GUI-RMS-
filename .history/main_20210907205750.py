################################################################################
##
## BY: Phung Hung Binh
## PROJECT MADE WITH: Qt Designer and PyQt5
## V: 1.0.0
##
################################################################################

import sys
from PyQt5 import uic
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from Function_Login import *
from Function_Menus import *
from ui_Login import *
from ui_main_menu import *
# GLOBALS
counter = 0
jumper = 10

## ==> YOUR APPLICATION WINDOW
class Menu_Windown(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi('main_menu.ui',self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
class Login_Windown(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi('Login.ui',self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Functions_Login.uiDefinitions(self)
        ## ==> MOVE WINDOW FUNCTIONALITY ##
        ########################################################################
        def moveWindow(event):

        ## moving window ##
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame.mouseMoveEvent = moveWindow
        self.ui.login_area.mouseMoveEvent = moveWindow
    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
        self.ui.close_popup.clicked.connect(lambda: self.frame_error.hide())
        self.ui.frame_error.hide()
        self.ui.Log_In.clicked.connect(lambda: Menu_Windown().show())
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi('splash_screen.ui',self)
        self.progressBarValue(0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) #
        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(10)
        self.show()

    def progress (self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.login = Login_Windown()
            self.login.show()
            self.close()
        counter += 0.5

    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
            background-color: qconicalgradient(spread:pad,cx:0.5, cy:0.5, angle:90, stop:{STOP_2} rgba(254, 121, 200, 255), stop:{STOP_1} rgba(170, 85, 255, 30));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
