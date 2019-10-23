import csv

#the csv module implements classes to read and write tabular data in CSV format

csvfile = open("eggs.csv", "w")

with open("eggs.csv", "w", newline="") as f:
    spamwriter = csv.writer(f, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])