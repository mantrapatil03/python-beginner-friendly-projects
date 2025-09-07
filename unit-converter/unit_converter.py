# unit_converter.py

def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose conversion (1-4): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c}°C")
    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273.15
        print(f"{c}°C = {k}K")
    elif choice == '4':
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273.15
        print(f"{k}K = {c}°C")
    else:
        print("Invalid choice!")

def currency_converter():
    rates = {'USD': 1.0, 'EUR': 0.91, 'GBP': 0.78, 'INR': 82.0}
    from_curr = input("From currency (USD, EUR, GBP, INR): ").upper()
    to_curr = input("To currency (USD, EUR, GBP, INR): ").upper()

    if from_curr not in rates or to_curr not in rates:
        print("Unsupported currency!")
        return

    amount = float(input(f"Amount in {from_curr}: "))
    # Convert amount to USD, then to target currency
    converted = amount / rates[from_curr] * rates[to_curr]
    print(f"{amount} {from_curr} = {converted} {to_curr}")

def length_converter():
    print("\nLength Converter")
    print("Supported units: meter (m), kilometer (km), mile (mi), yard (yd), foot (ft)")
    units = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048
    }

    from_unit = input("From unit (m, km, mi, yd, ft): ").lower()
    to_unit = input("To unit (m, km, mi, yd, ft): ").lower()

    if from_unit not in units or to_unit not in units:
        print("Unsupported unit!")
        return

    length = float(input(f"Enter length in {from_unit}: "))
    # Convert from source to meters, then meters to target
    length_in_m = length * units[from_unit]
    converted_length = length_in_m / units[to_unit]

    print(f"{length} {from_unit} = {converted_length} {to_unit}")

def main():
    while True:
        print("\nUnit Converter")
        print("1. Temperature")
        print("2. Currency")
        print("3. Length")
        print("4. Exit")
        choice = input("Choose conversion type (1-4): ")

        if choice == '1':
            temperature_converter()
        elif choice == '2':
            currency_converter()
        elif choice == '3':
            length_converter()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()
