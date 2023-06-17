import time

timestamp = (time.strftime('%H:%M:%S'))
print(timestamp)

hour = int(time.strftime('%H'))
print(hour)
# minute = int(time.strftime('%M'))
# print(minute)
# second = int(time.strftime('%S'))
# print(second)
hour = int(input("enter the time : "))
if (hour >= 6 and hour < 12):
    print("goodmorning")
elif (hour >= 12 and hour < 16):
    print("goodafternoon")
elif (hour >= 16 and hour < 21):
    print("goodevening")
elif (hour >= 21 and hour > 6):
    print("goodnight")


print("enter time between 1 to 12 and Am/PM ")
time = int(input("select time from 0 to 12 : "))
ampm = (input("am or pm : "))



if (((time >= 12) or (time < 6)) and (ampm == "am") ) or (((time >= 9) and (time < 12)) & (ampm == "pm") ):
    print("its good night ")
elif (((time >= 6) or (time < 12)) and (ampm == "am") ) :
    print("its good morning ")
elif (((time >= 12) or (time < 5)) and (ampm == "pm") ) :
    print("its afternoon ")
elif (((time >= 5) or (time < 9)) and (ampm == "pm") ) :
    print("its evening ")
