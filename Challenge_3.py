# CHALLENGE NUMBER 3
# Temperature conversion app from F to C and K
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060716#overview

# NOTES
# F to C -> Deduct 32, then multiply by 5, then divide by 9
# F to K -> Deduct 32, then multiply by 5, divide by 9 then add 273.15 ( = C + 273.15)

def convert_temperature(f_degress):
    c_degrees = round(((float(f_degress) - 32) * 5) / 9, 4)
    k_degrees = round(c_degrees + 273.15, 4)
    return c_degrees, k_degrees


if __name__ == '__main__':
    f_degrees = input("Welcome to the Temperature Conversion App\n\nWhat is the given temperature in degrees Fahrenheit: ")
    c_degrees, k_degrees = convert_temperature(f_degrees)
    print("Degrees Fahrenheit:\t" + f_degrees + "\nDegrees Celsius:\t" + str(c_degrees) + "\nDegrees Kelvin:\t\t" + str(k_degrees))
