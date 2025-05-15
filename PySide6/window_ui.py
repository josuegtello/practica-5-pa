# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 600)
        MainWindow.setStyleSheet(u"QWidget#gui *{\n"
"	font-family:arial;\n"
"	background-color:white;\n"
"	font-size:14px;\n"
"	color:black;\n"
"}\n"
"\n"
"/*Left Menu*/\n"
"QWidget#leftMenu QPushButton[btn-menu=\"left\"]{\n"
"	text-align:left;\n"
"	padding-left:8px;\n"
"	padding-right:20px;\n"
"	font-size:18px;	\n"
"}")
        self.gui = QWidget(MainWindow)
        self.gui.setObjectName(u"gui")
        self.horizontalLayout = QHBoxLayout(self.gui)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.gui)
        self.leftMenu.setObjectName(u"leftMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy)
        self.leftMenu.setMinimumSize(QSize(0, 0))
        self.leftMenu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.bottomLeftMenu = QWidget(self.leftMenu)
        self.bottomLeftMenu.setObjectName(u"bottomLeftMenu")
        self.bottomLeftMenu.setMinimumSize(QSize(0, 0))
        self.bottomLeftMenu.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.bottomLeftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.openMenuBtn = QPushButton(self.bottomLeftMenu)
        self.openMenuBtn.setObjectName(u"openMenuBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.openMenuBtn.sizePolicy().hasHeightForWidth())
        self.openMenuBtn.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"media/icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openMenuBtn.setIcon(icon)
        self.openMenuBtn.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.openMenuBtn)


        self.verticalLayout_4.addWidget(self.bottomLeftMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalWidget = QWidget(self.leftMenu)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.verticalWidget)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy3)
        self.homeBtn.setMinimumSize(QSize(0, 45))
        icon1 = QIcon()
        icon1.addFile(u"../../python/Programacion Avanzada/Practicas/Practica_4/code/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.verticalWidget)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.body = QWidget(self.gui)
        self.body.setObjectName(u"body")
        sizePolicy2.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.body)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.body)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.topMenu = QWidget(self.widget)
        self.topMenu.setObjectName(u"topMenu")

        self.horizontalLayout_2.addWidget(self.topMenu)

        self.windowButtons = QWidget(self.widget)
        self.windowButtons.setObjectName(u"windowButtons")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.windowButtons.sizePolicy().hasHeightForWidth())
        self.windowButtons.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.windowButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeWindowBtn = QPushButton(self.windowButtons)
        self.minimizeWindowBtn.setObjectName(u"minimizeWindowBtn")
        icon2 = QIcon()
        icon2.addFile(u"media/icons/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeWindowBtn.setIcon(icon2)
        self.minimizeWindowBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.minimizeWindowBtn)

        self.maximizeWindowBtn = QPushButton(self.windowButtons)
        self.maximizeWindowBtn.setObjectName(u"maximizeWindowBtn")
        icon3 = QIcon()
        icon3.addFile(u"media/icons/fullscreen.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeWindowBtn.setIcon(icon3)
        self.maximizeWindowBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.maximizeWindowBtn)

        self.closeWindowBtn = QPushButton(self.windowButtons)
        self.closeWindowBtn.setObjectName(u"closeWindowBtn")
        icon4 = QIcon()
        icon4.addFile(u"media/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeWindowBtn.setIcon(icon4)
        self.closeWindowBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.closeWindowBtn)


        self.horizontalLayout_2.addWidget(self.windowButtons, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.widget)

        self.content = QWidget(self.body)
        self.content.setObjectName(u"content")
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.content)
        self.pages.setObjectName(u"pages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 160, 49, 16))
        self.pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pages.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.pages)


        self.verticalLayout.addWidget(self.content)


        self.horizontalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.gui)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openMenuBtn.setText("")
        self.openMenuBtn.setProperty(u"state", QCoreApplication.translate("MainWindow", u"opened", None))
        self.openMenuBtn.setProperty(u"btn-menu", QCoreApplication.translate("MainWindow", u"hamburger", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.homeBtn.setProperty(u"state", QCoreApplication.translate("MainWindow", u"selected", None))
        self.homeBtn.setProperty(u"btn-menu", QCoreApplication.translate("MainWindow", u"left", None))
        self.homeBtn.setProperty(u"page-index", QCoreApplication.translate("MainWindow", u"0", None))
        self.minimizeWindowBtn.setText("")
        self.maximizeWindowBtn.setText("")
        self.maximizeWindowBtn.setProperty(u"state", QCoreApplication.translate("MainWindow", u"maximized", None))
        self.closeWindowBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
    # retranslateUi

