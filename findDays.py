#!/usr/bin/env python3

def findDays(year,month):

    isLeap=0
    if (year % 400 == 0):
        isLeap=1
    elif (year % 100 == 0):
        isLeap=0
    elif (year % 4 == 0):
        isLeap=1
    else:
        isLeap=0

    if (month == 2 and isLeap == 1 ):
        print("year:",year, "month:",month, "has 29 days")
    elif (month == 2 and isLeap == 0):
        #print("28")
        print("year:",year, "month:",month, "has 28 days")
    elif (month in [1,3,5,7,8,10,12]):
        #print("31")
        print("year:",year, "month:",month ,"has 31 days")
    elif (month in [4,6,9,11]):
       # print("30")
        print("year:",year, "month:",month ,"has 30 days")
    else:
        print("enter valid month")
    return 1

findDays(2020,2)
findDays(2024,10)
findDays(1996,104)
findDays(2000,10)

