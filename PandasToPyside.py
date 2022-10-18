from enum import Enum
import pandas as pd
from SteelOrderToPandas import SteelOrderToPandas


class PandasToPyside():
    """This class converts the received data into the required format
    in order to create tables, lists, and options for Pyside Widgets.
    """

    ORIGIN = 0
    DESTINY = 1


    def __init__(self) -> None:
        self.dataframe_origin: pd.DataFrame
        self.dataframe_destiny: pd.DataFrame


    def get_products_by_warehouse(self, warehouse_name: str,
                                        kind: int) -> pd.DataFrame:
        """This method looks for the warehouse given by name into the
        dataframe of warehouses and extracts its id number. Then looks
        into every product for this warehouse's id and extracts the
        current quantity of product inside this warehouse.
        Finally, generates a dictionary with the desired structure of
        key:value and is transformed into a pandas dataframe in order
        to be plotted into the PySide's QTableWidget.

        Args:
            warehouse_name (str): Receives the warehouse's name to be found.

            kind (int): Receives one of the following class constants:
            ORIGIN, DESTINY.

        Returns:
            pd.DataFrame: Returns a dataframe with the structure desired
            to be plotted into QTableWidget. The structure of this pd is:

            >>> my_dictionary = {"codigo":[],"nombre":[],"presente":[],
            >>> "traspaso":[],"futuro":[],"error":[],"codigo-error":[]}
        """
        # if kind is different to origin or destiny, is a bad function call.
        if kind != self.ORIGIN and kind != self.DESTINY:
            empty_dict = {"": []}
            return pd.DataFrame(empty_dict)
        # Create the instance of the steel order's api consumer
        my_api = SteelOrderToPandas()

        # Request all warehouses and products in order to work with them
        my_warehouses = my_api.request_warehouses()
        my_products = my_api.request_products()

        # Create the dictionary that will contain the structured data
        my_dictionary = {"codigo": [], "nombre": [], "presente": [], "traspaso": [],
                        'futuro': [], "error": [], "codigo-error": []}

        # Create a filter that matches the given warehouse's name in dataframe
        warehouses_filter = my_warehouses['name'] == warehouse_name

        # Try except block: Expects a warehouse id integer value. If an empty
        # string is given, like the first item in the combo_boxes, means
        # that no warehouse where selected, and error must be handled.
        try:
            warehouse_id = int(my_warehouses[warehouses_filter].loc[:, 'id'])

        # Returns an empty pandas dataframe.
        except TypeError:
            empty_dict = {"": []}
            if kind == self.ORIGIN:
                self.dataframe_origin = pd.DataFrame(empty_dict)
                return self.dataframe_origin
            elif kind == self.DESTINY:
                self.dataframe_destiny = pd.DataFrame(empty_dict)
                return self.dataframe_destiny

        # Iterates through the values in the column "full reference".
        for product_full_reference in my_products['full-reference']:

            # This filter matches only the current iterated product.
            product_filter = my_products['full-reference'] == product_full_reference

            # The filter is applied and we receive a respective product name
            # But it comes in Series object
            product_filtered = my_products[product_filter].loc[:, 'name']

            # The object is converted into a string without index in it
            product_name = product_filtered.to_string(index=False)

            # Create a variable that stores the stock of product in warehouse
            warehouse_real_stock = 0

            # The column "product-warehouses" contains an array of dictionaries
            # in order to get their values we need to iterate through every
            # dictionary, so we can convert a single dict into a dataframe
            for warehouse in my_products[product_filter].loc[:, 'product-warehouses']:
                warehouse_data = pd.DataFrame(warehouse)

                # Once we have a dataframe of warehouses that contain inside
                # the information of the current iterated product
                # we create a filter that will match the warehouse id that
                # we obtain before, which was passed as argument as warehouse name
                warehouse_filter = warehouse_data['warehouse-id'] == warehouse_id

                # We get a row that contains the warehouse selected by the filter
                warehouse_by_id = warehouse_data[warehouse_filter]

                # Try except block: will try to get the value of the current row
                # inside the column "real-stock" and convert it into integer.
                try:
                    value = warehouse_by_id.loc[:, 'real-stock']
                    warehouse_real_stock = int(value)

                # If the process above failed, then means that there is an
                # empty array and the stock is zero
                except TypeError:
                    warehouse_real_stock = 0

            # The last process is to fill the row with the current product and
            # the received warehouse's data.
            my_dictionary['codigo'].append(product_full_reference)
            my_dictionary['nombre'].append(product_name)
            my_dictionary['presente'].append(warehouse_real_stock)
            my_dictionary['traspaso'].append(0)
            my_dictionary['futuro'].append(warehouse_real_stock)
            my_dictionary['error'].append(0)
            my_dictionary['codigo-error'].append("")

        # Create a dataframe with the dictionary we have made and return it
        # It will save it into the origin or destiny warehouse respectively.
        if kind == self.ORIGIN:
            self.dataframe_origin = pd.DataFrame(my_dictionary)
            self.dataframe_origin.sort_values(by=['codigo'])
            return self.dataframe_origin
        elif kind == self.DESTINY:
            self.dataframe_destiny = pd.DataFrame(my_dictionary)
            self.dataframe_destiny.sort_values(by=['codigo'])
            return self.dataframe_destiny


    def put_warehouses_products():
        