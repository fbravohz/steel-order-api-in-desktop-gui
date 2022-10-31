# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#     pyside2-uic ui\mainwindow.ui -o ui\ui_mainwindow.py

from cgitb import text
from gc import isenabled
from http import client
from math import prod
from msilib.schema import Dialog
from operator import truediv
import sys
from typing import Type
import pandas as pd
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QLabel,
    QScrollBar,
    QDialog,
    QTableWidgetItem,
    QComboBox,
    QMessageBox,
    QPushButton,
    QStyle
)
from PySide2.QtCore import (
    Signal,
    QObject,
    Slot,
    QMetaMethod,
    Qt
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QPixmap
)
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_warehouse_alert import Ui_Dialog
from ui.ui_no_stock import Ui_DialogNoStock
from SteelOrderToPandas import SteelOrderToPandas
from PandasToPyside import PandasToPyside
import time

class MainWindow(QMainWindow):
    """This class inherits the QMainWindow class. It contains the base design
    of the application from the ui_mainwindow.py file.

    Args:
        QMainWindow (_type_): The QMainWindow class to apply from.
    """

    def __init__(self, parent=None):
        """Executes the main process and calls all the methods that are going
        to be used for the user interface.

        Args:
            parent (_type_, optional):Receives a parent to be linked.
            Defaults to None.
        """
        # Lines of code to make the main window work
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Class attributes that hold the current warehouses selection
        self.current_origin = ""
        self.current_destiny = ""

        # Make the window maximizable and minimizable
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)

        # Set the comboboxes with warehouses names
        self.set_combo_box_origin()
        self.ui.comboBox_destiny.setDisabled(True)

        # Signal catching section
        self.ui.pushButton_save.clicked.connect(self.table_save_data)
        self.ui.pushButton_pull.clicked.connect(self.table_pull_data)

        # Catches the signal of cellChanged and calls self.cell_changed method
        self.ui.tableWidget.cellChanged.connect(self.cell_changed)

        # Catches the signals when the user has an active warehouses transfer
        # and creates a confirmation if user really wants to discard changes
        self.ui.comboBox_origin.activated.connect(self.change_warehouse_selection)
        self.ui.comboBox_destiny.activated.connect(self.change_warehouse_selection)


    def cell_changed(self, row: int, col: int):
        """This method evaluates if the changed cell is selected by user,\n
        and then performs the corresponding operations.\n
        If it is not selected by user, means the cell has been changed by\n
        an algorithmic way and it will be ignored.\n

        Args:
            row (int): receives the row number
            col (int): receives the column number
        """

        # Gets the QTableWidgetItem in the (row, col) position
        table_item = self.ui.tableWidget.item(row,col)

        # Ask if the item in the received cordinates is selected
        selected = self.ui.tableWidget.isItemSelected(table_item)

        # If it is selected, perform evaluations and operations
        if selected:
            self.table_evaluate_cell_changed(row,col)
        # Otherwise it will be ignored


    def change_warehouse_selection(self):
        """A function that asks the user if he wants to discard his changes\n
        when he selects another warehouses transfer transaction, if he doesn't\n
        resets the warehouses selection to the previous state.
        """
        # Evaluate one of two conditions are true (OR)
        # each of them should be an (AND) condition
        # The first is that current index in combobox origin is diff to zero
        # AND the class attribute: current_origin is diff to current text in
        # combobox origin
        # OR the current index in combobox destiny is diff to zero
        # AND the class attribute: current_destiny is diff to current text in
        # combobox destiny
        if ((self.ui.comboBox_origin.currentIndex() != 0 and
            self.current_origin != self.ui.comboBox_origin.currentText()) or
            (self.ui.comboBox_destiny.currentIndex() != 0 and
            self.current_destiny != self.ui.comboBox_destiny.currentText())):

            # Evaluate that class attributes: current_origin and current_destiny
            # are different to "" empty string
            if (self.current_origin != "" and self.current_destiny != ""):

                # Calls the message box to ask if the user wants to discard
                # changes to the current transfer wh1 ➡ wh2
                self.open_messagebox_change_warehouse(
                    self.current_origin, self.current_destiny)

                # if the user rejected to discard changes, then reset the
                # warehouses selection to the last pulled, it is current_origin
                # and current_destiny class attributes.
                if self.messagebox_change_warehouse.result() != 1024:
                    self.ui.comboBox_origin.setCurrentText(self.current_origin)
                    self.ui.comboBox_destiny.setCurrentText(self.current_destiny)

                # If the user choose to discard changes, then the table is cleared
                # and the class attributes current_destiny and origin are cleared
                # last, the label that contains the current transfer is cleared
                else:
                    self.ClearTableWidgetData()
                    self.current_destiny = ""
                    self.current_origin = ""
                    self.ui.label_current_warehouses.setText("")


    def set_table_from_dataframe(self, data: pd.DataFrame):
        """Create and fill a table that contains the given dataframe in a\n
        QTableWidget. If there is a table already, it is cleared, and a new\n
        one is set. It also controls the animation of refreshing a table and\n
        the progress bar animation. Finally, it also handles with empty\n
        dataframes and controls the labels that inform this issues.

        Args:
            data (pd.DataFrame): Receives a pandas dataframe containing the\n
            information to fill the table.
        """
        self.ClearTableWidgetData()

        def set_table_data():
            """_summary_
            """
            self.ui.label_loading.setText("Cargando...")
            self.ui.progressBar.setValue(0)

            for rows in range(data.shape[0]):
                for cols in range(data.shape[1]):
                    item = QTableWidgetItem()
                    # if (cols == 6):
                    #     c_box = QComboBox()
                    #     c_box.insertItems(0,["","AMEU","C-LEGRAC","ETC"])
                    #     #item.setText(str(data.iloc[rows, cols]))
                    #     self.ui.tableWidget.setCellWidget(rows,cols,c_box)
                    #     #self.ui.tableWidget.setItem(rows, cols, item)
                    # else:
                    item.setText(str(data.iloc[rows, cols]))
                    if (cols != 5 and cols != 7 and cols != 8):
                        item.setFlags(Qt.ItemIsEditable)
                    self.ui.tableWidget.setItem(rows, cols, item)
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.resizeRowsToContents()

        def WaitAnimation():
            for i in range(0, 100, 5):
                time.sleep(0.01)
                curr_value = self.ui.progressBar.value()
                self.ui.progressBar.setValue(curr_value+5)
            self.ui.label_loading.setText("")

        self.ui.tableWidget.setRowCount(data.shape[0])
        self.ui.tableWidget.setColumnCount(data.shape[1])
        self.ui.tableWidget.setHorizontalHeaderLabels(data.columns)

        set_table_data()
        WaitAnimation()

        # This helps when the selected warehouse is empty and then
        # it got an empty dataframe. It asks the user to select a warehouse.
        if (self.ui.tableWidget.columnCount() == 1
                and self.ui.tableWidget.rowCount() == 0):
            self.ui.label_loading.setText("Selecciona almacén destino.")
            self.ui.progressBar.setValue(0)


    def set_combo_box_origin(self):
        sotp = SteelOrderToPandas()
        warehouses = sotp.request_warehouses()

        # If the warehouses['name'] key doesn't exist, means that the apikey
        # was rejected and needs to be verified
        try:
            warehouses_list = warehouses['name'].to_list()

        # The KeyError exception is raised, and a message is send. Exit the program.
        except KeyError:
            self.open_messagebox_no_key_name(sotp.status_code)
            exit()

        self.ui.comboBox_origin.insertItem(0, "")
        self.ui.comboBox_origin.insertItems(1, warehouses_list)
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
        self.ui.comboBox_destiny.insertItem(0, "")
        self.ui.comboBox_destiny.insertItems(1, list_destiny)


    def ClearTableWidgetData(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(0)


    def table_pull_data(self):

        self.ui.pushButton_save.setStyleSheet("")

        txt_cmbx_dny = self.ui.comboBox_destiny.currentText()
        txt_cmbx_ogn = self.ui.comboBox_origin.currentText()

        pandas_pyside = PandasToPyside()

        kind_ogn = pandas_pyside.ORIGIN
        kind_dny = pandas_pyside.DESTINY

        self.data_ogn = pandas_pyside.get_products_by_warehouse(txt_cmbx_ogn,kind_ogn)
        self.data_dny = pandas_pyside.get_products_by_warehouse(txt_cmbx_dny,kind_dny)

        self.set_table_from_dataframe(data=self.data_dny)

        # Class attributes that are going to be accesed outside the function
        # contains the names of the current origin and destiny warehouses
        self.current_origin = txt_cmbx_ogn
        self.current_destiny = txt_cmbx_dny

        # Setting text for label_current_warehouses in current transfer selection
        TXT = f'Transfiriendo:\n{self.current_origin} ➡ {self.current_destiny}'
        self.ui.label_current_warehouses.setText(TXT)


    def table_get_current_data(self):

        num_cols = self.ui.tableWidget.columnCount()
        num_rows = self.ui.tableWidget.rowCount()

        current_dataframe = pd.DataFrame(columns=['id-almacen','id-producto','codigo','nombre','presente','traspaso',
                                        'futuro','error','codigo-error'],
                                        index=range(num_rows))

        for col  in range(num_cols):
            for row in range(num_rows):
                current_dataframe.iloc[row,col] = self.ui.tableWidget.item(row,col).data(0)
        current_dataframe = current_dataframe.sort_values(by=['codigo'],ignore_index=True)
        self.data_dny = current_dataframe


    def table_save_data(self):

        self.table_get_current_data()
        pandas_to_pyside = PandasToPyside()
        success = pandas_to_pyside.put_warehouses_products(self.data_ogn,self.data_dny)
        #In the end this should call the pull table widget to refresh changes
        if success:
            self.ui.pushButton_pull.click()
            self.ui.pushButton_save.setStyleSheet("color: #005014")
        else:
            self.ui.pushButton_save.setStyleSheet("color: #740000")


    def table_evaluate_cell_changed(self,row,col):

        def error_add():
            present_row = int(self.ui.tableWidget.item(row,4).text())
            transfer_row = int(self.ui.tableWidget.item(row,5).text())
            error_row = int(self.ui.tableWidget.item(row,7).text())
            future_row = present_row + transfer_row + error_row
            self.ui.tableWidget.item(row,6).setText(str(future_row))


        def error_subs(data: pd.DataFrame):

            for error_code in data['error-code']:

                if(not data.empty):
                    mask = data['error-code'] == error_code
                    to_subs = data[mask].loc[:,'error-amount'].sum()

                    for i in range(self.ui.tableWidget.rowCount()):
                        product = self.ui.tableWidget.item(i,2).text()

                        if(error_code == product):
                            present_row = int(self.ui.tableWidget.item(i, 4).text())
                            transfer_row = int(self.ui.tableWidget.item(i, 5).text())
                            error_row = int(self.ui.tableWidget.item(i, 7).text())
                            future_row = present_row + transfer_row + error_row - to_subs
                            # if(future_row < 0):
                            #     self.open_messagebox_no_stock(self.current_destiny, product, present_row, future_row, "destino")
                            #     if(self.messagebox_no_stock.result() != 1024):
                            #         future_row = present_row + transfer_row + error_row
                            #         self.ui.tableWidget.item(i, 6).setText(str(future_row))
                            #         self.ui.tableWidget.item(row, 7).setText(str(0))
                            #         return
                            self.ui.tableWidget.item(i, 6).setText(str(future_row))

                    indexes = data[mask].loc[:,'error-amount'].index.to_list()
                    data = data.drop(indexes)


            # This process runs a for cicle because is executed in every
            # cell change, in order to catch any minimal modification.
        def error_code_handler():
            errors = {"error-code":[], "error-amount": []}
            for i in range(self.ui.tableWidget.rowCount()):
                error_code = self.ui.tableWidget.item(i,8).text()
                if(error_code != ""):
                    error_amount = int(self.ui.tableWidget.item(i,7).text())
                    errors["error-code"].append(str(error_code))
                    errors["error-amount"].append(error_amount)
                else:
                    pass
            errors = pd.DataFrame(errors)
            error_add()
            error_subs(errors)


    # This proccess will be executed only when modified column is 5 and will
    # check if the cell is currently selected has happened just before
    # editing. Otherwise means that the cell wasn't modified by a user
    # but by the algorithm.
        if(col == 5):

            # This statement ensures that when you delete data on cell,
            # it becomes 0
            if self.ui.tableWidget.item(row,5).text() == "":
                self.ui.tableWidget.item(row,5).setText(str(0))
            # Initialize destiny local variables
            dny_transfer = 0
            dny_present = 0
            # Evaluate if the transfer amount in destiny table contains non
            # numeric types
            try:
                dny_transfer = int(self.ui.tableWidget.item(row,5).text())
                # If the amount to transfer is negative, throws a messagebox
                # and sets the cell changed to zero
                if dny_transfer < 0:
                    self.open_messagebox_negative_number()
                    self.ui.tableWidget.item(row,col).setText(str(0))
                    return
            # If a non numeric value is present an exception is raised
            except ValueError:
                # Opens a dialog with a warning of a non numeric value
                self.open_messagebox_value_error(
                    str(self.ui.tableWidget.item(row,col).data(0)))
                # Set the wrong value to zero in the table and in the local
                # variable dny_transfer
                self.ui.tableWidget.item(row,col).setText(str(0))

            # Gets the full-reference string of the modified product stored
            # in column 0
            for i in range(self.ui.tableWidget.columnCount()):
                header_item: QTableWidgetItem
                header_item = self.ui.tableWidget.horizontalHeaderItem(i)
                if(header_item.text() == 'codigo'):
                    dny_transfer_product = str(
                        self.ui.tableWidget.item(row,i).data(0))

            # Create a mask or filter, in order to find the cells
            # that contain the full-reference of product in the origin
            # dataframe this helps a lot because doesn't matter how
            # unorganized are the QTableWidget data, we will always
            # find the correct row to modify with the given
            # dny_transfer_product
            mask = self.data_ogn.loc[:,'codigo'] == dny_transfer_product

            # Receive the value of the index for the first incidence
            idx = self.data_ogn[mask].index.values[0]

            # With the given index we put the value of the received amount
            # to transfer into the data origin dataframe,
            # but multiplied by (-) minus so a positive transfer in
            # warehouse B is a negative in warehouse A
            self.data_ogn.at[idx,'traspaso'] = (-(dny_transfer))

            # Cast the values of the dataframe of columns 'presente'
            # and 'traspaso'
            ogn_present = int(str(self.data_ogn.loc[idx,'presente']))
            ogn_transfer = int(str(self.data_ogn.loc[idx,'traspaso']))

            # Puts the value of the sum of the current stock plus the transfer
            # the transfer is gonna take from the present and assing all
            # the sum into the column 'futuro'
            self.data_ogn.at[idx,'futuro'] = ogn_present + ogn_transfer

            # Store the new 'futuro' column's value into local variable
            ogn_future = int(str(self.data_ogn.at[idx,'futuro']))

            # Assign the destiny present value into local variable
            dny_present = int(self.ui.tableWidget.item(row,col-1).data(0))

            # Evaluate if the future value of origin dataframe is
            # less equal to 0
            if(self.data_ogn.at[idx,'futuro'] < 0):

                # Opens a messagebox with the warning of insuficient stock
                self.open_messagebox_no_stock(
                    self.ui.comboBox_origin.currentText(),
                    dny_transfer_product,
                    str(ogn_present),
                    str(ogn_future),
                    "origen")

                # The result code of opening this messagebox should be
                # 1024 if accepted
                if self.messagebox_no_stock.result() == 1024:

                    # We have permission to transfer
                    self.ui.tableWidget.item(row,col+1).setText(
                        (str(dny_present + dny_transfer)))

                # If the code is other, we will set the following
                else:

                    # The QWidgetTable.item(row,col) which is the value
                    # of dny_transfer
                    # is set to zero
                    self.ui.tableWidget.item(row,col).setText(str(0))
                    # The QWidgetTable.item(row,col+1) which is the value
                    # corresponding to dny_future
                    # is set to QWidgetTable.item(row,col-1) which is the
                    # value of dny_present
                    self.ui.tableWidget.item(row,col+1).setText(
                        str(self.ui.tableWidget.item(row,col-1).text()))

            # If the future value of origin is higher than 0,
            # we have permission to transfer
            else:
                self.ui.tableWidget.item(row,col+1).setText(
                    (str(dny_present + dny_transfer)))

        # This statement will help us to catch typing errors
        # specifically from the column 7.
        if(col == 7):

            # This statement ensures that when you delete data on cell,
            # it becomes 0
            if self.ui.tableWidget.item(row,7).text() == "":
                # Sets the error number to zero
                self.ui.tableWidget.item(row,7).setText(str(0))

            # Evaluate if the error amount contains non numeric types
            try:
                error = int(self.ui.tableWidget.item(row,7).text())
                # If the error amount is negative
                if error < 0:
                    # Throws a messagebox and sets the cell changed to zero
                    self.open_messagebox_negative_number()
                    self.ui.tableWidget.item(row,7).setText(str(0))
                    return

            # If a non numeric value is present,
            # an exception is raised of type ValueError
            except ValueError:
                # Opens a dialog with a warning of a non numeric value
                self.open_messagebox_value_error(
                    str(self.ui.tableWidget.item(row,col).text()))
                # Set the wrong value to zero in the table
                self.ui.tableWidget.item(row,col).setText(str(0))

            # Evaluates that there is an error code, in the same row of
            # the error number
            if (self.ui.tableWidget.item(row,8).text() == "" and
                int(self.ui.tableWidget.item(row,7).text()) != 0):
                # If not, opens a messagebox asking for error code first
                self.open_messagebox_select_errorcode_first()
                # Sets the error number to zero
                self.ui.tableWidget.item(row, 7).setText(str(0))


        if(col == 8):
            found_row: int = -1
            if(self.ui.tableWidget.item(row,8).text() != ""):
                code_to_find = self.ui.tableWidget.item(row,8).text()
                for i in range(self.ui.tableWidget.rowCount()):
                    iterated_text = self.ui.tableWidget.item(i,2).text()
                    if iterated_text == code_to_find:
                        found_row = i
                        break
                if found_row == -1:
                    self.open_messagebox_error_code_not_found(code_to_find)
                    self.ui.tableWidget.item(row,8).setText("")
                    self.ui.tableWidget.item(row,7).setText(str(0))

            # Messagebox for product equals error-code
            if(self.ui.tableWidget.item(row,8).text() == self.ui.tableWidget.item(row,2).text()):
                self.open_messagebox_errorcode_is_self()
                self.ui.tableWidget.item(row, 8).setText("")
                self.ui.tableWidget.item(row, 7).setText(str(0))


        if(col == 5 or col == 7 or col == 8):
            error_code_handler()

            # if (find_error_code() != -1):
            #     if(self.ui.tableWidget.item(row,col-1))
            # if(self.ui.tableWidget.item(row,col).text() != ""):
            #     print(self.ui.tableWidget.item(row,col).text())

        #if((col == 8 or col ==7) and (self.ui.tableWidget.item(row,col).text() != )):



    # Open dialog with button ok
    def open_messagebox_value_error(self, word: str):
        self.messagebox_value_error = QMessageBox()
        self.messagebox_value_error.setWindowTitle("Error de valor")
        self.messagebox_value_error.setText(f"Error: \"{word}\" no es de tipo númerico.")
        self.messagebox_value_error.setIcon(QMessageBox.Warning)
        self.messagebox_value_error.setStandardButtons(QMessageBox.Ok)
        self.messagebox_value_error.exec_()


        # Open dialog with button ok and cancel
    def open_messagebox_no_stock(self, warehouse_ogn: str, product: str, current_stock: str, final_stock: str, kind: str):
        self.messagebox_no_stock = QMessageBox()
        self.messagebox_no_stock.setWindowTitle("Stock insuficiente")
        string_format = f"El almacen de {kind} {warehouse_ogn} con {current_stock} unidades de {product} quedará con {final_stock} al finalizar la operación. ¿Desea continuar?"
        self.messagebox_no_stock.setText(string_format)
        self.messagebox_no_stock.setIcon(QMessageBox.Warning)
        self.messagebox_no_stock.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        self.messagebox_no_stock.exec_()


    # Open dialog with button ok
    def open_messagebox_forbidden(self):
        self.messagebox_forbidden = QMessageBox()
        self.messagebox_forbidden.setWindowTitle("Prohibido")
        self.messagebox_forbidden.setText(f"Se alcanzó el limite de peticiones por minuto/día al servidor")
        self.messagebox_forbidden.setIcon(QMessageBox.Warning)
        self.messagebox_forbidden.setStandardButtons(QMessageBox.Ok)
        self.messagebox_forbidden.exec_()


    def open_messagebox_negative_number(self):
        self.messagebox_forbidden_negative = QMessageBox()
        self.messagebox_forbidden_negative.setWindowTitle("Prohibido")
        self.messagebox_forbidden_negative.setText(f"No se permite hacer traspasos negativos.")
        self.messagebox_forbidden_negative.setIcon(QMessageBox.Warning)
        self.messagebox_forbidden_negative.setStandardButtons(QMessageBox.Ok)
        self.messagebox_forbidden_negative.exec_()


    def open_messagebox_no_key_name(self, status_code: int):
        self.messagebox_no_key_name = QMessageBox()
        self.messagebox_no_key_name.setWindowTitle("API Key incorrecta")
        self.messagebox_no_key_name.setText(f"Falló la autenticación.\nError del servidor: {status_code}.")
        self.messagebox_no_key_name.setIcon(QMessageBox.Warning)
        self.messagebox_no_key_name.setStandardButtons(QMessageBox.Ok)
        self.messagebox_no_key_name.exec_()


    def open_messagebox_change_warehouse(self, warehouse_ogn: str, warehouse_dny: str):
        """A function that opens a MessageBox asking the user to confirm and
        discard the current changes or continue with current state.

        Args:
            warehouse_ogn (str): the string of current origin warehouse
            warehouse_dny (str): the string of current destiny warehouse
        """
        self.messagebox_change_warehouse = QMessageBox()
        self.messagebox_change_warehouse.setWindowTitle("Cambio de almacén")
        TXT = '¿Estas seguro que deseas descartar los cambios actuales en'\
            + f' traspaso:\n {warehouse_ogn} ➡ {warehouse_dny}?'
        self.messagebox_change_warehouse.setText(TXT)
        self.messagebox_change_warehouse.setIcon(QMessageBox.Warning)
        self.messagebox_change_warehouse.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        self.messagebox_change_warehouse.exec_()


    def open_messagebox_error_code_not_found(self, code: int):
        self.messagebox_error_code_not_found = QMessageBox()
        self.messagebox_error_code_not_found.setWindowTitle("No se encontró")
        TXT = f'No se encontro el código de producto \"{code}\".'\
            + f'\nIntenta nuevamente.'
        self.messagebox_error_code_not_found.setText(TXT)
        self.messagebox_error_code_not_found.setIcon(QMessageBox.Warning)
        self.messagebox_error_code_not_found.setStandardButtons(QMessageBox.Ok)
        self.messagebox_error_code_not_found.exec_()


    def open_messagebox_select_errorcode_first(self):
        self.messagebox_select_errorcode_first = QMessageBox()
        self.messagebox_select_errorcode_first.setWindowTitle("No se encontró código de error")
        TXT = f'Por favor selecciona un código de error primero.'
        self.messagebox_select_errorcode_first.setText(TXT)
        self.messagebox_select_errorcode_first.setIcon(QMessageBox.Warning)
        self.messagebox_select_errorcode_first.setStandardButtons(QMessageBox.Ok)
        self.messagebox_select_errorcode_first.exec_()


    def open_messagebox_errorcode_is_self(self):
        self.messagebox_errorcode_is_self = QMessageBox()
        self.messagebox_errorcode_is_self.setWindowTitle("Error en código")
        TXT = f'Error: El código de producto y error no pueden ser el mismo.'
        self.messagebox_errorcode_is_self.setText(TXT)
        self.messagebox_errorcode_is_self.setIcon(QMessageBox.Warning)
        self.messagebox_errorcode_is_self.setStandardButtons(QMessageBox.Ok)
        self.messagebox_errorcode_is_self.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
