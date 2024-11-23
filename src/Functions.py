from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader
from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main=MainWindow
        self.ui =MainWindow.ui



        #init app theme
        self.initializeAppTheme()

        #add click event to search button
        self.ui.searchBtn.clicked.connect(self.showSearchResults)

        self.connectMenuButtons()
    def connectMenuButtons(self):
         self.ui.settingsBtn.clicked.connect(lambda:self.ui.centerMenu.expandMenu())
         self.ui.infoBtn.clicked.connect(lambda:self.ui.centerMenu.expandMenu())
         self.ui.helpBtn.clicked.connect(lambda:self.ui.centerMenu.expandMenu())

         self.ui.closeCenterMenuBtn.clicked.connect(lambda:self.ui.centerMenu.collapseMenu())

         self.ui.notificationBtn.clicked.connect(lambda:self.ui.rightMenu.expandMenu())
         self.ui.moreBtn.clicked.connect(lambda:self.ui.rightMenu.expandMenu())
         self.ui.profileBtn.clicked.connect(lambda:self.ui.rightMenu.expandMenu())

         self.ui.closeRightMenuBtn.clicked.connect(lambda:self.ui.rightMenu.collapseMenu())

    #Create searchbar tooltip
    def createSearchTipOverlay(self):
        self.searchTooltip = QCustomTipOverlay(
            title="Search Results.",
            description="Searching...",
            icon=self.main.theme.PATH_RESOURCES+"feather/search.png",
            isClosable=True,
            target=self.ui.searchinpCont,   #put tipoverlay
            parent=self.main,
            deleteOnClose=True,
            duration=-1,
            tailPosition="top-center",
            closeIcon=self.main.theme.PATH_RESOURCES+"material_design/close.png",
            toolFlag=True

        )
        #Create Loader
        loader=QCustom3CirclesLoader(
             parent=self.searchTooltip,
             color=QColor(self.main.theme.COLOR_ACCENT_1),
             penWidth=20,
             animationDuration=400
        )
        #add loader to tip
        self.searchTooltip.addWidget(loader)


        #show tip overlay
    def showSearchResults(self):
        #only if not empty
        searchPhrase = self.ui.searchInp.text()
        if not searchPhrase:
             return 
        try:
                self.searchTooltip.show()
        except:
                #re-init
                self.createSearchTipOverlay()
                self.searchTooltip.show()
        # update search descriptions
        self.searchTooltip.setDescription("Showing search results for: "+searchPhrase)

        #initialize app theme
    def initializeAppTheme(self):
        settings = QSettings()
        current_theme=settings.value("THEME")
        #print("Current Theme is:", current_theme)
        self.populateThemeList(current_theme)

        # Connect  theme change signal
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)
    def populateThemeList(self,current_theme):
        theme_count=-1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            #check default theme
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count)#select the theme

    #change app theme
    def changeAppTheme(self):
        """change app theme based on user choice"""
        settings=QSettings()
        selected_theme=self.ui.themeList.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme: 
            #apply new Theme
            settings.setValue("THEME",selected_theme)
            QAppSettings.updateAppSettings(self.main,reloadJson=True)