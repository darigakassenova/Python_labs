import datetime
a = datetime.datetime(2003,12,31,23,23,00)
b = datetime.datetime(2022,1,3,23,23,00)
print((b-a).total_seconds())