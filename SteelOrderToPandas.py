import json
import pandas as pd
import requests
from PySide2.QtWidgets import QMessageBox, QMainWindow


class SteelOrderToPandas():
    """This class allows to make calls to the steel order's api.
    """

    def __init__(self) -> None:
        """Prepares the key to be used by the other class' methods.
        """

        self.get_api_key()
        self.status_code = 0

    def get_api_key(self):
        """Reads the apikey file and loads the string into
        self.apikey attribute.
        """
        with open('apikey', 'r', encoding='utf-8') as f:
            self.apikey = f.readline()

    def request_warehouses(self) -> pd.DataFrame:
        """Requests all warehouses data from steel order's api.

        Returns:
            pd.DataFrame: Returns a DataFrame with all warehouses data.
        """
        QUERY_PARAMETERS = {'APIKEY': self.apikey}
        URL = 'https://app.stelorder.com/app/warehouses'
        response = requests.get(URL, params=QUERY_PARAMETERS)
        df_warehouses = pd.DataFrame(response.json())
        self.status_code = response.status_code
        return df_warehouses

    def request_products(self) -> pd.DataFrame:
        """Requests all products data from steel order's api.

        Returns:
            pd.DataFrame: Returns a DataFrame with all products' data.
        """
        QUERY_PARAMETERS = {'APIKEY': self.apikey}
        URL = 'https://app.stelorder.com/app/products'
        response = requests.get(URL, params=QUERY_PARAMETERS)
        df_products = pd.DataFrame(response.json())
        self.status_code = response.status_code
        return df_products

    def put_product_into_warehouse(self, warehouse_id: int, item_id: int, real_stock: int):
        headers = {
            'accept': '*/*',
            'APIKEY': str(self.apikey),
            'Content-Type': 'application/json; charset=utf-8',
        }

        json_data = {
            'location': '',
            'real-stock': str(real_stock),
            'minimum-stock': str(0),
            'warehouse-id': str(warehouse_id),
            'item-id': str(item_id),
        }
        URL = 'https://app.stelorder.com/app/productWarehouses'
        response = requests.put(URL,headers=headers,json=json_data)
        df_put = pd.DataFrame(response.json())
        self.status_code = response.status_code


    def is_forbidden_status_code(self):
        if self.status_code == 403:
            return True
        elif self.status_code == 200:
            return False


if __name__ == "__main__":
    object = SteelOrderToPandas()
    #print(object.apikey)
    #object.put_product_into_warehouse(1009,7872468,0)
    for i in range(0,70):
        object.request_products()
        print(object.status_code)
    # def request_warehouse(self, warehouse_id: int) -> pd.DataFrame:
    #     """Requests a specific warehouse data.

    #     Args:
    #         warehouse_id (int): The id of the warehouse

    #     Returns:
    #         pd.DataFrame: Returns a DataFrame with the warehouse's data
    #     """
    #     QUERY_PARAMETERS = {'APIKEY':self.__apikey}
    #     URL = f'https://app.stelorder.com/app/warehouses/{warehouse_id}'
    #     response = requests.get(URL,params=QUERY_PARAMETERS)
    #     df_warehouse = pd.DataFrame(response.json())
    #     return df_warehouse

    # def request_product(self, product_id: int) -> pd.DataFrame:
    #     """Requests a specific product data

    #     Args:
    #         product_id (int): The product id

    #     Returns:
    #         pd.DataFrame: Returns a DataFrame with the product's data
    #     """
    #     QUERY_PARAMETERS = {'APIKEY':self.__apikey}
    #     URL = f'https://app.stelorder.com/app/products/{str(product_id)}'
    #     response = requests.get(URL,params=QUERY_PARAMETERS)
    #     df_product = pd.DataFrame(response.json())
    #     return df_product

    # def get_warehouses_data_by_product(self, product_id: int) -> bool:
    #     """Gets from the request_product(int) that saves into the attrib
    #     self.df_product DataFrame, a DataFrame of the 'product-warehouses'
    #     column content and saves it into self.df_product_warehouses_data.

    #     Returns:
    #         bool: _description_
    #     """
    #     if self.df_product.empty:
    #         return False
    #     df_product = self.request_product(product_id)
    #     for item in df_product['product-warehouses']:
    #         self.df_product_warehouses_data = pd.DataFrame(item)
    #     return True

    # def get_dataframe_cell_value(self, dataframe: pd.DataFrame, row, column):
    #     return dataframe.iloc[row,column]
