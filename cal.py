def calculate(x,y,znak):
    if znak == "+":
      wynik = (x+y)
      return wynik
    if znak == "-":
        wynik = (x-y)
        return wynik
    if znak == "*":
        wynik = (x*y)
        return wynik
    if znak == "/":
        wynik = (x/y)
        return wynik

while True:
    x = input("podaj pierwsza liczbe (albo litere aby wyjsc) ")
    try:
        x = int(x)
    except ValueError:
        break
    znak = input("jakie działanie chcesz wykonać(wpisz znak) ")
    y = int(input("podaj druga liczbe "))
    wynik = calculate(x,y,znak)
    print("Wynik: {}".format(wynik))
