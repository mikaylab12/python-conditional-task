speed = int(input("What is the average speed of the driver in km/h: "))
speed_limit = int(input("What is the allowed speed on the road: "))
points = (speed- speed_limit)/5

if speed < 60:
    print("Ok")
else:
    if points < 12:
          print("demerits" + str(points))
    else:
        print("Time to go to jail.")