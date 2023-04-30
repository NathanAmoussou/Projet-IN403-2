# Partie 1 : Structure de données

class Sommet():
    def __init__(self, entrant: list, sortant: list):
        self.entrant = entrant
        self.sortant = sortant

class Arc():
    def __init__(self, nom: str, nature: str, duree: float=0):
        self.nature = nature
        self.nom = nom
        self.duree = duree

# Exemple :
#abs

arcs = {
    # Téléskis
    "PYRAMIDE": Arc("PYRAMIDE", "téléski"),
    "SOURCES": Arc("SOURCES", "téléski"),
    "ROCHER DE L'OMBRE": Arc("ROCHER DE L'OMBRE", "téléski"),
    "PRAZ JUGET": Arc("PRAZ JUGET", "téléski"),
    "BOUT BLANC": Arc("BOUT BLANC", "téléski"),
    "GROS MURGER": Arc("GROS MURGER", "téléski"),
    "LOZE": Arc("LOZE", "téléski"),
    "STADE": Arc("STADE", "téléski"),
    "EPICEA": Arc("EPICEA", "téléski"),
    # Télésièges
    "CHANROSSA": Arc("CHANROSSA", "télésiège"),
    "ROC MERLET": Arc("ROC MERLET", "télésiège"),
    "ROC MUGNIER": Arc("ROC MUGNIER", "télésiège"),
    "CREUX NOIRS": Arc("CREUX NOIRS", "télésiège"),
    "MARMOTTES": Arc("MARMOTTES", "télésiège"),
    "SUISSES": Arc("SUISSES", "télésiège"),
    "BIOLLAY": Arc("BIOLLAY", "télésiège"),
    "PRALONG": Arc("PRALONG", "télésiège"),
    "COOS": Arc("COOS", "télésiège"),
    "COL DE LA LOZE": Arc("COL DE LA LOZE", "télésiège"),
    "DOU DES LANCHES": Arc("DOU DES LANCHES", "télésiège"),
    "CRÊTES": Arc("CRÊTES", "télésiège"),
    "PLANTREY": Arc("PLANTREY", "télésiège"),
    "TOVETS": Arc("TOVETS", "télésiège"),
    # Télécabines
    "VIZELLE": Arc("VIZELLE", "télécabine"),
    "JARDIN ALPIN": Arc("JARDIN ALPIN", "télécabine"),
    "LA TANIA": Arc("LA TANIA", "télécabine"),
    "FORET": Arc("FORET", "télécabine"),
    "PRAZ": Arc("PRAZ", "télécabine"),
    "CHENUS": Arc("CHENUS", "télécabine"),
    "VERDONS": Arc("VERDONS", "télécabine"),
    "GRANGETTES": Arc("GRANGETTES", "télécabine"),
    # Téléphériques
    "SAULIRE": Arc("SAULIRE", "téléphérique"),
    # Pistes vertes
    "Renard": Arc("Renard", "piste verte"),
    "Verdons": Arc("Verdons", "piste verte"),
    "Lac Bleu": Arc("Lac Bleu", "piste verte"),
    "Loze Est": Arc("Loze Est", "piste verte"),
    "Plan Fontaine": Arc("Plan Fontaine", "piste verte"),
    # Pistes bleues
    "Plan Mugnier": Arc("Plan Mugnier", "piste bleue"),
    "Mont Russes": Arc("Mont Russes", "piste bleue"),
    "Pyramide": Arc("Pyramide", "piste bleue"),
    "Altiport": Arc("Altiport", "piste bleue"),
    "Super Pralong": Arc("Super Pralong", "piste bleue"),
    "Pralong": Arc("Pralong", "piste bleue"),
    "Biollay Verdons": Arc("Biollay Verdons", "piste bleue"),
    "Biollay": Arc("Biollay", "piste bleue"),
    "Anémones": Arc("Anémones", "piste bleue"),
    "Col de la Loze": Arc("Col de la Loze", "piste bleue"),
    "Folyères": Arc("Folyères", "piste bleue"),
    "Arolles": Arc("Arolles", "piste bleue"),
    "Crêtes": Arc("Crêtes", "piste bleue"),
    "Stade": Arc("Stade", "piste bleue"),
    "Tovets": Arc("Tovets", "piste bleue"),
    "Provères": Arc("Provères", "piste bleue"),
    "Cospillot": Arc("Cospillot", "piste bleue"),
    # Pistes rouges
    "Jean Pachod": Arc("Jean Pachod", "piste rouge"),
    "Roc Merlet": Arc("Roc Merlet", "piste rouge"),
    "Creux": Arc("Creux", "piste rouge"),
    "Roc Mugnier": Arc("Roc Mugnier", "piste rouge"),
    "Lac Creux": Arc("Lac Creux", "piste rouge"),
    "Roches Grises": Arc("Roches Grises", "piste rouge"),
    "Combe Saulire": Arc("Combe Saulire", "piste rouge"),
    "Park City": Arc("Park City", "piste rouge"),
    "Rama": Arc("Rama", "piste rouge"),
    "Stade Descente": Arc("Stade Descente", "piste rouge"),
    "Marquetty": Arc("Marquetty", "piste rouge"),
    "Cave des Creux": Arc("Cave des Creux", "piste rouge"),
    "Mur": Arc("Mur", "piste rouge"),
    "Lanches": Arc("Lanches", "piste rouge"),
    "Bouc Blanc": Arc("Bouc Blanc", "piste rouge"),
    "Moretta Blanche": Arc("Moretta Blanche", "piste rouge"),
    "Murettes": Arc("Murettes", "piste rouge"),
    "Amoureux": Arc("Amoureux", "piste rouge"),
    "Saint Bon": Arc("Saint Bon", "piste rouge"),
    "Brigues": Arc("Brigues", "piste rouge"),
    "Loze": Arc("Loze", "piste rouge"),
    "Dou du Midi": Arc("Dou du Midi", "piste rouge"),
    "Petit Dou": Arc("Petit Dou", "piste rouge"),
    "Jantzen": Arc("Jantzen", "piste rouge"),
    "Chenus": Arc("Chenus", "piste rouge"),
    "Déviation 1550": Arc("Déviation 1550", "piste rouge"),
    # Pistes noires
    "Chanrossa": Arc("Chanrossa", "piste noire"),
    "Turcs": Arc("Turcs", "piste noire"),
    "Suisses": Arc("Suisses", "piste noire"),
    "Combe Pylones": Arc("Combe Pylones", "piste noire"),
    "Grand Couloir": Arc("Grand Couloir", "piste noire"),
    "m": Arc("m", "piste noire"),
    "Dou des Lanches": Arc("Dou des Lanches", "piste noire"),
    "Jockeys": Arc("Jockeys", "piste noire"),
    "Jean Blanc": Arc("Jean Blanc", "piste noire"),
}

sommets = [
    Sommet(
        [arcs["CHANROSSA"], arcs["ROC MERLET"]],
        [arcs["Chanrossa"], arcs["Jean Pachod"], arcs["Roc Merlet"]]
    ),
    Sommet(
        [arcs["Creux"], arcs["Jean Pachod"], arcs["Chanrossa"]],
        [arcs["CHANROSSA"]]
    ),
    Sommet(
        [arcs["Roc Mugnier"], arcs["Creux"]],
        [arcs["ROC MUGNIER"]]
    ),
    Sommet(
        [arcs["ROC MUGNIER"], arcs["Pyramide"], arcs["Mont Russes"], arcs["Plan Mugnier"]],
        [arcs["Roc Mugnier"], arcs["PYRAMIDE"]]
    ),
    Sommet(
        [arcs["PYRAMIDE"], arcs["Roc Merlet"]],
        [arcs["Plan Mugnier"], arcs["Mont Russes"], arcs["Pyramide"], arcs["ROC MERLET"]]
    )
]

# Exemple

def afficher_sommets_adjacents():
    print("Requête type : Je suis en haut de Chanrossa.")
    input_utilisateur = input("Où êtes-vous ? ")
    input_utilisateur = input_utilisateur.strip(".").split(" ")
    indice_localisation = input_utilisateur.index("de")
    localisation = " ".join(input_utilisateur[indice_localisation+1:])
    #print(localisation)
    sommet_localisation = None
    if "haut" in input_utilisateur:
        i = 0
        while sommet_localisation is None:
            if arcs[localisation] in sommets[i].entrant:
                sommet_localisation = sommets[i]
        i += 1
    elif "bas" in input_utilisateur:
        pass
    print(sommet_localisation)
    print(sommets[0])

afficher_sommets_adjacents()
