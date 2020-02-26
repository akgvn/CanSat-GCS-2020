# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:53:11 2020

@author: MKA
"""


import serial
import time
import csv

# Arduino'nun bağlı olduğu port, baundrate, timeout
ser = serial.Serial('COM16', 9600, timeout=None)
# belirtilen sürede istenilen miktarda byte gönderilmezse boş döner
time.sleep(1)  # port bağlantısı kurulması için beklenilen süre
ser.flushInput()  # bufferı bosaltmak

"""
In Python 3, there's no implicit conversion between unicode (str) objects and bytes objects.
If you know the encoding of the output, you can .decode() it to get a string, 
or you can turn the \n you want to add to bytes with "\n".encode('ascii')
"""

myDict = {'TEAM_ID': [], 'MISSION_TIME': [], 'PACKET_COUNT': [], 'ALTITUDE': [], 'PRESSURE': [], 'TEMP': [], 'VOLTAGE': [], 'GPS_TIME': [],
          'GPS_LATITUDE': [], 'GPS_LONGITUDE': [], 'GPS_ALTITUDE': [], 'GPS_SATS': [], 'AIR_SPEED': [],  'SOFTWARE_STATE': [], 'PARTICLE_COUNT': []}


def getValues():  # Porttan gelen verileri bufferdan çekme
    arduinoData = ser.readline()  # byte -> TODO try-catch bloğu w
    arduinoData = arduinoData.decode().strip()
    splittedArduinoData = str(arduinoData).split(",")  # str
    assert len(splittedArduinoData) == 15
    return splittedArduinoData


def addToList(dataList):   # append data to Dictionary

    myDict['TEAM_ID'].append(dataList[0])
    myDict['MISSION_TIME'].append(dataList[1])
    myDict['PACKET_COUNT'].append(dataList[2])
    myDict['ALTITUDE'].append(dataList[3])
    myDict['PRESSURE'].append(dataList[4])
    myDict['TEMP'].append(dataList[5])
    myDict['VOLTAGE'].append(dataList[6])
    myDict['GPS_TIME'].append(dataList[7])
    myDict['GPS_LATITUDE'].append(dataList[8])
    myDict['GPS_LONGITUDE'].append(dataList[9])
    myDict['GPS_ALTITUDE'].append(dataList[10])
    myDict['GPS_SATS'].append(dataList[11])
    myDict['AIR_SPEED'].append(dataList[12])
    myDict['SOFTWARE_STATE'].append(dataList[13])
    myDict['PARTICLE_COUNT'].append(dataList[14])
    print(dataList)
    writeToCSV(dataList) # write to CSV
    


def writeToCSV(dataList):
        with open('ArduinoData.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #Time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            TEAM_ID = dataList[0]
            MISSION_TIME = dataList[1]
            PACKET_COUNT = dataList[2]
            ALTITUDE = dataList[3]
            PRESSURE = dataList[4]
            TEMP = dataList[5]
            VOLTAGE = dataList[6]
            GPS_TIME= dataList[7]
            GPS_LATITUDE= dataList[8]
            GPS_LONGITUDE= dataList[9]
            GPS_ALTITUDE= dataList[10]
            GPS_SATS = dataList[11]
            AIR_SPEED= dataList[12]
            SOFTWARE_STATE= dataList[13]
            PARTICLE_COUNT= dataList[14]
            
            info = {
            "TEAM_ID": TEAM_ID,
            "MISSION_TIME": MISSION_TIME,
            "PACKET_COUNT": PACKET_COUNT,
            "ALTITUDE": ALTITUDE,
            "PRESSURE": PRESSURE,
            "TEMP": TEMP,
            "VOLTAGE": VOLTAGE,
            "GPS_TIME": GPS_TIME,
            "GPS_LATITUDE": GPS_LATITUDE,
            "GPS_LONGITUDE": GPS_LONGITUDE,
            "GPS_ALTITUDE": GPS_ALTITUDE,
            "GPS_SATS": GPS_SATS,
            "AIR_SPEED": AIR_SPEED,
            "SOFTWARE_STATE": SOFTWARE_STATE,
            "PARTICLE_COUNT": PARTICLE_COUNT
            }
            csv_writer.writerow(info)
    
    
fieldnames = ["TEAM_ID", "MISSION_TIME", "PACKET_COUNT", "ALTITUDE", "PRESSURE", "TEMP", "VOLTAGE",
              "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_SATS", "AIR_SPEED", "SOFTWARE_STATE", "PARTICLE_COUNT"]  # columns of dataFrame
with open('ArduinoData.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
while 1:
    addToList(getValues())
    
