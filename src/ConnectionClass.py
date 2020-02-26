# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 2020

@author: MKA
"""

import serial
import time 
import csv

class SerialBridge:
    
    __mySerial = serial.Serial()
    __baudrate = 0
    __port = ''
    
    myDict = {'TEAM_ID': [], 'MISSION_TIME': [], 'PACKET_COUNT': [], 'ALTITUDE': [], 'PRESSURE': [], 'TEMP': [], 'VOLTAGE': [], 'GPS_TIME': [],
          'GPS_LATITUDE': [], 'GPS_LONGITUDE': [], 'GPS_ALTITUDE': [], 'GPS_SATS': [], 'AIR_SPEED': [],  'SOFTWARE_STATE': [], 'PARTICLE_COUNT': []}
    
    fieldnames = ["TEAM_ID", "MISSION_TIME", "PACKET_COUNT", "ALTITUDE", "PRESSURE", "TEMP", "VOLTAGE",
              "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_SATS", "AIR_SPEED", "SOFTWARE_STATE", "PARTICLE_COUNT"]  # columns of dataFrame
    
    def __init__(self, baudrate, port ):
        self.mySerial =serial.Serial(port, baudrate, timeout=None)
        self.mySerial.flushInput()  # empty the buffer
        time.sleep(1)  # expected time to establish port connection
                    
    def setPort(self, port):
        self.port = port;
        self.mySerial.port= port
    def getPort(self):
        return self.port
    def setBaudrate(self, baudrate):
        self.baudrate = baudrate
    def getBaudrate(self):
        return self.baudrate
    
    def getValues(self):  # Retrieving data from the port from the buffer
        arduinoData = self.mySerial.readline()  # byte -> TODO try-catch bloğu w
        arduinoData = arduinoData.decode().strip()
        splittedArduinoData = str(arduinoData).split(",")  
        assert len(splittedArduinoData) == 15
        return splittedArduinoData
    
    def getDictionary(self):
        return self.myDict
    
    def writeToCSV(self, dataList):
            with open('SerialData.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
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
            
            with open('SerialData.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                csv_writer.writeheader()
    
    def addToList(self, dataList):   # append data to Dictionary

        self.myDict['TEAM_ID'].append(dataList[0])
        self.myDict['MISSION_TIME'].append(dataList[1])
        self.myDict['PACKET_COUNT'].append(dataList[2])
        self.myDict['ALTITUDE'].append(dataList[3])
        self.myDict['PRESSURE'].append(dataList[4])
        self.myDict['TEMP'].append(dataList[5])
        self.myDict['VOLTAGE'].append(dataList[6])
        self.myDict['GPS_TIME'].append(dataList[7])
        self.myDict['GPS_LATITUDE'].append(dataList[8])
        self.myDict['GPS_LONGITUDE'].append(dataList[9])
        self.myDict['GPS_ALTITUDE'].append(dataList[10])
        self.myDict['GPS_SATS'].append(dataList[11])
        self.myDict['AIR_SPEED'].append(dataList[12])
        self.myDict['SOFTWARE_STATE'].append(dataList[13])
        self.myDict['PARTICLE_COUNT'].append(dataList[14])
        print(dataList)
        self.writeToCSV(dataList) # write to CSV
        
        
    
