import pandas as pd
import json

from steel_order_api_pandas import steel_order_api_python

def get_warehouse_by_product_id():
    my_api = steel_order_api_python()
    my_product_warehouses = my_api.request_product(7872468)
    print(my_api.get_dataframe_cell_value(my_api.df_product_warehouses_data,0,4))

def run():
    my_api = steel_order_api_python()
    #data = my_api.request_warehouses()
    #list(data['id'])
    #print(my_api.request_warehouse(-2))
    
    # myDict = dict(my_api.request_warehouse(-2).loc[0,['name']])
    # print(type(myDict['name']))
    
    
    # print(my_api.request_products())
    # print(my_api.request_products().loc[:,['full-reference', 'description', 'real-stock', 'id']])

    my_product_warehouses = my_api.request_product(7872468)
    #product_warehouses = my_product_warehouses.loc[0,['product-warehouses']]
    #print(my_api.product_warehouses_data)
    # for dictionary in product_warehouses:
    #     for item in dictionary:
    #         print("ESTE ES EL ITEM: ",item)
    #         print(type(item))
    print(my_api.get_dataframe_cell_value(my_api.df_product_warehouses_data,0,4))
    
if __name__ == '__main__':
    run()