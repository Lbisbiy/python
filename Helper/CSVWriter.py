# -*- coding: utf-8 -*-
import csv


class CSVWriter:

    @staticmethod
    def write_csv(date):
        with open('avito.csv', 'a') as inf:
            writer = csv.writer(inf)
            writer.writerow((
                date['year'],
                date['price'],
                date['mileage'],
                date['engine'],
                date['body_type'],
                date['url']
            ))

