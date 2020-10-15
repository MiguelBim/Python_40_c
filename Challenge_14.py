# CHALLENGE NUMBER 14
# TOPIC: For loop
# Factorial Calculator App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060784#overview


def fibonacci_sequence(num):

    current = 1
    fib_num = 0

    print("\nThe first " + str(num) + " numbers of the Fibonacci Sequence are: ")
    for digit in range(num):
        previous = current
        current = fib_num
        fib_num = previous + current
        print(fib_num)

    current = 1
    fib_num = 0
    print("\nThe corresponding Golden Ratio values are: ")
    for digit in range(num + 1):
        previous = current
        current = fib_num
        fib_num = previous + current
        if current and previous != 0:
            gold_ratio = float(current) / float(previous)
            print(gold_ratio)

    print("The ratio of the consecutive Fibonacci terms approaches Phi; 1.618..")


    return


if __name__ == '__main__':
    print("Welcome to the Fibonacci Calculator App.")
    digits = int(input("\nHow many digits of the Fibonacci Sequence would you like to compute: "))
    fibonacci_sequence(digits)