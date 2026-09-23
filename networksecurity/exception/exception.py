import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.errors = error_message
        _,_,exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file = exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return f"Error occured in python script name [{0}] at line number [{1}] error message [{2}]".format(
            self.file, self.lineno, str(self.errors))
