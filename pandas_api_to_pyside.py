import pandas as pd
from steel_order_api_pandas import steel_order_api_pandas

def from_dataframe_get_warehouses_combobox(data: pd.DataFrame):
    temp_list = list(data['name'])
    return temp_list

if __name__=='__main__':
    my_class = steel_order_api_pandas()