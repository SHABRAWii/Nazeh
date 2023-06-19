import serial
import numpy as np


import logging

import csv
import pandas as pd
import logging



        
#Barcode Scanner
class Barcode_Scanner(object):    
    # DE2120 response
    ACKN_CMD = 0x06 #sending acknowledge command to check zero barcode status
    NACK_CMD = 0x15

    # Constructor
    def __init__(self, port,Baud_rate):
        self.port = port
        self.baud_rate = Baud_rate
        if port is not None:
            self.port = serial.Serial(port, Baud_rate, timeout=1)
        else:
            self.port = port
        
    # Construct a command/parameter and send it to the module.
    def send_command(self, cmd):
        # start = '^_^'
        # end   = '.'
        command_string = '^_^'+ cmd +'.'
        self.port.write(command_string.encode())       
        ack_value = self.port.read()
        if ord(ack_value) == 0x06:
            return True
        elif ord(ack_value) == 0x15:
            return False
        return False
    
    def begin(self):
        if self.Connected() == False:
            return False
        self.port.flush()
        return True
    
    # determine whether the module is connected.
    def Connected(self):   
        String = "^_^" + chr(4) + "SPYFW."
        self.port.write(String.encode())
        
        # If it's an ACKN, return true
        # Otherwise, return false
        ack_value = self.port.read()
        if len(ack_value) > 0 and ord(ack_value) == 0x06:   # ACKN
            return True
        elif len(ack_value) > 0 and ord(ack_value) == 0x15: # NACK
            return False
        else:
            return False
        
    # Change the serial baud rate for the barcode module
    def Select_baudrate(self, baud_rate):
        if baud_rate == 1200:
            return self.send_command("232BAD2")# at 1200 baudrate
            
        elif baud_rate == 2400:
            return self.send_command("232BAD3") #for setting baudrate at 2400

        elif baud_rate == 4800:
            return self.send_command("232BAD4") #for setting baudrate at 4800

        elif baud_rate == 9600:
            return self.send_command("232BAD5") #for setting baudrate at 9600

        elif baud_rate == 19200:
            return self.send_command("232BAD6") #for setting baudrate at 19200

        elif baud_rate == 38400:
            return self.send_command("232BAD7") #for setting baudrate at 38400

        elif baud_rate == 57600:
            return self.send_command("232BAD8") #for setting baudrate at 57600
        
        else:   
            return self.send_command("232BAD9") # for Default (115200) baudrate
    
    # Returns the number of bytes in the serial receive buffer
    def available(self):
        return self.port.in_waiting

    # read byte from the serial port
    def read(self):
        return self.port.read()
    
      
    # Check the receive buffer for serial data from the barcode scanner
    def Read(self):
        # Check if there's data available
        if self.port.in_waiting == False:
            return False
        
        # read from serial port
        ack_value = self.port.read_until()
        return ack_value.decode()
    
   