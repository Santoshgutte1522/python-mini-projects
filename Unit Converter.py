def unit_converter():
    print("Unit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Kilograms to Pounds")

    choice = int(input("Choose an option: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", (celsius * 9/5) + 32)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius:", (fahrenheit - 32) * 5/9)
    elif choice == 3:
        km = float(input("Enter distance in kilometers: "))
        print("Distance in miles:", km * 0.621371)
    elif choice == 4:
        kg = float(input("Enter weight in kilograms: "))
        print("Weight in pounds:", kg * 2.20462)
    else:
        print("Invalid choice!")


unit_converter()
