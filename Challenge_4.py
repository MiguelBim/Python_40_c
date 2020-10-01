# CHALLENGE NUMBER 4
# Triangel hypotenuse and area calculation
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060716#overview

# NOTES
# hˆ2 = a^2 + bˆ2 (Teorema de Pitagoras)
# area = (b * a) / 2

def calculate_features(a, b):

    hypotenuse = round((a**2 + b**2)**(1/2), 2)
    area = round((a * b) / 2, 3)

    return hypotenuse, area


if __name__ == '__main__':
    a = float(input("What is the first leg of the triangle: "))
    b = float(input("What is the second leg of the triangle: "))
    hypotenuse, area = calculate_features(a, b)
    print("For a tirangle with legs of " + str(a) + " and " + str(b) + " the hypotenuse is " + str(hypotenuse))
    print("For a tirangle with legs of " + str(a) + " and " + str(b) + " the area is " + str(area))
