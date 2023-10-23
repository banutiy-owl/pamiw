from datetime import datetime, timedelta

from model import *

def getDay(day):
    first_day = datetime.now()
    if (day==1):
        return first_day.strftime("%A")
    return_day = first_day+timedelta(days=(day-1))
    return return_day.strftime("%A")


def getCurrentConditions(city):
    list_current_condtions=current_conditions(city)
    return list_current_condtions

def getDays(city):
    days=[forDay(1, city),forDay(2, city),forDay(3, city),forDay(4, city),forDay(5, city)]
    return days