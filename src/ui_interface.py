# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1828, 698)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1069, 698))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(46, 42))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(98, 136))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 0, 5)
        self.homeBtn = QPushButton(self.widget_3)
        self.homeBtn.setObjectName(u"homeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.widget_3)
        self.dataBtn.setObjectName(u"dataBtn")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataBtn.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.dataBtn)

        self.reportsBtn = QPushButton(self.widget_3)
        self.reportsBtn.setObjectName(u"reportsBtn")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/printer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportsBtn.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.reportsBtn)

        self.graphsBtn = QPushButton(self.widget_3)
        self.graphsBtn.setObjectName(u"graphsBtn")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/pie-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graphsBtn.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.graphsBtn)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(116, 105))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 0, 5)
        self.settingsBtn = QPushButton(self.widget_2)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.widget_2)
        self.infoBtn.setObjectName(u"infoBtn")
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoBtn.setIcon(icon6)

        self.verticalLayout_3.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.widget_2)
        self.helpBtn.setObjectName(u"helpBtn")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.helpBtn)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.widget_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.closeCenterMenuBtn)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_6 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.widget_5 = QWidget(self.settingsPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame = QFrame(self.widget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.themeList = QComboBox(self.frame)
        self.themeList.setObjectName(u"themeList")

        self.horizontalLayout_3.addWidget(self.themeList)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_8 = QVBoxLayout(self.informationPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.informationPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.centerMenuPages.addWidget(self.informationPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.helpPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignVCenter)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_5.addWidget(self.centerMenuPages)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.mainBody)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 5, 0, 0)
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.titleTxt = QLabel(self.header)
        self.titleTxt.setObjectName(u"titleTxt")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.titleTxt.setFont(font1)

        self.horizontalLayout_7.addWidget(self.titleTxt, 0, Qt.AlignmentFlag.AlignBottom)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 0, 5)
        self.notificationBtn = QPushButton(self.frame_3)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon9 = QIcon()
        icon9.addFile(u":/feather/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreBtn = QPushButton(self.frame_3)
        self.moreBtn.setObjectName(u"moreBtn")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/more-horizontal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moreBtn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.moreBtn)

        self.profileBtn = QPushButton(self.frame_3)
        self.profileBtn.setObjectName(u"profileBtn")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.profileBtn)


        self.horizontalLayout_7.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignBottom)

        self.searchinpCont = QFrame(self.header)
        self.searchinpCont.setObjectName(u"searchinpCont")
        self.searchinpCont.setMaximumSize(QSize(410, 16777215))
        self.searchinpCont.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchinpCont.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.searchinpCont)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_10 = QLabel(self.searchinpCont)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(16, 16))
        self.label_10.setMaximumSize(QSize(16, 16))
        self.label_10.setPixmap(QPixmap(u"../35e97f94/alert-circle.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.searchInp = QLineEdit(self.searchinpCont)
        self.searchInp.setObjectName(u"searchInp")
        self.searchInp.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.searchInp)

        self.label_9 = QLabel(self.searchinpCont)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.searchBtn = QPushButton(self.searchinpCont)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_8.addWidget(self.searchBtn)


        self.horizontalLayout_7.addWidget(self.searchinpCont, 0, Qt.AlignmentFlag.AlignBottom)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_4)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_4)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon13)

        self.horizontalLayout_9.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon14)

        self.horizontalLayout_9.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_10.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainPagesCont.sizePolicy().hasHeightForWidth())
        self.mainPagesCont.setSizePolicy(sizePolicy2)
        self.mainPagesCont.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.mainPagesCont)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.mainPages = QCustomQStackedWidget(self.mainPagesCont)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_11 = QVBoxLayout(self.homePage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.rentTable = QTableWidget(self.homePage)
        if (self.rentTable.columnCount() < 8):
            self.rentTable.setColumnCount(8)
        if (self.rentTable.rowCount() < 1000):
            self.rentTable.setRowCount(1000)
        self.rentTable.setObjectName(u"rentTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rentTable.sizePolicy().hasHeightForWidth())
        self.rentTable.setSizePolicy(sizePolicy3)
        self.rentTable.setRowCount(1000)
        self.rentTable.setColumnCount(8)

        self.verticalLayout_11.addWidget(self.rentTable)

        self.mainPages.addWidget(self.homePage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.reportsPage.sizePolicy().hasHeightForWidth())
        self.reportsPage.setSizePolicy(sizePolicy4)
        self.verticalLayout_14 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.customerTable = QTableWidget(self.reportsPage)
        if (self.customerTable.columnCount() < 6):
            self.customerTable.setColumnCount(6)
        if (self.customerTable.rowCount() < 1000):
            self.customerTable.setRowCount(1000)
        self.customerTable.setObjectName(u"customerTable")
        self.customerTable.setRowCount(1000)
        self.customerTable.setColumnCount(6)

        self.verticalLayout_14.addWidget(self.customerTable)

        self.mainPages.addWidget(self.reportsPage)
        self.chartsPage = QWidget()
        self.chartsPage.setObjectName(u"chartsPage")
        self.verticalLayout_15 = QVBoxLayout(self.chartsPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.chartsPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_14)

        self.mainPages.addWidget(self.chartsPage)
        self.dataAnalysisPage = QWidget()
        self.dataAnalysisPage.setObjectName(u"dataAnalysisPage")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dataAnalysisPage.sizePolicy().hasHeightForWidth())
        self.dataAnalysisPage.setSizePolicy(sizePolicy5)
        self.verticalLayout_12 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.carsTable = QTableWidget(self.dataAnalysisPage)
        if (self.carsTable.columnCount() < 6):
            self.carsTable.setColumnCount(6)
        if (self.carsTable.rowCount() < 1000):
            self.carsTable.setRowCount(1000)
        self.carsTable.setObjectName(u"carsTable")
        sizePolicy3.setHeightForWidth(self.carsTable.sizePolicy().hasHeightForWidth())
        self.carsTable.setSizePolicy(sizePolicy3)
        self.carsTable.setRowCount(1000)
        self.carsTable.setColumnCount(6)

        self.verticalLayout_12.addWidget(self.carsTable)

        self.mainPages.addWidget(self.dataAnalysisPage)

        self.horizontalLayout_12.addWidget(self.mainPages)


        self.horizontalLayout_10.addWidget(self.mainPagesCont)

        self.rightMenu = QCustomSlideMenu(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.rightMenu.sizePolicy().hasHeightForWidth())
        self.rightMenu.setSizePolicy(sizePolicy6)
        self.rightMenu.setMinimumSize(QSize(600, 500))
        self.verticalLayout_16 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.widget_6 = QWidget(self.rightMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.widget_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.closeRightMenuBtn = QPushButton(self.widget_6)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon8)

        self.horizontalLayout_11.addWidget(self.closeRightMenuBtn)


        self.verticalLayout_16.addWidget(self.widget_6)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenu)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        sizePolicy2.setHeightForWidth(self.rightMenuPages.sizePolicy().hasHeightForWidth())
        self.rightMenuPages.setSizePolicy(sizePolicy2)
        self.notificationPage = QWidget()
        self.notificationPage.setObjectName(u"notificationPage")
        self.gridLayoutWidget_2 = QWidget(self.notificationPage)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 572, 507))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 2, 1, 1, 1)

        self.CarDelete = QPushButton(self.gridLayoutWidget_2)
        self.CarDelete.setObjectName(u"CarDelete")

        self.gridLayout_2.addWidget(self.CarDelete, 4, 0, 1, 1)

        self.CarNew = QPushButton(self.gridLayoutWidget_2)
        self.CarNew.setObjectName(u"CarNew")

        self.gridLayout_2.addWidget(self.CarNew, 3, 0, 1, 1)

        self.CarIdTable = QLineEdit(self.gridLayoutWidget_2)
        self.CarIdTable.setObjectName(u"CarIdTable")

        self.gridLayout_2.addWidget(self.CarIdTable, 0, 0, 1, 1)

        self.Model = QLineEdit(self.gridLayoutWidget_2)
        self.Model.setObjectName(u"Model")

        self.gridLayout_2.addWidget(self.Model, 1, 3, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 1, 2, 1, 1)

        self.CarUpdate = QPushButton(self.gridLayoutWidget_2)
        self.CarUpdate.setObjectName(u"CarUpdate")

        self.gridLayout_2.addWidget(self.CarUpdate, 3, 3, 1, 1)

        self.ModelYear = QLineEdit(self.gridLayoutWidget_2)
        self.ModelYear.setObjectName(u"ModelYear")

        self.gridLayout_2.addWidget(self.ModelYear, 2, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 0, 2, 1, 1)

        self.Kilometer = QLineEdit(self.gridLayoutWidget_2)
        self.Kilometer.setObjectName(u"Kilometer")

        self.gridLayout_2.addWidget(self.Kilometer, 2, 3, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.Brand = QLineEdit(self.gridLayoutWidget_2)
        self.Brand.setObjectName(u"Brand")

        self.gridLayout_2.addWidget(self.Brand, 1, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 1, 1, 1, 1)

        self.Plate = QLineEdit(self.gridLayoutWidget_2)
        self.Plate.setObjectName(u"Plate")

        self.gridLayout_2.addWidget(self.Plate, 0, 3, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 2, 2, 1, 1)

        self.rightMenuPages.addWidget(self.notificationPage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        sizePolicy2.setHeightForWidth(self.morePage.sizePolicy().hasHeightForWidth())
        self.morePage.setSizePolicy(sizePolicy2)
        self.gridLayoutWidget_3 = QWidget(self.morePage)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 0, 572, 507))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.FirstDate = QLineEdit(self.gridLayoutWidget_3)
        self.FirstDate.setObjectName(u"FirstDate")

        self.gridLayout_4.addWidget(self.FirstDate, 3, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 0, 2, 1, 1)

        self.EndDate = QLineEdit(self.gridLayoutWidget_3)
        self.EndDate.setObjectName(u"EndDate")

        self.gridLayout_4.addWidget(self.EndDate, 3, 3, 1, 1)

        self.RentUpdate = QPushButton(self.gridLayoutWidget_3)
        self.RentUpdate.setObjectName(u"RentUpdate")

        self.gridLayout_4.addWidget(self.RentUpdate, 4, 3, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_4.addWidget(self.label_34, 3, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_3)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_4.addWidget(self.label_35, 1, 2, 1, 1)

        self.CarId = QLineEdit(self.gridLayoutWidget_3)
        self.CarId.setObjectName(u"CarId")

        self.gridLayout_4.addWidget(self.CarId, 0, 3, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_3)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_4.addWidget(self.label_36, 1, 1, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_3)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_4.addWidget(self.label_37, 3, 2, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_4.addWidget(self.label_38, 2, 2, 1, 1)

        self.CustomerId = QLineEdit(self.gridLayoutWidget_3)
        self.CustomerId.setObjectName(u"CustomerId")

        self.gridLayout_4.addWidget(self.CustomerId, 1, 0, 1, 1)

        self.RentPrice = QLineEdit(self.gridLayoutWidget_3)
        self.RentPrice.setObjectName(u"RentPrice")

        self.gridLayout_4.addWidget(self.RentPrice, 2, 0, 1, 1)

        self.Status_3 = QLineEdit(self.gridLayoutWidget_3)
        self.Status_3.setObjectName(u"Status_3")

        self.gridLayout_4.addWidget(self.Status_3, 1, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_3)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_4.addWidget(self.label_39, 2, 1, 1, 1)

        self.RentNew = QPushButton(self.gridLayoutWidget_3)
        self.RentNew.setObjectName(u"RentNew")

        self.gridLayout_4.addWidget(self.RentNew, 4, 0, 1, 1)

        self.RentId = QLineEdit(self.gridLayoutWidget_3)
        self.RentId.setObjectName(u"RentId")

        self.gridLayout_4.addWidget(self.RentId, 0, 0, 1, 1)

        self.Damaged = QLineEdit(self.gridLayoutWidget_3)
        self.Damaged.setObjectName(u"Damaged")

        self.gridLayout_4.addWidget(self.Damaged, 2, 3, 1, 1)

        self.RentDelete = QPushButton(self.gridLayoutWidget_3)
        self.RentDelete.setObjectName(u"RentDelete")

        self.gridLayout_4.addWidget(self.RentDelete, 5, 0, 1, 1)

        self.rightMenuPages.addWidget(self.morePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        sizePolicy2.setHeightForWidth(self.profilePage.sizePolicy().hasHeightForWidth())
        self.profilePage.setSizePolicy(sizePolicy2)
        self.verticalLayout_19 = QVBoxLayout(self.profilePage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_18 = QLabel(self.profilePage)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 1, 1, 1)

        self.Surname = QLineEdit(self.profilePage)
        self.Surname.setObjectName(u"Surname")

        self.gridLayout.addWidget(self.Surname, 1, 0, 1, 1)

        self.CustomerId_2 = QLineEdit(self.profilePage)
        self.CustomerId_2.setObjectName(u"CustomerId_2")

        self.gridLayout.addWidget(self.CustomerId_2, 0, 0, 1, 1)

        self.label_20 = QLabel(self.profilePage)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 2, 1, 1, 1)

        self.label_13 = QLabel(self.profilePage)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.CustomerName = QLineEdit(self.profilePage)
        self.CustomerName.setObjectName(u"CustomerName")

        self.gridLayout.addWidget(self.CustomerName, 0, 3, 1, 1)

        self.CustomerUpdate = QPushButton(self.profilePage)
        self.CustomerUpdate.setObjectName(u"CustomerUpdate")

        self.gridLayout.addWidget(self.CustomerUpdate, 3, 3, 1, 1)

        self.Age = QLineEdit(self.profilePage)
        self.Age.setObjectName(u"Age")

        self.gridLayout.addWidget(self.Age, 1, 3, 1, 1)

        self.label_8 = QLabel(self.profilePage)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.CustomerNew = QPushButton(self.profilePage)
        self.CustomerNew.setObjectName(u"CustomerNew")

        self.gridLayout.addWidget(self.CustomerNew, 3, 0, 1, 1)

        self.TC = QLineEdit(self.profilePage)
        self.TC.setObjectName(u"TC")

        self.gridLayout.addWidget(self.TC, 2, 3, 1, 1)

        self.label_19 = QLabel(self.profilePage)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 1, 2, 1, 1)

        self.License = QLineEdit(self.profilePage)
        self.License.setObjectName(u"License")

        self.gridLayout.addWidget(self.License, 2, 0, 1, 1)

        self.label_21 = QLabel(self.profilePage)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 2, 2, 1, 1)

        self.CustomerDelete = QPushButton(self.profilePage)
        self.CustomerDelete.setObjectName(u"CustomerDelete")

        self.gridLayout.addWidget(self.CustomerDelete, 4, 0, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout)

        self.rightMenuPages.addWidget(self.profilePage)

        self.verticalLayout_16.addWidget(self.rightMenuPages)


        self.horizontalLayout_10.addWidget(self.rightMenu)


        self.verticalLayout_10.addWidget(self.mainContents)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 0, 0)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.frame_2 = QFrame(self.footer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.activityProgress = QProgressBar(self.frame_2)
        self.activityProgress.setObjectName(u"activityProgress")
        self.activityProgress.setMinimumSize(QSize(0, 10))
        self.activityProgress.setMaximumSize(QSize(16777215, 10))
        self.activityProgress.setValue(24)
        self.activityProgress.setTextVisible(False)

        self.horizontalLayout_5.addWidget(self.activityProgress)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.sizeGrip, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_10.addWidget(self.footer, 0, Qt.AlignmentFlag.AlignBottom)

         # QTableWidget'ı yatayda ve dikeyde esnek hale getirin
        self.customerTable.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
 
        # Sütun genişliklerini otomatik olarak ayarlayın
        self.customerTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
        # Satır yüksekliklerini otomatik olarak ayarlayın
        self.customerTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
        self.rentTable.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
 
 
        self.rentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
        
        self.rentTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
        self.carsTable.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
 
        # Sütun genişliklerini otomatik olarak ayarlayın
        self.carsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
        # Satır yüksekliklerini otomatik olarak ayarlayın
        self.carsTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
 

        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("Menu")
        self.homeBtn.setText("Rent")
        self.dataBtn.setText("Car")
        self.reportsBtn.setText("Customer")
        self.graphsBtn.setText("Graphs")
        self.settingsBtn.setText("Settings")
        self.infoBtn.setText("Info")
        self.helpBtn.setText("Help")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.closeCenterMenuBtn.setText("X")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.titleTxt.setText(QCoreApplication.translate("MainWindow", u"CarFinder", None))
        self.notificationBtn.setText("Cars")
        self.moreBtn.setText("Rent")
        self.profileBtn.setText("Customer")
        self.label_10.setText("X")
        self.searchInp.setText("?")
        self.searchInp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.label_9.setText("X")
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
        self.minimizeBtn.setText("Minimize")
        self.restoreBtn.setText("Restore")
        self.closeBtn.setText("X")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Charts Page", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("X")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"ModelYear", None))
        self.CarDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CarNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.CarUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Plate", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CarId", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Brand", None))
        self.Plate.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Kilometer", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CarId", None))
        self.RentUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"FirstDate", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.CarId.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"CustomerId", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"EndDate", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Damaged", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"RentId", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"RentPrice", None))
        self.RentNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.RentDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"DriverLicense", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.CustomerUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CustomerId", None))
        self.CustomerNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TC", None))
        self.CustomerDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright Tunahan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Theme Progress", None))
    # retranslateUi

