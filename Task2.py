import datetime
import time

earth_weight = 64
moon_index = 0.165
year_now = datetime.date.today().year

for i in range(1, 16):
  print(f"Ваш вес в {year_now} году: {round(earth_weight * moon_index, 2)} кг" )
  earth_weight += 1
  year_now +=1