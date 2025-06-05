def rekursiivinen_funktio(luku):
    if luku <= 1:
        return 1
    else:
        return luku * rekursiivinen_funktio(luku - 1)
    
print(rekursiivinen_funktio(3))  # Esimerkki: tulostaa 120, joka on 5!