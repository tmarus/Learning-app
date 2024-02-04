import random
a = random.randint(1, 10)
b = random.randint(1, 10)
text = float(input(f"Ile to jest {a} * {b}: "))
wynik = a*b


if text==wynik:
    print(f"Gratulacje wynik {wynik}")
else:
    print(f"Źle poprawny wynik {wynik}")


