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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1069, 698)
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
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon9.addFile(u":/feather/icons/feather/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.verticalLayout_11 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.mainPages = QCustomQStackedWidget(self.mainPagesCont)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_13 = QVBoxLayout(self.homePage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_12 = QLabel(self.homePage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)

        self.mainPages.addWidget(self.homePage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_14 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.reportsPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_13)

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
        self.verticalLayout_12 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_11 = QLabel(self.dataAnalysisPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_11)

        self.mainPages.addWidget(self.dataAnalysisPage)

        self.verticalLayout_11.addWidget(self.mainPages)


        self.horizontalLayout_10.addWidget(self.mainPagesCont)

        self.rightMenu = QCustomSlideMenu(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
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
        self.notificationPage = QWidget()
        self.notificationPage.setObjectName(u"notificationPage")
        self.verticalLayout_17 = QVBoxLayout(self.notificationPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_16 = QLabel(self.notificationPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_16)

        self.rightMenuPages.addWidget(self.notificationPage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_18 = QVBoxLayout(self.morePage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_17 = QLabel(self.morePage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)

        self.rightMenuPages.addWidget(self.morePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_19 = QVBoxLayout(self.profilePage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_18 = QLabel(self.profilePage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_18)

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


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.graphsBtn.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.titleTxt.setText(QCoreApplication.translate("MainWindow", u"CarFinder", None))
        self.notificationBtn.setText("")
        self.moreBtn.setText("")
        self.profileBtn.setText("")
        self.label_10.setText("")
        self.searchInp.setText("")
        self.searchInp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.label_9.setText("")
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Reports Page", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Charts Page", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Data Anaysis Page", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright Tunahan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Theme Progress", None))
    # retranslateUi
