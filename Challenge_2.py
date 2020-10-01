
# CHALLENGE NUMBER 2
# Convert MPH (Miles Per Hour) to MPS (Meters per second)
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060712#overview

# NOTES
# 2 decimal places for result
# 1 MPH = 1.60934 KPH

from decimal import Decimal


def mph_to_mps(actual_value):

    kph_value = round(Decimal((((float(actual_value) * 1.60934) * 1000) / 60) / 60), 2)
    print("Your speed in meters per second is " + str(kph_value))


if __name__ == '__main__':
    print("Welcome to the MPH to MPS Convertion App\n")
    mph_velocity = input("What is your speed in miles per hour: ")
    mph_to_mps(mph_velocity)