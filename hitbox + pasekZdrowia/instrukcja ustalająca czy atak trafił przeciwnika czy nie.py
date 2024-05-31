#to powinno się znajdować w pętli while i za każdym razem sprawdzać
#czy koordynaty pocisku się nie pokrywają z tymi od postaci


def sprawdzenie_kolizji(wsp_pocisku, postac, damage, roznica=20):
    wsp_x, wsp_y = wsp_pocisku
#napisałem postac.x oraz postac.y jakby funcja pobierała dane z klasy ale nie wiem czy ostatecznie będzie klasa postać
    if abs(wsp_x - postac.x) < roznica and abs(wsp_y - postac.y) < roznica:
        postac.health -= damage
        return True
    return False
