# -*- coding: utf-8 -*-

# Mustafa Kayhan Arıcan, 2020-02-27

import csv
import time
import serial


class SerialBridge:

    __mySerial = serial.Serial()
    __baudrate = 0
    # Windows = "COM13", Linux = "/dev/ttyUSB0" etc. Numbers can change.
    __port = ""
    message="";

    myDict = {"TEAM_ID": [], "MISSION_TIME": [], "PACKET_COUNT": [], "ALTITUDE": [], "PRESSURE": [], "TEMP": [], "VOLTAGE": [], "GPS_TIME": [],
              "GPS_LATITUDE": [], "GPS_LONGITUDE": [], "GPS_ALTITUDE": [], "GPS_SATS": [], "AIR_SPEED": [],  "SOFTWARE_STATE": [], "PARTICLE_COUNT": []}

    fieldnames = ["TEAM_ID", "MISSION_TIME", "PACKET_COUNT", "ALTITUDE", "PRESSURE", "TEMP", "VOLTAGE",
                  "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_SATS", "AIR_SPEED", "SOFTWARE_STATE", "PARTICLE_COUNT"]  # columns of dataFrame

    def __init__(self, port,baudrate ):
        self.mySerial = serial.Serial(port, baudrate, timeout=None)
        self.mySerial.flushInput()  # empty the buffer
        time.sleep(1)  # expected time to establish port connection
        with open('SerialDatam.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            csv_writer.writeheader()

    def setPort(self, port):
        self.port = port
        self.mySerial.port = port

    def getPort(self):
        return self.port

    def getSerial(self):
        return self.mySerial

    def setBaudrate(self, baudrate):
        self.baudrate = baudrate

    def getBaudrate(self):
        return self.baudrate
    """"    
    def sendMessageToArduino(self, message):
        self.__mySerial.write(b''+message)
    """

    def getValues(self):  # Retrieving data from the port from the buffer
        arduinoData = self.mySerial.readline()  # byte -> TODO try-catch bloğu w
        arduinoData = arduinoData.decode().strip()
        splittedArduinoData = str(arduinoData).split(",")
        assert len(splittedArduinoData) == 15
        return splittedArduinoData

    def getDictionary(self):
        row = self.getValues()
        self.addToList( row )
        return self.myDict

    def writeToCSV(self, dataList):     
        with open('SerialDatam.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            TEAM_ID = dataList[0]
            MISSION_TIME = dataList[1]
            PACKET_COUNT = dataList[2]
            ALTITUDE = dataList[3]
            PRESSURE = dataList[4]
            TEMP = dataList[5]
            VOLTAGE = dataList[6]
            GPS_TIME = dataList[7]
            GPS_LATITUDE = dataList[8]
            GPS_LONGITUDE = dataList[9]
            GPS_ALTITUDE = dataList[10]
            GPS_SATS = dataList[11]
            AIR_SPEED = dataList[12]
            SOFTWARE_STATE = dataList[13]
            PARTICLE_COUNT = dataList[14]

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

            
        time.sleep(0.5)

        

    def addToList(self, dataList):   # append data to Dictionary

        self.myDict["TEAM_ID"].append( int( dataList[0]) )
        self.myDict["MISSION_TIME"].append( int( dataList[1] ))
        self.myDict["PACKET_COUNT"].append(int( dataList[2]) )
        self.myDict["ALTITUDE"].append(int( dataList[3]) )
        self.myDict["PRESSURE"].append(int( dataList[4]) )
        self.myDict["TEMP"].append( float( dataList[5]) )
        self.myDict["VOLTAGE"].append( float ( dataList[6]) )
        self.myDict["GPS_TIME"].append( int ( dataList[7]) )
        self.myDict["GPS_LATITUDE"].append( float( dataList[8]) )
        self.myDict["GPS_LONGITUDE"].append( float( dataList[9]))
        self.myDict["GPS_ALTITUDE"].append( float( dataList[10]) )
        self.myDict["GPS_SATS"].append(int ( dataList[11]) )
        self.myDict["AIR_SPEED"].append( float( dataList[12]) )
        self.myDict["SOFTWARE_STATE"].append( int( dataList[13]))
        self.myDict["PARTICLE_COUNT"].append( float( dataList[14]))
        print(dataList)
        self.writeToCSV(dataList)  # write to CSV
