import requests 
import pandas as pd
import datetime

dates = []

date_min = datetime.date.today()
date_max = date_min + datetime.timedelta(days=6)

while date_min <= date_max:
    #print(date_min)
    dates.append(date_min)
    date_min += datetime.timedelta(days=1)
#print(f"For Dates:\t{dates[0]} to {dates[-1]}")
date_min = datetime.date.today()

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date_min}&end_date={date_max}&api_key=7cHwgga1fvwHiaBYv5lcE3O7Tsiz8P2wvL7KenHd"
getreq = requests.get(url)
data = getreq.json()  #raw json data 

#Status code
if getreq.status_code == 200:
    print("\nAll Good! \n")
else: 
    print(f"\nSomething went wrong, here's your status code :\t{getreq.status_code}")

#Here is your date range and number of objects
print(f"For Dates {dates[0]}, to {dates[-1]}: There are {data['element_count']} Near-Earth-Objects! \n")

dfmin = data['near_earth_objects'][str(date_min)]
df2 = data['near_earth_objects'][str(dates[1])]
df3 = data['near_earth_objects'][str(dates[2])]
df4 = data['near_earth_objects'][str(dates[3])]
df5 = data['near_earth_objects'][str(dates[4])]
df6 = data['near_earth_objects'][str(dates[5])]
df7 = data['near_earth_objects'][str(dates[6])]

dataframe = pd.json_normalize(dfmin + df2 + df3 + df4 +df5 + df6 + df7)
print(dataframe)




# print(date_min)
# print(dates[0])