import random
import time


#tu trzeba umieścić wszystkie klasy które chcemy wygenerować
klasy = []
#w sposób losowy

def losowe_generowanie_zdarzen(ilosc_czasu):
    poczatek = time.time()
    klasy_do_generowania = []

    while (time.time() - poczatek) < ilosc_czasu:
        losowa_klasa = random.choice(klasy)
        # tutaj instancja klasy mega ważne !!! bo wpisujemy parametry
        instancja_klasy = losowa_klasa()
        klasy_do_generowania. append(instancja_klasy)

        time.sleep(random.uniform(0.1,1.0))

    return klasy_do_generowania

wylosowane_klasy =  losowe_generowanie_zdarzen(10)
