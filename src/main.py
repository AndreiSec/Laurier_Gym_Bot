'''
Created on Mar 18, 2021

@author: andrei
'''


from Components import BookGymSpot
from Time_Module import time_checker
import datetime




# INPUTS: CHANGE TO YOUR HEARTS DESIRE #####################################################################################

bookingType = "FitCentre" #GET STRING FROM TABLE AT https://www.laurierathletics.com/ecommerce/user/home.php
desired_time = "11:00:00" #KEEP IN THIS FORMAT
days_in_advance = 4 # MINIMUM 3 DAYS!


login = ""

password = ""

############################################################################################################################



# """TESTING TESTING TESTING TESTING TESTING TESTING TESTING """
# 
# bookingType = "Pool (Deep End)"
# desired_time = "12:00:00"
# days_in_advance = 4
# 
# 
# """TESTING TESTING TESTING TESTING TESTING TESTING TESTING """

# Don't worry about these ##################################################################################################

curDate = datetime.datetime.now()
delta = datetime.timedelta(days = days_in_advance)
a = curDate + delta
dateThreeDaysFromNow = a.strftime('%Y-%m-%d')

############################################################################################################################





test1 = BookGymSpot()

test1.setup_method()

startNow = time_checker(desired_time)

if startNow == True:
    test1.test_test1(login, password, dateThreeDaysFromNow, desired_time, bookingType)

# test1.teardown_method()


