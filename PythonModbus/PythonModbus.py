##################################################
# Yuldashev Shuhrat /megashuh17@gmail.com/       #
# Mikroelektronika plyus 2020, 12.01             #
# Examples using ModbusClient                    #
##################################################

from ModbusClient import ModbusClient 
from Debug import Debug
import time

dg = Debug()
dg.set_debug(True)

def main():    
    while True:
        mclient = ModbusClient()
        mclient.set_signed_value(True)
        dg.print(mclient.get_signed_value())

        if mclient.connect('localhost', 502):            
            dg.print("Connect to PLC OK") 
            response = mclient.read_holding_registers(1, 0, 10)
            dg.print(response)                
            del(response)
            time.sleep(1)            
        mclient.close()
        dg.print("Close socket")
        del(mclient)

if __name__ == "__main__":
    main()





