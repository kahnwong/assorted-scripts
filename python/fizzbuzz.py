numbers = list(range(1, 100))

# ~ for number in numbers:
# ~ if number % 15 == 0:
# ~ print('FizzBuzz')
# ~ elif number % 5 == 0:
# ~ print('Buzz')
# ~ elif number % 3 == 0:
# ~ print('Fizz')
# ~ else:
# ~ print(number)

a = 3
b = 5


for i in numbers:
    output = ""

    if i % a == 0:
        output += "Fizz"
    if i % b == 0:
        output += "Buzz"

    if output:
        print(output, i)
    else:
        print(i)
