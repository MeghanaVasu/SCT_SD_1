def convert_temperature(value, from_scale, to_scale):
    # Convert input to Celsius first
    if from_scale == 'F':
        celsius = (value - 32) * 5/9
    elif from_scale == 'K':
        celsius = value - 273.15
    else:
        celsius = value

    # Convert Celsius to target scale
    if to_scale == 'F':
        return (celsius * 9/5) + 32
    elif to_scale == 'K':
        return celsius + 273.15
    else:
        return celsius

# Example usage:
temp = float(input("Enter temperature value: "))
f_scale = input("From scale (C/F/K): ").upper()
t_scale = input("To scale (C/F/K): ").upper()

result = convert_temperature(temp, f_scale, t_scale)
print(f"{temp}°{f_scale} is equal to {result:.2f}°{t_scale}")