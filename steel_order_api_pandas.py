import pandas as pd
import requests

class steel_order_api_pandas():
    """_summary_
    """
    def __init__(self) -> None:
        """Calls the method get_api_key
        """
        self.get_api_key()


    def get_api_key(self):
        """Reads the apikey file and loads the string into self.apikey attribute
        """
        with open('apikey','r',encoding='utf-8') as f:
            self.apikey = f.readline()


    #Funcion GetWarehouses
    def request_warehouses(self) -> pd.DataFrame:
        """Requests all warehouses data from steel order api

        Returns:
            pd.DataFrame: Returns a DataFrame with all warehouses data
        """
        QUERY_PARAMETERS = {'APIKEY':self.apikey}
        URL = 'https://app.stelorder.com/app/warehouses'
        response = requests.get(URL,params=QUERY_PARAMETERS)
        df_warehouses = pd.DataFrame(response.json())
        return df_warehouses


    #Funcion GetWarehouse
    def request_warehouse(self, warehouse_id: int) -> pd.DataFrame:
        """Request a specific warehouse data

        Args:
            warehouse_id (int): The id of the warehouse

        Returns:
            pd.DataFrame: Returns a DataFrame with the warehouse's data
        """
        QUERY_PARAMETERS = {'APIKEY':self.apikey}
        URL = f'https://app.stelorder.com/app/warehouses/{warehouse_id}'
        response = requests.get(URL,params=QUERY_PARAMETERS)
        df_warehouse = pd.DataFrame(response.json())
        return df_warehouse


    def request_products(self) -> pd.DataFrame:
        """Requests all products data from steel order api

        Returns:
            pd.DataFrame: Returns a DataFrame with all products' data
        """
        QUERY_PARAMETERS = {'APIKEY':self.apikey}
        URL = 'https://app.stelorder.com/app/products'
        response = requests.get(URL,params=QUERY_PARAMETERS)
        df_products = pd.DataFrame(response.json())
        return df_products

    def from_request_products_get_product(self, product_id: int):
        df_products = self.request_products()
        #print(df_products['id'] == product_id)
        #print(df_products.loc[df_products['id'] == product_id])
        print(df_products.iloc[df_products.index == 0])


    def request_product(self, product_id: int) -> pd.DataFrame:
        """Requests a specific product data

        Args:
            product_id (int): The product id

        Returns:
            pd.DataFrame: Returns a DataFrame with the product's data
        """
        QUERY_PARAMETERS = {'APIKEY':self.apikey}
        URL = f'https://app.stelorder.com/app/products/{str(product_id)}'
        response = requests.get(URL,params=QUERY_PARAMETERS)
        df_product = pd.DataFrame(response.json())
        return df_product

    def get_warehouses_data_by_product(self, product_id: int) -> bool:
        """Gets from the request_product(int) that saves into the attrib
        self.df_product DataFrame, a DataFrame of the 'product-warehouses'
        column content and saves it into self.df_product_warehouses_data.

        Returns:
            bool: _description_
        """
        if self.df_product.empty:
            return False
        df_product = self.request_product(product_id)
        for item in df_product['product-warehouses']:
            self.df_product_warehouses_data = pd.DataFrame(item)
        return True

    def get_dataframe_cell_value(self, dataframe: pd.DataFrame, row, column):
        return dataframe.iloc[row,column]


if __name__ == '__main__':
    my_class = steel_order_api_pandas()
    #my_class.from_request_products_get_product(7872468)
    print(my_class.request_warehouses())