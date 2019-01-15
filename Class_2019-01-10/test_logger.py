import time

from logger import writelog

writelog("logfile1.log", "Program Started")

time.sleep(10)

writelog("logfile1.log", "Program Finished")
