dopuszczalnaroznica = 20

#pierwsza wersja funckji dla podejścia bardziej obiektowego
def czynnosc (obiekt1, obiekt2):
    roznicax = abs(obiekt1.x - obiekt2.x)
    roznicay = abs(obiekt.y - obiekt2.y)

    if roznicax < dopuszczalnaroznica or roznicay < dopuszczalnaroznica:
        # reszta kodu czyli co się dzieje jeżeli
        obiekt1.x -= 10
        obiekt2.x += 10
    else :
        break;
    break;


#podejście nie obiektowe
def czynnosc(x1, y1, x2, y2):
    roznicax = x1 - x2
    roznicay = y1 - y2

    while True:

        if -dopuszczalnaroznica < roznicax < 0:
            x1 += 5
            x2 -= 5
        elif 0 < roznicax < dopuszczalnaroznica:
            x1 -= 5
            x2 += 5
        elif -dopuszczalnaroznica < roznicay < 0:
            y1 += 5
            y2 -= 5
        elif 0 < roznicay < dopuszczalnaroznica:
            y1 -= 5
            y2 += 5
        else:
            break
