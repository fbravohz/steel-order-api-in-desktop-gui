# This Python file uses the following encoding: utf-8
import sys
import pandas as pd

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QLabel,
    QScrollBar,
    QDialog,
    QTableWidgetItem
    )
from PySide2.QtCore import Signal, QObject, Slot, QMetaMethod, Qt
from PySide2.QtGui import QBrush, QColor, QPixmap
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_buttonsWindow import Ui_Dialog
from steel_order_api_pandas import steel_order_api_pandas
import pandas_api_to_pyside

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        #Main lines of code to make the main window work
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Make the window maximizable and minimizable
        self.setWindowFlag(Qt.WindowMaximizeButtonHint,True)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint,True)
        
        #data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
        my_steel_order_api = steel_order_api_pandas()
        data: pd.DataFrame = my_steel_order_api.request_product(7872468)
        self.SetTableWidgetFromPandas(data)
        #self.ui.pushButton.clicked.connect(self.openDialog)
        item =self.ui.tableWidget.item(0,0)
        color = QColor(125,125,125)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(color)
        
        def background():
            item.setBackground(brush)
        
        self.ui.pushButton_save.clicked.connect(background)
        self.ui.pushButton_clear.clicked.connect(self.clear_table_widget_data)
        
        self.set_combo_box_origin()
        self.ui.comboBox_destiny.setDisabled(True)

    #Open dialog with buttons accept and cancel
    def openDialog(self):
        #we define the "window" property with the QDialog instance
        #In this case is a QDialog because the window is a Dialog, otherwise would be QMainWindow
        self.window2 = QDialog()
        #We assign an instance of the class container of the designed dialog
        self.ui = Ui_Dialog()
        #We set up the ui by passing the argument of the current object for window
        self.ui.setupUi(self.window2)
        #Run the window.show()
        self.window2.show()

    def SetTableWidgetFromPandas(self, data: pd.DataFrame):

        # Column Headers
        def SetColumnHeaders():
            #column_indexes = data.columns
            self.ui.tableWidget.setColumnCount(data.shape[1])
            self.ui.tableWidget.setHorizontalHeaderLabels(data.columns)
            self.ui.tableWidget.resizeColumnsToContents()

        #Row Headers
        def SetRowHeaders():
            self.ui.tableWidget.setRowCount(data.shape[0])
            #Use the line below if you want to use a column data as row header
            #self.ui.tableWidget.setVerticalHeaderLabels(data['Name'])
            self.ui.tableWidget.resizeRowsToContents()

        #Set table data
        def SetTableData():
            for rows in range(data.shape[0]):
                for cols in range(data.shape[1]):
                    item = QTableWidgetItem()
                    item.setText(str(data.iloc[rows,cols]))
                    self.ui.tableWidget.setItem(rows,cols,item)
        #Calling previusly defined functions
        SetColumnHeaders()
        SetRowHeaders()
        SetTableData()

    def set_combo_box_origin(self):
        temp_df_warehouses = steel_order_api_pandas().request_warehouses()
        temp_list = pandas_api_to_pyside.from_dataframe_get_warehouses_combobox(temp_df_warehouses)
        self.ui.comboBox_origin.insertItem(0,"")
        self.ui.comboBox_origin.insertItems(1,temp_list)
        self.ui.comboBox_origin.currentTextChanged.connect(self.set_combo_box_destiny)

    def set_combo_box_destiny(self):
        self.ui.comboBox_destiny.clear()
        if(self.ui.comboBox_origin.currentIndex() != 0):
            self.ui.comboBox_destiny.setEnabled(True)
        elif(self.ui.comboBox_origin.currentIndex() == 0):
            self.ui.comboBox_destiny.setEnabled(False)
        list_destiny = []
        for i in range(self.ui.comboBox_origin.count()):
            if self.ui.comboBox_origin.currentIndex() != i:
                if self.ui.comboBox_origin.itemText(i) != "":
                    list_destiny.append(self.ui.comboBox_origin.itemText(i))
        self.ui.comboBox_destiny.insertItem(0,"")
        self.ui.comboBox_destiny.insertItems(1,list_destiny)

    def clear_table_widget_data(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(0)

    def pull_table_widget_data(self):
        pass

    def save_table_widget_data(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())

