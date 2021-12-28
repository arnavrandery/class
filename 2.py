var = int(input("Enter a number: "))

if var % 3 == 0 and var % 5 == 0:
    print("fizzbuzz")
elif var % 3 == 0:
    print("fizz")
elif var % 5 == 0:
    print("buzz")
else:
    print(var)
