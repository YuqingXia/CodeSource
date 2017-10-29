#this is simple scheduler
import threading
import logging
import os
import subprocess
log = logging.getLogger()

def exec_functions(command_list):
    for command in command_list:
        subprocess.call(command)






