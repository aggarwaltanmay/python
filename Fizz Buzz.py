for number in range(101):
    if number%3 == 0 :
        print(number)
        print("Fizz")

    if number%5 == 0 :
        print(number)
        print("Buzz")

    elif number%3 and 5 == 0 :
        print(number)
        print("FizzBuzz")