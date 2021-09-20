#Temperature conversion from celsius to Farenheit
def celsius_to_farenheit(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

#Temperature conversion from farenheit to celsius
def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius


celsius = celsius_to_farenheit(32)
print("The temperature is " + str(celsius) + " degrees celsius")
farenheit = farenheit_to_celsius(32)
print("The temperature is " + str(farenheit) + " degrees farenheit")





