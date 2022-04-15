def podajSlownie(x):
    liczby = {0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć"}
    pierwsza = int(str(x)[0])
    wynik = liczby[pierwsza]
    print(wynik)

podajSlownie("hahaha")
podajSlownie(1197)
