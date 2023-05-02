from unidecode import unidecode

# Partie 1 : Structure de données

class Sommet():
    def __init__(self, entrant: list, sortant: list, nom: str=""):
        """
        Crée un sommet avec ses arcs entrants et sortants et son nom (optionnel)
        :param entrant: liste des arcs entrants
        :param sortant: liste des arcs sortants
        :param nom: nom du sommet
        """
        self.entrant = entrant
        self.sortant = sortant
        self.nom = nom

class Arc():
    """
    Crée un arc avec son nom, sa nature et sa durée (optionnel)
    :param nom: nom de l'arc
    :param nature: nature de l'arc (téléski, télésiège, télécabine, téléphérique, piste verte, piste bleue, piste rouge, piste noire)
    :param duree_1: temps de parcours de la remontée ou de la piste pour un débutant (optionnel)
    :param duree_2: temps de parcours de la piste pour un fonceur (optionnel)
    """
    
    echelle = 3.059e-3 # échelle de la carte
    attente_remontees = 10
    v_remontees = {"téléski": 12.5, "télésiège": 15, "télécabine": 22.5, "téléphérique": 30}
    v_pistes = {"piste verte": [20, 20], "piste bleue": [17.5, 35], "piste rouge": [15, 45], "piste noire": [12.5, 50]} # [vitesse débutant, vitesse fonceur]

    def __init__(self, nom: str, nature: str, duree_1: float=0, duree_2: float=0):
        self.nature = nature
        self.nom = nom
        if self.nature == ("téléski" or "télésiège" or "télécabine" or "téléphérique"):
            self.duree = (duree_1 / self.echelle) / (self.v_remontees[self.nature] / 3.6) / 60 + self.attente_remontees
        elif self.nature == ("piste verte" or "piste bleue" or "piste rouge" or "piste noire"):
            self.duree_1 = (duree_1 / self.echelle) / (self.v_pistes[self.nature][0] / 3.6) # durée pour un débutant
            self.duree_2 = (duree_2 / self.echelle) / (self.v_pistes[self.nature][1] / 3.6) # durée pour un fonceur


arcs = {
    # Téléskis
    "PYRAMIDE": Arc("PYRAMIDE", "téléski", 3.2),
    "SOURCES": Arc("SOURCES", "téléski", ),
    "ROCHER DE L'OMBRE": Arc("ROCHER DE L'OMBRE", "téléski"),
    "PRAZ JUGET": Arc("PRAZ JUGET", "téléski"),
    "BOUC BLANC": Arc("BOUC BLANC", "téléski"),
    "GROS MURGER": Arc("GROS MURGER", "téléski"),
    "LOZE": Arc("LOZE", "téléski"),
    "STADE": Arc("STADE", "téléski"),
    "EPICEA": Arc("EPICEA", "téléski"),
    "MARQUIS": Arc("MARQUIS", "téléski"),
    "STE AGATHE": Arc("STE AGATHE", "téléski"),
    "STADE": Arc("STADE", "téléski"),
    "GRANGES": Arc("GRANGES", "téléski"),
    "COMBE": Arc("COMBE", "téléski"),
    "PTE BOSSE": Arc("PTE BOSSE", "téléski"),
    # Télésièges
    "CHANROSSA": Arc("CHANROSSA", "télésiège", 4.3),
    "ROC MERLET": Arc("ROC MERLET", "télésiège", 1.6),
    "ROC MUGNIER": Arc("ROC MUGNIER", "télésiège"),
    "CREUX NOIRS": Arc("CREUX NOIRS", "télésiège"),
    "MARMOTTES": Arc("MARMOTTES", "télésiège"),
    "SUISSES": Arc("SUISSES", "télésiège"),
    "BIOLLAY": Arc("BIOLLAY", "télésiège"),
    "PRALONG": Arc("PRALONG", "télésiège"),
    "COQS": Arc("COQS", "télésiège"),
    "COL DE LA LOZE": Arc("COL DE LA LOZE", "télésiège"),
    "DOU DES LANCHES": Arc("DOU DES LANCHES", "télésiège"),
    "CRÊTES": Arc("CRÊTES", "télésiège"),
    "PLANTREY": Arc("PLANTREY", "télésiège"),
    "TOVETS": Arc("TOVETS", "télésiège"),
    "3 VALLÉES": Arc("3 VALLÉES", "télésiège"),
    "CHAPELETS": Arc("CHAPELETS", "télésiège"), 
    "SIGNAL": Arc("SIGNAL", "télésiège"),
    "GRAVELLES": Arc("GRAVELLES", "télésiège"),
    "AIGUILLE DU FRUIT": Arc("AIGUILLE DU FRUIT", "télésiège"),
    # Télécabines
    "VIZELLE": Arc("VIZELLE", "télécabine"),
    "JARDIN ALPIN": Arc("JARDIN ALPIN", "télécabine"),
    "LA TANIA": Arc("LA TANIA", "télécabine"),
    "FORET": Arc("FORET", "télécabine"),
    "PRAZ": Arc("PRAZ", "télécabine"),
    "CHENUS": Arc("CHENUS", "télécabine"),
    "VERDONS": Arc("VERDONS", "télécabine"),
    "GRANGETTES": Arc("GRANGETTES", "télécabine"),
    "ARIONDAZ": Arc("ARIONDAZ", "télécabine"),
    # Téléphériques
    "SAULIRE": Arc("SAULIRE", "téléphérique"),
    # Pistes vertes
    "Renard": Arc("Renard", "piste verte"),
    "Verdons": Arc("Verdons", "piste verte"),
    "Lac Bleu": Arc("Lac Bleu", "piste verte"),
    "Loze Est": Arc("Loze Est", "piste verte"),
    "Plan Fontaine": Arc("Plan Fontaine", "piste verte"),
    "Belvédère": Arc("Belvédère", "piste verte"),
    "Praline": Arc("Praline", "piste verte"),
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
    "Piste Bleue": Arc("Piste Bleue", "piste bleue"),
    "Marquis": Arc("Marquis", "piste bleue"),
    "Granges": Arc("Granges", "piste bleue"),
    "Carabosse": Arc("Carabosse", "piste bleue"),
    "Grandes Bosses": Arc("Grandes Bosses", "piste bleue"),
    "Ariondaz": Arc("Ariondaz", "piste bleue"),
    "Indiens": Arc("Indiens", "piste bleue"),
    "Gravelles": Arc("Gravelles", "piste bleue"),
    "Prameruel": Arc("Prameruel", "piste bleue"),
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
    "Stade": Arc("Stade", "piste rouge"),
    "Bel Air": Arc("Bel Air", "piste rouge"),
    "Rochers": Arc("Rochers", "piste rouge"),
    "Chapelets": Arc("Chapelets", "piste rouge"),
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

print(arcs["PYRAMIDE"].duree)

sommets = [
    Sommet(
        [arcs["CHANROSSA"], arcs["ROC MERLET"]],
        [arcs["Chanrossa"], arcs["Jean Pachod"], arcs["Roc Merlet"]],
        "CHANROSSA"
    ),
    Sommet(
        [arcs["Creux"], arcs["Jean Pachod"], arcs["Chanrossa"], arcs["Rama"]],
        [arcs["CHANROSSA"], arcs["MARMOTTES"], arcs["Creux"]],
        "CREUX"
    ),
    Sommet(
        [arcs["Roc Mugnier"], arcs["Creux"], arcs["Gravelles"], arcs["Cave des Creux"], arcs["Mur"], arcs["Prameruel"]],
        [arcs["ROC MUGNIER"], arcs["AIGUILLE DU FRUIT"], arcs["GRAVELLES"]],
        "PRAMEUEL"
    ),
    Sommet(
        [arcs["ROC MUGNIER"], arcs["COMBE"], arcs["Pyramide"], arcs["Mont Russes"], arcs["Plan Mugnier"], arcs["Grandes Bosses"]],
        [arcs["Roc Mugnier"], arcs["PYRAMIDE"], arcs["Grandes Bosses"]]
    ),
    Sommet(
        [arcs["PYRAMIDE"], arcs["Roc Merlet"]],
        [arcs["Plan Mugnier"], arcs["Mont Russes"], arcs["Pyramide"], arcs["ROC MERLET"]]
    ),
    Sommet(
        [arcs["CREUX NOIRS"]],
        [arcs["Roches Grises"]],
        "CREUX NOIRS"
    ),
    Sommet(
        [arcs["SAULIRE"]],
        [arcs["Grand Couloir"], arcs["Creux"], arcs["Combe Saulire"]],
        "SAULIRE"
    ),
    Sommet(
        [arcs["MARMOTTES"], arcs["SUISSES"], arcs["VIZELLE"], arcs["Combe Saulire"]],
        [arcs["Combe Saulire"], arcs["Combe Pylones"], arcs["m"], arcs["Turcs"], arcs["Suisses"]],
        "VIZELLE"
    ),
    Sommet(
        [arcs["Combe Pylones"], arcs["Combe Saulire"], arcs["Grand Couloir"], arcs["Biollay Verdons"], arcs["m"], arcs["VERDONS"], arcs["SOURCES"]],
        [arcs["VIZELLE"], arcs["SAULIRE"], arcs["Verdons"], arcs["Renard"], arcs["Biollay Verdons"]],
        "VERDONS"
    ),
    Sommet(
        [arcs["Combe Saulire"], arcs["Grand Couloir"], arcs["ROCHER DE L'OMBRE"]],
        [arcs["Stade Descente"], arcs["Combe Saulire"]]
    ),
    Sommet(
        [arcs["Lac Creux"]],
        [arcs["Lac Creux"], arcs["CREUX NOIRS"]]
    ),
    Sommet(
        [arcs["Turcs"], arcs["AIGUILLE DU FRUIT"]],
        [arcs["Turcs"], arcs["Park City"]]
    ),
    Sommet(
        [arcs["GRAVELLES"], arcs["Lac Creux"], arcs["Park City"]],
        [arcs["Cave des Creux"], arcs["Altiport"]]
    ),
    Sommet(
        [arcs["Turcs"], arcs["Suisses"], arcs["Altiport"], arcs["Super Pralong"]],
        [arcs["SUISSES"], arcs["Mur"], arcs["Altiport"]]
    ),
    Sommet(
        [arcs["PRALONG"]],
        [arcs["Super Pralong"], arcs["Pralong"], arcs["Biollay Verdons"], arcs["Marquetty"], arcs["Biollay"]]
    ),
    Sommet(
        [arcs["Pralong"], arcs["Altiport"]], # ajouter ALTIPORT
        [arcs["Prameruel"], arcs["Pralong"], arcs["Altiport"]]
    ),
    Sommet(
        [arcs["JARDIN ALPIN"], arcs["Biollay Verdons"]],
        []
    ),
    Sommet(
        [arcs["Biollay"], arcs["Altiport"]],
        [arcs["PRALONG"]], # ajouter ALTIPORT
        "PRALONG"
    ),
    Sommet(
        [arcs["COQS"], arcs["CHENUS"], arcs["CRÊTES"], arcs["PRAZ JUGET"], arcs["Col de la Loze"]],
        [arcs["Crêtes"], arcs["Lanches"], arcs["Chenus"], arcs["Anémones"], arcs["COL DE LA LOZE"], arcs["Lac Bleu"]],
        "CHENUS"
    ),
    Sommet(
        [arcs["COL DE LA LOZE"], arcs["DOU DES LANCHES"]],
        [arcs["Col de la Loze"], arcs["Dou des Lanches"]],
        "COL DE LA LOZE"
    ),
    Sommet(
        [arcs["Crêtes"], arcs["LOZE"], arcs["PLANTREY"], arcs["BOUC BLANC"]],
        [arcs["Crêtes"], arcs["Loze Est"], arcs["Loze"], arcs["Dou du Midi"], arcs["Petit Dou"], arcs["Jean Blanc"], arcs["Bouc Blanc"], arcs["Déviation 1550"]],
        "LOZE"
    ),
    Sommet(
        [arcs["Crêtes"], arcs["FORET"]],
        [arcs["CRÊTES"], arcs["Arolles"]]
    ),
    Sommet(
        [arcs["Dou des Lanches"], arcs["Bouc Blanc"], arcs["Arolles"], arcs["LA TANIA"]],
        [arcs["DOU DES LANCHES"], arcs["PRAZ JUGET"], arcs["Arolles"], arcs["Bouc Blanc"], arcs["Plan Fontaine"], arcs["Jockeys"], arcs["Murettes"]],
        "PRAZ JUGET"
    ),
    Sommet(
        [arcs["Arolles"], arcs["Bouc Blanc"], arcs["Plan Fontaine"], arcs["GROS MURGER"]],
        [arcs["BOUC BLANC"], arcs["Plan Fontaine"], arcs["Moretta Blanche"], arcs["Folyères"]]
    ),
    Sommet(
        [arcs["Folyères"], arcs["Plan Fontaine"], arcs["Moretta Blanche"]],
        [arcs["GROS MURGER"], arcs["LA TANIA"]],
        "LA TANIA"
    ),
    Sommet(
        [arcs["Brigues"], arcs["Amoureux"], arcs["Jockeys"], arcs["Murettes"], arcs["Jean Blanc"]],
        [arcs["Saint Bon"], arcs["PRAZ"], arcs["FORET"]],
        "COURCHEVEL - LE PRAZ - 1300m"
    ),
    Sommet(
        [arcs["Saint Bon"]],
        [],
        "ST BON - 1100m"
    ),
    Sommet(
        [arcs["Déviation 1550"], arcs["Dou du Midi"], arcs["Stade"], arcs["Provères"], arcs["Tovets"]],
        [arcs["TOVETS"], arcs["GRANGETTES"]],
        "COURCHEVEL - 1550m"
    ),
    Sommet(
        [arcs["Verdons"], arcs["Anémones"], arcs["Jantzen"], arcs["Loze"], arcs["GRANGETTES"], arcs["TOVETS"], arcs["Petit Dou"]],
        # On considère que seul Verdons relie Lac à ce sommet
        [arcs["JARDIN ALPIN"], arcs["VERDONS"], arcs["LOZE"], arcs["CHENUS"], arcs["Stade"], arcs["Tovets"], arcs["Provères"], arcs["Brigues"], arcs["Amoureux"]]
    ),
    Sommet(
        [arcs["Marquetty"], arcs["Renard"], arcs["Verdons"], arcs["Stade Descente"], arcs["Loze Est"], arcs["Lac Bleu"], arcs["Chenus"]],
        [arcs["BIOLLAY"], arcs["SOURCES"], arcs["ROCHER DE L'OMBRE"], arcs["COQS"], arcs["Verdons"]],
        "LAC"
    ),
    Sommet(
        [arcs["Piste Bleue"], arcs["Marquis"], arcs["Indiens"], arcs["Belvédère"]],
        [arcs["3 VALLÉES"], arcs["MARQUIS"], arcs["STE AGATHE"], arcs["ARIONDAZ"]],
        "COURCHEVEL - 1650m"
    ),
    Sommet(
        [arcs["Stade"], arcs["Granges"], arcs["Carabosse"], arcs["Praline"]],
        [arcs["STADE"], arcs["GRANGES"], arcs["Belvédère"]]
    ),
    Sommet(
        [arcs["Chapelets"], arcs["Rochers"], arcs["Bel Air"], arcs["Praline"]],
        [arcs["Praline"], arcs["CHAPELETS"]]
    ),
    Sommet(
        [arcs["CHAPELETS"], arcs["SIGNAL"]],
        [arcs["Chapelets"], arcs["Rochers"], arcs["Grandes Bosses"]],
        "SIGNAL"
    ),
    Sommet(
        [arcs["Rochers"], arcs["ARIONDAZ"]],
        [arcs["COMBE"], arcs["Rochers"], arcs["Bel Air"], arcs["Ariondaz"]],
        "BEL AIR"
    ),
    Sommet(
        [arcs["Ariondaz"], arcs["GRANGES"], arcs["MARQUIS"], arcs["3 VALLÉES"]],
        [arcs["SIGNAL"], arcs["Granges"], arcs["Carabosse"], arcs["Praline"], arcs["PTE BOSSE"], arcs["Indiens"], arcs["Piste Bleue"], arcs["Marquis"]],
        "BOSSES"
    ),
    Sommet(
        [arcs["PTE BOSSE"]],
        [arcs["Gravelles"]]
    ),
    Sommet(
        [arcs["STADE"]],
        [arcs["Stade"]]
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

#afficher_sommets_adjacents()

def ecrire_arcs(arcs, nom_fichier):
    """
    Écrit les arcs dans un fichier texte.
    :arcs: liste d'arcs
    :nom_fichier: nom du fichier dans lequel écrire
    :return: None
    """
    with open(nom_fichier, 'w') as f:
        for arc in arcs.values():
            nom_sans_accents = unidecode(arc.nom)
            nature_sans_accents = unidecode(arc.nature)
            f.write(f"{{'nom': '{nom_sans_accents}', 'nature': '{nature_sans_accents}'}}\n")

def ecrire_sommets(sommets, nom_fichier):
    """
    Écrit les sommets dans un fichier texte.
    :sommets: liste de sommets
    :nom_fichier: nom du fichier dans lequel écrire
    :return: None
    """
    with open(nom_fichier, 'w') as f:
        for sommet in sommets:
            entrant = [unidecode(arc.nom) for arc in sommet.entrant]
            sortant = [unidecode(arc.nom) for arc in sommet.sortant]
            nom = unidecode(sommet.nom) if sommet.nom else ""
            entrant_str = str(entrant)
            sortant_str = str(sortant)
            nom_str = f"'nom': '{nom}'" if nom else ""
            f.write(f"{{'entrant': {entrant_str}, 'sortant': {sortant_str}, {nom_str}}}\n")

#ecrire_arcs(arcs, "liste_pistes.txt")
#ecrire_sommets(sommets, "liste_sommets.txt")