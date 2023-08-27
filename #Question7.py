#Question7
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def matching_temperature():
    # starting from a low value.
    celsius = -100  
    while True:
        fahrenheit = celsius_to_fahrenheit(celsius)
        if celsius == fahrenheit:
            return celsius
        celsius += 1

temperature = matching_temperature()
print("The temperature at which Celsius and Fahrenheit are the same:", temperature)
