def czy_kolizja(hitbox, inny_obiekt ):
    if(hibox['x'] < inny_obiekt['x'] + inny_obiekt['szerokosc'] and
   hitbox['x'] + hitbox['szerokosc'] >  inny_obiekt['x']:
       if (hitbox1['y'] < hitbox2['y'] + hitbox2['wysokość'] and
            hitbox1['y'] + hitbox1['wysokość'] > hitbox2['y']):


             return True
    return False

def odbicie(hitbox, inny_obiekt):
    # Jeśli występuje kolizja, oblicz kierunek odbicia
    if czy_kolizja(hitbox, inny_obiekt):
        # Oblicz różnicę położenia między hitboxami
        dx = (hitbox['x'] + hitbox['szerokość']/2) - (inny_obiekt['x'] + inny_obiekt['szerokość']/2)
        dy = (hitbox['y'] + hitbox['wysokość']/2) - (inny_obiekt['y'] + inny_obiekt['wysokość']/2)

        # Jeśli wartość bezwzględna dx jest większa niż wartość bezwzględna dy,
        # odbicie będzie w kierunku poziomym
        if abs(dx) > abs(dy):
            hitbox['predkosc_x'] *= -1
            inny_obiekt['predkosc_x'] *= -1
        # W przeciwnym razie odbicie będzie w kierunku pionowym
        else:
            hitbox['predkosc_y'] *= -1
            inny_obiekt['predkosc_y'] *= -1
