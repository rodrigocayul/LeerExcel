import json
import xlrd
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def main():
    df = pd.read_excel("listado.xlsx")

    data = []

    for index,row in df.iterrows():
        data.append({"ProfileKey":"ID","Contact":{"Email":row["Email"],"CustomFields":[{"key":"nombre","value":row["Nombre"]}]}})

    print("JSON - Conectar con servicios API")
    ##print("POST")
    print(json.dumps(data))

main()