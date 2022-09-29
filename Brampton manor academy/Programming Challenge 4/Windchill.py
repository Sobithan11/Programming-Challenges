def Windchill(air_temp,air_speed):
  Windchill=35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
  return Windchill
y=[[10,15],[0,25],[-10,35]]
for i in range (0,3):
  print(f'Temperature of {y[i][0]} and speed of {y[i][1]} gives windchill of :{Windchill(y[i][0],y[i][1])}')
  
air_temp=float(input("Temperature:"))
air_speed=float(input("Speed:"))
x=Windchill(air_temp,air_speed)
print(f'Windchill: {x}')


  