def celsiusParaFah(c):
    return (c*9/5) + 32
tempCelsius = [10, 20, 35]

tempFahrenheit = map(celsiusParaFah, tempCelsius)

print(list(tempFahrenheit))