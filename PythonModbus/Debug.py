##################################################
# Yuldashev Shuhrat                              #
# Mikroelektronika plyus 2020, 12.01             #                  
# For printig Debug messages                     #
##################################################

import sys

class Debug:

    def __init__(self):
        self.debug_flag = True

    def print(self, string):
        if self.debug_flag == True:
            print(string)

    def set_debug(self, status):
        self.debug_flag = status

    

        