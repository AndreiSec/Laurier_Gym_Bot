'''
Created on Sep 16, 2020

@author: andrei
'''

from datetime import date, timedelta, datetime
import time


def time_checker(desired_time):
    desired_time = desired_time[0:5]
    now_time = get_time()
#     return str("Open")
#     now_time = "16:00"
    while str(now_time) != desired_time:
#         now = datetime.now()
        time.sleep(1)
        now_time = get_time()
        
    
    if str(now_time) == desired_time:
        print(now_time)
        return True
    else:
        return False
    
    
def get_time():
    now = datetime.now()
    time = now.strftime("%H:%M")
    
    return time

def get_date():
    now = datetime.today().strftime('%Y-%m-%d')
    
    return now


