class Osoba:
    def __init__(self, imie, nazwisko, PESEL):
        self.imie = imie
        self.nazwisko = nazwisko
        self.PESEL = PESEL


    def __eq__(self, os):
        return self.PESEL==os.PESEL


pierwsza = Osoba("Marek", "Markowicz", "01234567890", "Lublin")
druga = Osoba("Konrad", "Markowicz", "01234567890", "Warszawa")
print(pierwsza == druga)
print(pierwsza == trzecia)

