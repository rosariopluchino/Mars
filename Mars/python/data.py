import time
import csv
def sendData():
    input = "../Dataset/input.csv"
    output = "../Dataset/output.csv"
    with open(input,  "r") as inmarsweather:
        csv_reader = csv.reader(inmarsweather,  delimiter=", ")
        for row in csv_reader:
            with open(output,  "a") as outmarsweather:
                writer = csv.writer(outmarsweather)
                writer.writerow(row)
                time.sleep(1)

sendData()