"""This module defines a custom exception class for network security errors.
It inherits from the built-in Exception class and provides additional context"""

import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message,error_details:sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "error occured  in python script name [{0}] at line number [{1}] with error message [{2}]".format(self.file_name, self.lineno, str(self.error_message))  

# if __name__ == '__main__':
#     try:
#         logger.logging.info("enter the try block")
#         a= 1 / 0
#         print("This will not be printed", a)
#     except Exception as e:
#         raise NetworkSecurityException(e, sys)      