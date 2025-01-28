class TemperatureConverter():
    #constances Class variables

    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9

    def convert_temperature(self, original, value):
        if original == self.FAHRENHEIT:
            return self.fahrenheit_to_celsius(value)
        elif original == self.CELSIUS:
            return self.celsius_to_fahrenheit(value)

#object
MyConverter = TemperatureConverter()
Celsius = MyConverter.convert_temperature('F', 27)
Fahrenheit = MyConverter.convert_temperature('C', 90)
print(Celsius)
print(Fahrenheit)
MyConverter.ErrorMargin = 0.001

print(f"{Celsius} + {MyConverter.ErrorMargin} OR {Celsius} - {MyConverter.ErrorMargin}  ")
print(f"{Fahrenheit} + {MyConverter.ErrorMargin} OR {Fahrenheit} - {MyConverter.ErrorMargin}  ")
