def convert_to_celsius(fahrenheit):

  global CELSIUS_TO_FAHRENHEIT_FACTOR  # Access global factor (5/9 here)
  return (fahrenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR

def convert_to_fahrenheit(celsius):

  global FAHRENHEIT_TO_CELSIUS_FACTOR  
  return (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def main():
  
  try:
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if unit == 'C':
      converted_temp = convert_to_fahrenheit(temperature)
      unit_label = "°C"
      converted_unit_label = "°F"
    elif unit == 'F':
      converted_temp = convert_to_celsius(temperature)
      unit_label = "°F"
      converted_unit_label = "°C"
    else:
      raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    print(f"{temperature}{unit_label} is {converted_temp:.2f}{converted_unit_label}")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()