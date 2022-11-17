# Python:   3.10.7
#
# Author:   Ethan LaRocca
#
# Purpose:  The Portland-based company you work for just 
#           opened two new branches. One is in New York City,
#           the other in London. They need a very simple program 
#           to find out if the branches are open or closed. 
#           The hours of both branches are 9:00 a.m.-5:00 p.m. 
#           in their own time zone.

from datetime import datetime
from pytz import timezone

format = "%H:%M:%S %Z%z"

time = datetime.now(timezone('UTC'))

portlandTime = time.astimezone(timezone('US/Pacific'))
portlandHour = portlandTime.strftime("%H")
if 9 <= int(portlandHour) <= 16:
    print("Portland Branch Status: OPEN")
else:
    print("Portland Branch Status: CLOSED")


nycTime = time.astimezone(timezone('US/Eastern'))
nycHour = nycTime.strftime("%H")
if 9 <= int(nycHour) <= 16:
    print("New York City Branch Status: OPEN")
else:
    print("New York City Branch Status: CLOSED")

londonTime = time.astimezone(timezone('Europe/London'))
londonHour = londonTime.strftime("%H")
if 9 <= int(londonHour) <= 16:
    print("London Branch Status: OPEN")
else:
    print("London Branch Status: CLOSED")