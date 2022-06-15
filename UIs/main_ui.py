# -*- coding: utf-8 -*-


#Automatycznie wygenerowane na podstawie pliku main.ui za pomocą narzędzia pyside6-uic

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(915, 665)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(915, 665))
        MainWindow.setMaximumSize(QSize(919, 669))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette = QPalette()
        brush = QBrush(QColor(0, 120, 215, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setStyleSheet(u"")
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setGeometry(QRect(0, 50, 915, 615))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setMinimumSize(QSize(915, 615))
        self.body.setMaximumSize(QSize(915, 615))
        self.body.setStyleSheet(u"background-color: #455A64;\n"
"border: none;")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.mailList = QListWidget(self.body)
        self.mailList.setObjectName(u"mailList")
        self.mailList.setGeometry(QRect(0, 4, 915, 607))
        self.mailList.setStyleSheet(u"padding:5px;\n"
"border:none;")
        self.mailList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mailList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.side_menu = QFrame(self.body)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setGeometry(QRect(0, 0, 400, 615))
        self.side_menu.setStyleSheet(u"background-color: rgb(55, 71, 79);\n"
"border: none;\n"
"border-right: 2px solid #263238;\n"
"border-top: 2px solid #263238;\n"
"color: rgb(255, 255, 255);")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.address_list = QListWidget(self.side_menu)
        self.address_list.setObjectName(u"address_list")
        self.address_list.setGeometry(QRect(2, 110, 396, 501))
        self.address_list.setStyleSheet(u"padding:5px;\n"
"border:none;")
        self.address_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.address_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.email_edit = QLineEdit(self.side_menu)
        self.email_edit.setObjectName(u"email_edit")
        self.email_edit.setGeometry(QRect(20, 10, 171, 31))
        font = QFont()
        font.setPointSize(11)
        self.email_edit.setFont(font)
        self.email_edit.setStyleSheet(u"border:none;\n"
"border-bottom: 1px solid white;\n"
"")
        self.add_button = QPushButton(self.side_menu)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(330, 10, 51, 31))
        self.add_button.setStyleSheet(u"border: 1px solid white;")
        self.random_button = QPushButton(self.side_menu)
        self.random_button.setObjectName(u"random_button")
        self.random_button.setGeometry(QRect(150, 60, 101, 31))
        self.random_button.setStyleSheet(u"border: 1px solid white;")
        self.combo_box = QComboBox(self.side_menu)
        self.combo_box.setObjectName(u"combo_box")
        self.combo_box.setGeometry(QRect(200, 10, 121, 31))
        self.combo_box.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid white;")
        self.menu_top_bar = QFrame(self.centralwidget)
        self.menu_top_bar.setObjectName(u"menu_top_bar")
        self.menu_top_bar.setGeometry(QRect(0, 0, 915, 50))
        palette1 = QPalette()
        brush2 = QBrush(QColor(55, 71, 79, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        self.menu_top_bar.setPalette(palette1)
        self.menu_top_bar.setStyleSheet(u"background-color: rgb(55, 71, 79);\n"
"border: none;")
        self.menu_top_bar.setFrameShape(QFrame.StyledPanel)
        self.menu_top_bar.setFrameShadow(QFrame.Raised)
        self.menu_button = QPushButton(self.menu_top_bar)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setGeometry(QRect(20, 10, 30, 30))
        self.menu_button.setStyleSheet(u"border: none;\n"
"")
        icon = QIcon()
        icon.addFile(u"IMGs/Hamburger_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(40, 30))
        self.menu_button.setAutoDefault(False)
        self.menu_button.setFlat(True)
        self.close_button = QPushButton(self.menu_top_bar)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(860, 10, 30, 30))
        self.close_button.setStyleSheet(u"border: none;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"IMGs/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(25, 25))
        self.minimize_button = QPushButton(self.menu_top_bar)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(810, 10, 30, 30))
        self.minimize_button.setStyleSheet(u"border: none;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"IMGs/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon2)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.label = QLabel(self.menu_top_bar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 915, 50))
        palette2 = QPalette()
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.label.setPalette(palette2)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.refresh_button = QPushButton(self.menu_top_bar)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(70, 10, 30, 30))
        self.refresh_button.setStyleSheet(u"border: none;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"IMGs/refresh_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_button.setIcon(icon3)
        self.refresh_button.setIconSize(QSize(40, 30))
        self.refresh_button.setAutoDefault(False)
        self.refresh_button.setFlat(True)
        self.label.raise_()
        self.menu_button.raise_()
        self.close_button.raise_()
        self.minimize_button.raise_()
        self.refresh_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menu_button.setDefault(False)
        self.refresh_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.email_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter email...", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.random_button.setText(QCoreApplication.translate("MainWindow", u"Generate random", None))
        self.menu_button.setText("")
        self.close_button.setText("")
        self.minimize_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TmpMail", None))
        self.refresh_button.setText("")
    # retranslateUi

