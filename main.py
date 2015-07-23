#! /usr/bin/python
import datetime , time
#Made by Zach
q = 1
while q == 1:
   try:
      print "What is your birthdate?"
      year = input ("Birth-day year (example 2013): ")
      month = input ("Birth-day month (example 4): ")
      day = input ("Birth-day day (example 13): ")
      hour = input ("Birth-day hour (example 3): ")
      minute = input ("Birth-day minute (example 34): ")
      second = input ("Birth-day second (example 54): ")
      bday = datetime.datetime(year,month,day,hour,minute,second)
      while 1:
          ctime = datetime.datetime.now()
          a = (ctime-bday).total_seconds()
          print "                      "*9999
          print "You are ",a," seconds old"
          print "Hit enter to update and type q to quit"
          q = raw_input()
          if q == "q":
             print "Stoping..."
             break 
             
              
          
   except:
      pass 
print "Done"
