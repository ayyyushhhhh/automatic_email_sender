import csv 
from data_model import Data

def get_data(file_name:str):
    with open(file_name,"r") as csv_data:
        data_names = csv.reader(csv_data) 
        data_list =[] 
        for data in data_names:
            names_data = Data(data[0], data[1])
            data_list.append(names_data) 
        return data_list