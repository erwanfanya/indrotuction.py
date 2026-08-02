city = input("enter your city name:")
temp = float(input("enter today's temparature in C:"))

if temp>35:
    print("warning: it's verey hot today")

if temp>25:
    print("Great day to go outside!")
else:
    print("GRab a jackect before you go out")

if temp >35:
    print("weather: scorching hot")
elif temp >25:
    print("Weather:warm and sunny")
elif temp >15:
    print("weathhhher: cool and breezy")
else:
    print("weather:cold - stay warm!")



import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now", now)

print(calendar.calendar(now.year))
