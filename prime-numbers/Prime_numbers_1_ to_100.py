def prime_checker(number):
    prime = False
    if number % 2 == 0:
        if number == 2:
            prime = True
    elif number % 3 == 0:
        if number == 3:
            prime = True
    elif number % 5 == 0:
        if number == 5:
            prime = True
    elif number % 7 == 0:
        if number == 7:
            prime = True
    else:
        prime = True
    if prime:
        print(f"{number} : It's a prime number.")
    else:
        print(f"{number} : It's not a prime number.")


# n = int(input("Check this number: "))
for n in range(1, 101):
    prime_checker(number=n)
