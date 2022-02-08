import csv
import datetime
import math

import pandas as pd


with open('sales.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    item_sold = []
    gender_sales = []
    total_quantity = []
    total_revenue_february = []
    total_revenue_january = []


    def convert(date_time):
        format = '%m %d %Y'  # The format
        datetime_str = datetime.datetime.strptime(date_time, format)

        return datetime_str

    line_count = 0
    total_revenue = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # total revenue
            data_float = float(row[9])
            data_int = math.ceil(data_float)
            total_revenue += data_int

            # total_quantity.append(row[9])
            #
            # item_sold.append(row[6])
            # item_sold.append(row[5])
            #
            # gender_sales.append(row[9])
            # gender_sales.append(row[4])
            line_count += 1

    # total revenue
    print(f'How much is the total sales revenue of the data ? {total_revenue}')

    # print(f'How many are the total quantity of all the sold items ?  {max(item_sold)}')
    #
    # print(f'What is the most expensive item that is sold ?  {max(item_sold)}')
    # print(f'Which Gender does generate more sales ? {max(gender_sales)}')
    #
    # print(f'How much is the total sales revenue in February 2019 ? {max(gender_sales)}')
    # print(f'What is the most popular Product Line in January 2019 ? {max(gender_sales)}')

    # How much is the total sales revenue of the data ? (10)
    # How many are the total quantity of all the sold items ? (10)
    # What is the most expensive item that is sold ? (10) -> OK
    # Which Gender does generate more sales ? (20) -> OK
    # How much is the total sales revenue in February 2019 ? (25) OK
    # What is the most popular Product Line in January 2019 ? (25) OK
