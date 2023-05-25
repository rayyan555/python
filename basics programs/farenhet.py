def display_temperature_conversion_table():
    print("Celsius\t\tFahrenheit")
    for celsius in range(0, 101, 10):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}\t\t{fahrenheit:.1f}")

display_temperature_conversion_table()
