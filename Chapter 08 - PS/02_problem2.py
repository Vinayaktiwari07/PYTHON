def temperature():
    temp = int(input("Enter deegre: "))
    fehren = ((temp*9/5) + 32)
    print(f"{round(fehren, 0)}°F")
temperature()