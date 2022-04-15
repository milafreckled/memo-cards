from random import randint

def nrLosowy():
    nr = "LU "
    for i in range(5):
        wybor = randint(0, 2)
        if wybor==0:
            nr+=chr(randint(48, 58))
        else:
            nr+=chr(randint(65, 90))

    print("Numer rejestracyjny losowy: "+nr)

nrLosowy()
            
