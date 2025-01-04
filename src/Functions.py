import mysql.connector
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader
from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtWidgets import QTableWidgetItem
import time
class GuiFunctions():
    def __init__(self, MainWindow):
        self.main=MainWindow
        self.ui =MainWindow.ui

        ##############################################################
        #VERİTABANI İÇİN BAĞLANTI KODU BUNU DEĞİŞTİRMENİZ LAZIM

        
        ##############################################################
        #VERİTABANI İÇİN BAĞLANTI KODU BUNU DEĞİŞTİRMENİZ LAZIM

        

        self.mydb = mysql.connector.connect(
        host="192.168.1.7", #BATUNUN İP ADRESİ
        user="tunahan", #BURAK SANA BİR ÜYELİK OLUŞTURAMSI LAZIM BATU BANA OLUŞTURDUĞU GİBİ
        password="tuna60",#BATUNUN SANA OLUŞTURDIĞI ŞİFRE
        database="carrent"   #CARRENT
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

        self.carsTableshow()
        self.customerTableshow()
        self.rentTableshow()
        ######################3
        
        

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
        ############car tablosu
         self.ui.CarNew.clicked.connect(lambda:self.insert_car())
         self.ui.CarDelete.clicked.connect(lambda:self.delete_car())
         self.ui.CarUpdate.clicked.connect(lambda:self.update_car())

         self.ui.CustomerNew.clicked.connect(lambda:self.insert_customer())
         self.ui.CustomerUpdate.clicked.connect(lambda:self.update_customer())
         self.ui.CustomerDelete.clicked.connect(lambda:self.delete_customer())

    
    

    def carsTableshow(self):
        self.ui.carsTable.clearContents()
        self.ui.carsTable.setRowCount(50)

        self.mycursor.execute("Select * From Cars")
        result=self.mycursor.fetchall()
        for index,generalvalue in enumerate(result):
            for indexy,value in enumerate(generalvalue):
                self.ui.carsTable.setItem(index,indexy,QTableWidgetItem(str(value)))
        print("Tablo güncellendi.")
              
        
    def customerTableshow(self):
        self.ui.customerTable.clearContents()
        self.mycursor.execute("Select * from Customers")
        result=self.mycursor.fetchall()
        for index,generalvalue in enumerate(result):
            for indexy,value in enumerate(generalvalue):
                self.ui.customerTable.setItem(index,indexy,QTableWidgetItem(str(value)))
    def rentTableshow(self):
        self.ui.rentTable.clearContents()
        self.mycursor.execute("Select * from Rent")
        result=self.mycursor.fetchall()
        for index,generalvalue in enumerate(result):
            for indexy,value in enumerate(generalvalue):
                self.ui.rentTable.setItem(index,indexy,QTableWidgetItem(str(value)))

    #####Rentcardaki tüm bilgileri çekme
    def get_data(self):
        ##Rent
        self.rent_id=self.ui.RentId.text()
        self.car_id=self.ui.CarId.text()
        self.customer_id=self.ui.CustomerId.text()
        self.damaged=self.ui.Damaged.text()
        self.firstdate=self.ui.FirstDate.text()
        self.enddate=self.ui.EndDate.text()
        self.price=self.ui.RentPrice.text()
        self.status=self.ui.Status_3.text()


        ##car
        self.brand=self.ui.Brand.text()
        self.car_c_id=self.ui.CarIdTable.text()
        self.kilometer=self.ui.Kilometer.text()
        self.model=self.ui.Model.text()
        self.model_year=self.ui.ModelYear.text()
        self.plate=self.ui.Plate.text()



        ##customer
        self.age=self.ui.Age.text()
        self.customer_c_id=self.ui.CustomerId_2.text()
        self.customer_name=self.ui.CustomerName.text()
        self.license=self.ui.License.text()
        self.surname=self.ui.Surname.text()
        self.tc=self.ui.TC.text()


        

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
             self.customer_id=int(self.customer_id)
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

        self.rentTableshow()
    def delete_rent(self):
        self.get_data()
        sql=f"DELETE FROM Rent Where RentId = %s" ###querylerle aynı olacak sadece verilerin yerine %s koyacaksınız
        self.mycursor.execute(sql,(self.rent_id,))
        self.mydb.commit()
        
        self.rentTableshow()
        
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

        self.rentTableshow()
    def insert_car(self):
        self.get_data()
        sql="INSERT INTO Cars Values (%s, %s, %s, %s, %s, %s)"
        val=(self.car_c_id,self.plate,self.brand,self.model,self.model_year,self.kilometer)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        self.carsTableshow()


    def delete_car(self):
        self.get_data()
        sql = "DELETE FROM Cars WHERE CarId = %s"
        self.mycursor.execute(sql, (self.car_c_id,))
        self.mydb.commit()
        print("Silme işlemi başarılı.")
        
        self.carsTableshow()  # Tabloyu yenile


   
    
    def update_car(self):
        self.get_data()
        print("plaka")
        if self.plate:
            
            sql="UPDATE Cars SET PlateNumber = %s WHERE CarId = %s"
            val=(self.plate,self.car_c_id)
            self.mycursor.execute(sql,val)
        if self.brand:
            sql="UPDATE Cars SET CarBrand = %s WHERE CarId = %s"
            val=(self.brand,self.car_c_id)
            self.mycursor.execute(sql,val)
        if self.model:
            sql="UPDATE Cars SET CarModel = %s WHERE CarId = %s"
            val=(self.model,self.car_c_id)
            self.mycursor.execute(sql,val)
        if self.model_year:
            sql="UPDATE Cars SET ModelYear = %s WHERE CarId = %s"
            val=(self.model_year,self.car_c_id)
            self.mycursor.execute(sql,val)
        if self.kilometer:
            sql="UPDATE Cars SET kilometer = %s WHERE CarId = %s"
            val=(self.kilometer,self.car_c_id)
            self.mycursor.execute(sql,val)
        self.mydb.commit()  
        self.carsTableshow()

        
    def insert_customer(self):
        self.get_data()
        sql="INSERT INTO Customers Values (%s, %s, %s, %s, %s, %s)"
        val=(self.customer_c_id,self.customer_name,self.surname,self.age,self.license,self.tc)
        self.mycursor.execute(sql,val)

        self.mydb.commit()  

        self.customerTableshow()
    def delete_customer(self):
        self.get_data()
        sql=f"DELETE FROM Customers Where CustomerId = %s" ###querylerle aynı olacak sadece verilerin yerine %s koyacaksınız
        self.mycursor.execute(sql,(self.customer_c_id,))
        
        self.mydb.commit()
      
        self.customerTableshow()
    def update_customer(self):
        self.get_data()

        if self.customer_name:
            sql="UPDATE Customers SET CustomerName = %s WHERE CustomerId = %s"
            val=(self.customer_name,self.customer_c_id)
            self.mycursor.execute(sql,val)
        
        if self.surname:
            sql="UPDATE Customers SET CustomerSurname = %s WHERE CustomerId = %s"
            val=(self.surname,self.customer_c_id)
            self.mycursor.execute(sql,val)

        if self.age:
            sql="UPDATE Customers SET Age = %s WHERE CustomerId = %s"
            val=(self.age,self.customer_c_id)
            self.mycursor.execute(sql,val)
        if self.license:
            sql="UPDATE Customers SET DriverLicenseType = %s WHERE CustomerId = %s"
            val=(self.license,self.customer_c_id)
            self.mycursor.execute(sql,val)
        if self.tc:
            sql="UPDATE Customers SET TCNO = %s WHERE CustomerId = %s"
            val=(self.tc,self.customer_c_id)
            self.mycursor.execute(sql,val)
        self.mydb.commit()      

        self.customerTableshow()

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
        self.resultshowed=""
        self.current_index = self.ui.mainPages.currentIndex()
       
        self.searchPhrase = [self.ui.searchInp.text()]
        if not self.searchPhrase:
             return 
        try:
                self.searchTooltip.show()
        except:
                #re-init
                self.createSearchTipOverlay()
                self.searchTooltip.show()
        if self.current_index == 0 :
            sql="Select * From Rent Where rentId = %s"
            val=self.searchPhrase
            self.mycursor.execute(sql,val)
            result=self.mycursor.fetchall()
            
            for i in result:
                self.resultshowed=self.resultshowed+str(i)
            
        elif self.current_index == 1:
            sql="Select * From Customers Where CustomerId = %s"
            val=self.searchPhrase
            self.mycursor.execute(sql,val)
            result=self.mycursor.fetchall()
            
            for i in result:
                self.resultshowed=self.resultshowed+str(i)
                
                
            
        elif self.current_index == 3:
            sql="Select * From Cars Where CarId = %s"
            val=self.searchPhrase
            self.mycursor.execute(sql,val)
            result=self.mycursor.fetchall()
            
            for i in result:
                self.resultshowed=self.resultshowed+str(i)
        print(self.resultshowed)
        self.searchTooltip.setDescription("Showing search results for: "+ self.resultshowed)
        
        # update search descriptions
        

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
