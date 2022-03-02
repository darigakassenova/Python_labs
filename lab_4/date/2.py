import datetime
t = datetime.date.today()
y = datetime.date.today() - datetime.timedelta(1)
tw = datetime.date.today()+ datetime.timedelta(1)
print(y, t, tw, sep = "\n")