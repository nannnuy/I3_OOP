class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        print(f"Celsius: {celsius}")
        print(f"Fahrenheit: {9.0/5*celsius + 32}")


    def fahrenheit_to_celsius(fahrenheit):
        print(f"Fahrenheit: {fahrenheit}")
        celsius = 5.0/9*(fahrenheit - 32)
        print(f"Celsius: {celsius}")


    def celsius_to_kelvin(celsius):
        print(f"Kelvin: {celsius+273.15}")
        

Temperature.celsius_to_fahrenheit(25)
Temperature.celsius_to_kelvin(25)
    