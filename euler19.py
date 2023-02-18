from datetime import datetime

sundays = []

for y in range(1901, 2001):
    for m in range(1,13):
        ds = str(y) + ", " + str(m) + ", 1"
##        dp = datetime.strptime(ds, '%Y, %m, %d')
        dp = datetime(y,m,1)
        if dp.strftime('%A') == 'Sunday':
            print(dp)
            sundays.append(dp)

print(len(sundays))
