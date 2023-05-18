v=float(input("enter the speed of the wind mill:"))
t=float(input("enter the temperature in celcius:"))
wind_chill_index=13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16
print("the wind chill index is :",wind_chill_index)
