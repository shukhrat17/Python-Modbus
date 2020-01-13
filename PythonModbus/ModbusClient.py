##################################################
# Yuldashev Shuhrat /megashuh17@gmail.com/        #
# Mikroelektronika plyus 2020, 12.01             #
# The module is developed on the basis of the    #
# open uModbus library on pure Python.           #                    
# For installing uModbus: pip install uModbus    #
# https://pypi.org/project/uModbus/              #
##################################################

import socket
import sys

from umodbus import conf
from umodbus.client import tcp

from Debug import Debug

dg = Debug()
dg.set_debug(True)

class ModbusClient:

    def __init__(self):        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timeout = 5

    # Enable values to be signed (default is False)
    def set_signed_value(self, signed):
        if signed == True:
            conf.SIGNED_VALUES = True            
        else:
            conf.SIGNED_VALUES = False            
    
    # Get signed values status
    def get_signed_value(self):
        if conf.SIGNED_VALUES == True:
            return True
        else:
            return False

    # Set socket connect timeout
    def set_timeout(self, time):
        self.timeout = time

    # Get socket connect timeout
    def get_timeout(self):
        return self.timeout

    # Connect to Server
    def connect(self, ip, port): 
        timeout = self.timeout
        sock = self.sock
        sock.settimeout(timeout)
        try:
            sock.connect((ip, port))
            #self.sock = sock
            return True
        except:
            #self.sock = sock
            return False


    # Close socket
    def close(self):
        self.sock.close()

    # 01: Read Coils
    def read_coils(self, slave_id, starting_address, quantity):
        try:
            message = tcp.read_coils(slave_id, starting_address, quantity)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                 dg.print (f"Error code = {e.error_code}")
            return False
    
    # 02: Read Discrete Inputs
    def read_discrete_inputs(self, slave_id, starting_address, quantity):
        try:
            message = tcp.read_discrete_inputs(slave_id, starting_address, quantity)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                dg.print (f"Error code = {e.error_code}")
            return False

    # 03: Read Holding Registers
    def read_holding_registers(self, slave_id, starting_address, quantity):
        try:
            message = tcp.read_holding_registers(slave_id, starting_address, quantity)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                dg.print (f"Error code = {e.error_code}")
            return False

    # 04: Read Input Registers
    def read_input_registers(self, slave_id, starting_address, quantity):
        try:
            message = tcp.read_input_registers(slave_id, starting_address, quantity)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                dg.print (f"Error code = {e.error_code}")
            return False

    # 05: Write Single Coil
    def write_single_coil(self, slave_id, starting_address, value):
        try:
            message = tcp.write_single_coil(slave_id, starting_address, value)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                dg.print (f"Error code = {e.error_code}")
            return False

    # 06: Write Single Register
    def write_single_register(self, slave_id, starting_address, value):
        try:
            message = tcp.write_single_register(slave_id, starting_address, value)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                dg.print (f"Error code = {e.error_code}")
            return False

    # 15: Write Multiple Cpoils
    def write_multiple_coils(self, slave_id, starting_address, values):
        try:
            message = tcp.write_multiple_coils(slave_id, starting_address, values)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                dg.print (f"Error code = {e.error_code}")
            return False

    # 16: Write Multiple Registers
    def write_multiple_registers(self, slave_id, starting_address, values):
        try:
            message = tcp.write_multiple_registers(slave_id, starting_address, values)
            response = tcp.send_message(message, self.sock)
            return response
        except Exception as e:
            dg.print ("Error string = " + str(e))
            if(str(e).isdigit()):
                dg.print (f"Error code = {e.error_code}")
            return False



    

