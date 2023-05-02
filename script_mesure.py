import math

while True:
    largeur = int(input("Entrez la largeur en pixels : "))
    longueur = int(input("Entrez la longueur en pixels : "))
    diagonale = math.sqrt(largeur**2 + longueur**2)
    print("La longueur de la diagonale est de", round(diagonale, 2), "pixels\n")