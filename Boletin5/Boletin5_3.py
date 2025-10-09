print("Fahrenheit  |  Celsius")
print("----------------------")

for f in range(0, 121, 10):
    c = (f - 32) * 5 / 9
    print(f"{f:10}  |  {c:7.2f}")
