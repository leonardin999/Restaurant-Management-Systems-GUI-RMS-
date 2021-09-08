################################################################################
##
## BY: PHUNG HUNG BINH
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##

from main import *

class Functions_Login(Login_Windown):
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    def uiDefinitions(self):
        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.shadow1 = QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(17)
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow1.setColor(QColor(0, 0, 0, 150))
        self.ui.login_area.setGraphicsEffect(self.shadow1)

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
