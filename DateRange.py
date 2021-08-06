import datetime
date =[]
dates = []
date_min = datetime.date.today()
date_max = date_min + datetime.timedelta(days=7)
while date_min <= date_max:
    print(date_min)
    dates.append(str(date_min))
    date.append(date_min)
    date_min += datetime.timedelta(days=1)
print([dates])
print([date])


print(len(dates))

print(f"This is your first date:\t {str(dates[0])}")
# print(f"\n{dates[:3]}")

# print(f"\nHere's your first date in string form:\t {str(dates[0])}\n")

# print(f"Here's all of your dates:\t {str(dates)}")

