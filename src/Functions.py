import mysql.connector
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

        ##############################################################
        #VERİTABANI İÇİN BAĞLANTI KODU BUNU DEĞİŞTİRMENİZ LAZIM

        
        ##############################################################
        #VERİTABANI İÇİN BAĞLANTI KODU BUNU DEĞİŞTİRMENİZ LAZIM

        

        self.mydb = mysql.connector.connect(
        host="localhost", #BATUNUN İP ADRESİ
        user="yourusername", #BURAK SANA BİR ÜYELİK OLUŞTURAMSI LAZIM BATU BANA OLUŞTURDUĞU GİBİ
        password="yourpassword",#BATUNUN SANA OLUŞTURDIĞI ŞİFRE
        database="mydatabase"   #CARRENT
        )

        self.mycursor = self.mydb.cursor()


        ###########################################################3
        ########################################################################
        


        ###########################################################3
        ########################################################################

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
            ##### tuşlara basınca hangi fonksiyonu çalıştırcağını seçiyor bunun için ben butopnların adını ne yaptım bilmeniz lazım onu da gruba attom Qpushbuttonların adına bakın
         self.ui.RentNew.clicked.connect(lambda:self.insert_rent())
         self.ui.RentDelete.clicked.connect(lambda:self.delete_rent())
         self.ui.RentUpdate.clicked.connect(lambda:self.update_rent())


    #####Rentcardaki tüm bilgileri çekme
    def get_data(self):
         
        self.rent_id=self.ui.RentId.text()
        self.car_id=self.ui.CarId.text()
        self.customer_id=self.ui.CustomerId.text()
        self.damaged=self.ui.Damaged.text()
        self.firstdate=self.ui.FirstDate.text()
        self.enddate=self.ui.EndDate.text()
        self.price=self.ui.RentPrice.text()
        self.status=self.ui.Status_3.text()

        

        if not self.rent_id:
              self.rent_id=None
        else:
             self.rent_id=int(self.rent_id)
        
        if not self.car_id:
             self.car_id=None
        else:
             self.car_id=int(self.car_id)
        if not self.customer_id:
             self.customer_id=None
        else:
             self.customer_id_id=int(self.customer_id)
        if not self.damaged:
             self.damaged=None
        else:
            if self.damaged== "damaged" or self.damaged== "Damaged":
                self.damaged=True
            else:
                self.damaged=False
        
        if not self.enddate:
             self.enddate=None
        if not self.firstdate:
             self.firstdate=None
        if not self.price:
             self.price=None
        if not self.status:
             self.status=None
         
    def insert_rent(self):
        self.get_data()  # Verileri al
        sql="INSERT INTO Rent Values (%s, %s, %s, %s, %s, %s, %s, %s)"
        val=(self.rent_id,self.car_id,self.customer_id,self.status,self.price,self.damaged,self.firstdate,self.enddate)
        self.mycursor.execute(sql,val)

        self.mydb.commit()
    def delete_rent(self):
        self.get_data()
        sql=f"DELETE FROM Rent Where RentId = %s" ###querylerle aynı olacak sadece verilerin yerine %s koyacaksınız
        self.mycursor.execute(sql,(self.rent_id,))
        
        self.mydb.commit()
        
    def update_rent(self):
        self.get_data()

        if self.status:
            sql="UPDATE Rent SET Status = %s WHERE rentId = %s"
            val=(self.status,self.rent_id)

            self.mycursor.execute(sql,val)
        if self.price:
            sql="UPDATE Rent SET RentPrice = %s WHERE rentId = %s"
            val=(self.price,self.rent_id)

            self.mycursor.execute(sql,val)
        if self.firstdate:
            sql="UPDATE Rent SET FirstDate = %s WHERE rentId = %s"
            val=(self.firstdate,self.rent_id)

            self.mycursor.execute(sql,val)
        if self.enddate:
            sql="UPDATE Rent SET EndDate = %s WHERE rentId = %s"
            val=(self.enddate,self.rent_id)

            self.mycursor.execute(sql,val)
        if self.damaged:
            sql="UPDATE Rent Set Status = %s Where rentId = %s"
            val=(self.damaged,self.rent_id)

            self.mycursor.execute(sql,val)
        if self.customer_id:
            sql="UPDATE Rent Set CustomerId = %s Where rentId = %s"
            val=(self.customer_id,self.rent_id)

            self.mycursor.execute(sql,val)
        if self.car_id:
            sql="UPDATE Rent Set CarId = %s Where rentId = %s"
            val=(self.car_id,self.rent_id)

            self.mycursor.execute(sql,val)

        self.mydb.commit()
             
             
              

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