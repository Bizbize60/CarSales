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
        self.main = MainWindow
        self.ui = MainWindow.ui

        self.mydb = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="your_database"
        )
        self.mycursor = self.mydb.cursor()

        self.initializeAppTheme()
        self.ui.searchBtn.clicked.connect(self.showSearchResults)
        self.carsTableshow()
        self.customerTableshow()
        self.rentTableshow()
        self.connectMenuButtons()

    def connectMenuButtons(self):
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.moreBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu())

        self.ui.RentNew.clicked.connect(lambda: self.insert_rent())
        self.ui.RentDelete.clicked.connect(lambda: self.delete_rent())
        self.ui.RentUpdate.clicked.connect(lambda: self.update_rent())
        self.ui.CarNew.clicked.connect(lambda: self.insert_car())
        self.ui.CarDelete.clicked.connect(lambda: self.delete_car())
        self.ui.CarUpdate.clicked.connect(lambda: self.update_car())
        self.ui.CustomerNew.clicked.connect(lambda: self.insert_customer())
        self.ui.CustomerUpdate.clicked.connect(lambda: self.update_customer())
        self.ui.CustomerDelete.clicked.connect(lambda: self.delete_customer())
    
    def carsTableshow(self):
        self.ui.carsTable.clearContents()
        self.ui.carsTable.setRowCount(50)
        self.mycursor.execute("SELECT * FROM Cars")
        result = self.mycursor.fetchall()
        for index, generalvalue in enumerate(result):
            for indexy, value in enumerate(generalvalue):
                self.ui.carsTable.setItem(index, indexy, QTableWidgetItem(str(value)))
        print("Tablo güncellendi.")

    def customerTableshow(self):
        self.ui.customerTable.clearContents()
        self.mycursor.execute("SELECT * FROM Customers")
        result = self.mycursor.fetchall()
        for index, generalvalue in enumerate(result):
            for indexy, value in enumerate(generalvalue):
                self.ui.customerTable.setItem(index, indexy, QTableWidgetItem(str(value)))

    def rentTableshow(self):
        self.ui.rentTable.clearContents()
        self.mycursor.execute("SELECT * FROM Rent")
        result = self.mycursor.fetchall()
        for index, generalvalue in enumerate(result):
            for indexy, value in enumerate(generalvalue):
                self.ui.rentTable.setItem(index, indexy, QTableWidgetItem(str(value)))

    def get_data(self):
        self.rent_id = self.ui.RentId.text()
        self.car_id = self.ui.CarId.text()
        self.customer_id = self.ui.CustomerId.text()
        self.damaged = self.ui.Damaged.text()
        self.firstdate = self.ui.FirstDate.text()
        self.enddate = self.ui.EndDate.text()
        self.price = self.ui.RentPrice.text()
        self.status = self.ui.Status_3.text()
        self.brand = self.ui.Brand.text()
        self.car_c_id = self.ui.CarIdTable.text()
        self.kilometer = self.ui.Kilometer.text()
        self.model = self.ui.Model.text()
        self.model_year = self.ui.ModelYear.text()
        self.plate = self.ui.Plate.text()
        self.age = self.ui.Age.text()
        self.customer_c_id = self.ui.CustomerId_2.text()
        self.customer_name = self.ui.CustomerName.text()
        self.license = self.ui.License.text()
        self.surname = self.ui.Surname.text()
        self.tc = self.ui.TC.text()

        if not self.rent_id:
            self.rent_id = None
        else:
            self.rent_id = int(self.rent_id)

        if not self.car_id:
            self.car_id = None
        else:
            self.car_id = int(self.car_id)

        if not self.customer_id:
            self.customer_id = None
        else:
            self.customer_id = int(self.customer_id)

        if not self.damaged:
            self.damaged = None
        else:
            if self.damaged.lower() == "damaged":
                self.damaged = True
            else:
                self.damaged = False

        if not self.enddate:
            self.enddate = None
        if not self.firstdate:
            self.firstdate = None
        if not self.price:
            self.price = None
        if not self.status:
            self.status = None
        def insert_rent(self):
        self.get_data()
        sql = "INSERT INTO Rent VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.rent_id, self.car_id, self.customer_id, self.status, self.price, self.damaged, self.firstdate, self.enddate)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.rentTableshow()

    def delete_rent(self):
        self.get_data()
        sql = "DELETE FROM Rent WHERE RentId = %s"
        self.mycursor.execute(sql, (self.rent_id,))
        self.mydb.commit()
        self.rentTableshow()

    def update_rent(self):
        self.get_data()
        if self.status:
            sql = "UPDATE Rent SET Status = %s WHERE RentId = %s"
            val = (self.status, self.rent_id)
            self.mycursor.execute(sql, val)
        if self.price:
            sql = "UPDATE Rent SET RentPrice = %s WHERE RentId = %s"
            val = (self.price, self.rent_id)
            self.mycursor.execute(sql, val)
        if self.firstdate:
            sql = "UPDATE Rent SET FirstDate = %s WHERE RentId = %s"
            val = (self.firstdate, self.rent_id)
            self.mycursor.execute(sql, val)
        if self.enddate:
            sql = "UPDATE Rent SET EndDate = %s WHERE RentId = %s"
            val = (self.enddate, self.rent_id)
            self.mycursor.execute(sql, val)
        if self.damaged:
            sql = "UPDATE Rent SET Status = %s WHERE RentId = %s"
            val = (self.damaged, self.rent_id)
            self.mycursor.execute(sql, val)
        if self.customer_id:
            sql = "UPDATE Rent SET CustomerId = %s WHERE RentId = %s"
            val = (self.customer_id, self.rent_id)
            self.mycursor.execute(sql, val)
        if self.car_id:
            sql = "UPDATE Rent SET CarId = %s WHERE RentId = %s"
            val = (self.car_id, self.rent_id)
            self.mycursor.execute(sql, val)

        self.mydb.commit()
        self.rentTableshow()

    def insert_car(self):
        self.get_data()
        sql = "INSERT INTO Cars VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.car_c_id, self.plate, self.brand, self.model, self.model_year, self.kilometer)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.carsTableshow()

    def delete_car(self):
        self.get_data()
        sql = "DELETE FROM Cars WHERE CarId = %s"
        self.mycursor.execute(sql, (self.car_c_id,))
        self.mydb.commit()
        self.carsTableshow()

    def update_car(self):
        self.get_data()
        if self.plate:
            sql = "UPDATE Cars SET PlateNumber = %s WHERE CarId = %s"
            val = (self.plate, self.car_c_id)
            self.mycursor.execute(sql, val)
        if self.brand:
            sql = "UPDATE Cars SET CarBrand = %s WHERE CarId = %s"
            val = (self.brand, self.car_c_id)
            self.mycursor.execute(sql, val)
        if self.model:
            sql = "UPDATE Cars SET CarModel = %s WHERE CarId = %s"
            val = (self.model, self.car_c_id)
            self.mycursor.execute(sql, val)
        if self.model_year:
            sql = "UPDATE Cars SET ModelYear = %s WHERE CarId = %s"
            val = (self.model_year, self.car_c_id)
            self.mycursor.execute(sql, val)
        if self.kilometer:
            sql = "UPDATE Cars SET Kilometer = %s WHERE CarId = %s"
            val = (self.kilometer, self.car_c_id)
            self.mycursor.execute(sql, val)

        self.mydb.commit()
        self.carsTableshow()

