def czy_kolizja(hitbox, inny_obiekt ):
    if(hibox['x'] < inny_obiekt['x'] + inny_obiekt['szerokosc'] and
   hitbox['x'] + hitbox['szerokosc'] >  inny_obiekt['x']:
       if (hitbox1['y'] < hitbox2['y'] + hitbox2['wysokość'] and
            hitbox1['y'] + hitbox1['wysokość'] > hitbox2['y']):


             return True
    return False

