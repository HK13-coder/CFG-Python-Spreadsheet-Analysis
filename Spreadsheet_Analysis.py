import csv
import pandas as pd
import openpyxl
import xlsxwriter
import matplotlib.pyplot as plt
import numpy as np


profits_list=[]
months=[]

#--------Read the data:--------
def read_data ():
    data = []
    with open('sales.csv', 'r+') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


#--------List of months--------
def month ():
    data = read_data()

    for row in data:
        month = (row['month'])
        months.append(month)
    print('The sales sheet includes data for the following months {}'.format(months))


#--------Total sales across all months & List of all sales--------
def sales ():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    all_sales=print('All of the sales are{}',format(sales))
    total = sum(sales)
    print('Total sales: {}'.format(total))

#--------Sales minus expenditure--------
def profits ():
    data=read_data()

    for row in data:
        sale = int(row['sales'])
        expenditure = int(row['expenditure'])
        profits_list.append(sale - expenditure)
    print('The profits are {}',format(profits_list))

month()
sales()
profits()

#--------Add profit column to csv--------
df = pd.read_csv('sales.csv')
df['Profits']=profits_list
df.to_csv("sales.csv",index=False)

# --------plot profits on graph--------
xpoints = np.array(months)
ypoints = np.array(profits_list)
plt.plot(xpoints, ypoints,marker = '*', color ='r',ls = ':')
plt.title("Profit per month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

#--------Change CSV to Excel--------
read_file = pd.read_csv(r'C:\Users\holly\Documents\Code First Girls\Python\venv\sales2.csv')
read_file.to_excel(r'C:\Users\holly\Documents\Code First Girls\Python\venv\Sales_ex.xlsx', index = None, header =True)


#--------conditional format --------
