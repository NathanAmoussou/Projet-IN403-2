# Structure de données

class Sommet():
    def __init__(self, entrant: list=[], sortant: list=[], nom: str=""):
        """
        Crée un sommet avec ses arcs entrants et sortants et son nom (optionnel)
        :param entrant: liste des arcs entrants
        :param sortant: liste des arcs sortants
        :param nom: nom du sommet
        """
        self.entrant = entrant
        self.sortant = sortant
        self.nom = nom
    
    def get_entrant(self):
        """
        Renvoie la liste des arcs entrants
        :return: liste des arcs entrants
        """
        return self.entrant
    
    def get_sortant(self):
        """
        Renvoie la liste des arcs sortants
        :return: liste des arcs sortants
        """
        return self.sortant
    
    def get_nom(self):
        """
        Renvoie le nom du sommet
        :return: nom du sommet
        """
        return self.nom

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
        if self.nature == "téléski" or self.nature == "télésiège" or self.nature == "télécabine" or self.nature == "téléphérique":
            self.duree = (duree_1 / self.echelle) / (self.v_remontees[self.nature] / 3.6) / 60 + self.attente_remontees
        elif self.nature == "piste verte" or self.nature == "piste bleue" or self.nature == "piste rouge" or self.nature == "piste noire":
            self.duree_1 = (duree_1 / self.echelle) / (self.v_pistes[self.nature][0] / 3.6) / 60 # durée pour un débutant
            self.duree_2 = (duree_1 / self.echelle) / (self.v_pistes[self.nature][1] / 3.6) / 60 # durée pour un fonceur
    
    def get_duree(self, niveau: str="débutant"):
        """
        Renvoie la durée de l'arc
        :param niveau: niveau de ski (débutant ou fonceur)
        :return: durée de l'arc
        """
        if niveau == "débutant":
            return self.duree_1
        elif niveau == "fonceur":
            return self.duree_2
        else:
            raise ValueError("Le niveau doit être débutant ou fonceur")
        
    def get_nom(self):
        """
        Renvoie le nom de l'arc
        :return: nom de l'arc
        """
        return self.nom
    
    def get_nature(self):
        """
        Renvoie la nature de l'arc
        :return: nature de l'arc
        """
        return self.nature

arcs = {
    # Téléskis
    "PYRAMIDE": Arc("PYRAMIDE", "téléski", 3.2),
    "SOURCES": Arc("SOURCES", "téléski", 2.3),
    "ROCHER DE L'OMBRE": Arc("ROCHER DE L'OMBRE", "téléski", 3.3),
    "PRAZ JUGET": Arc("PRAZ JUGET", "téléski", 3.5),
    "BOUC BLANC": Arc("BOUC BLANC", "téléski", 4.8),
    "GROS MURGER": Arc("GROS MURGER", "téléski", 3.3),
    "LOZE": Arc("LOZE", "téléski", 3.7),
    "STADE": Arc("STADE", "téléski", 1.1),
    "EPICEA": Arc("EPICEA", "téléski", 1.7),
    "MARQUIS": Arc("MARQUIS", "téléski", 4),
    "STE AGATHE": Arc("STE AGATHE", "téléski", 1.5),
    "STADE": Arc("STADE", "téléski", 2),
    "GRANGES": Arc("GRANGES", "téléski", 1.5),
    "COMBE": Arc("COMBE", "téléski", 1.7),
    "PTE BOSSE": Arc("PTE BOSSE", "téléski", 0.9),
    # Télésièges
    "CHANROSSA": Arc("CHANROSSA", "télésiège", 4.3),
    "ROC MERLET": Arc("ROC MERLET", "télésiège", 1.6),
    "ROC MUGNIER": Arc("ROC MUGNIER", "télésiège", 3.6),
    "CREUX NOIRS": Arc("CREUX NOIRS", "télésiège", 3.6),
    "MARMOTTES": Arc("MARMOTTES", "télésiège", 4.9),
    "SUISSES": Arc("SUISSES", "télésiège", 4.3),
    "BIOLLAY": Arc("BIOLLAY", "télésiège", 3.3),
    "PRALONG": Arc("PRALONG", "télésiège", 3.1),
    "COQS": Arc("COQS", "télésiège", 3.7),
    "COL DE LA LOZE": Arc("COL DE LA LOZE", "télésiège", 2.5),
    "DOU DES LANCHES": Arc("DOU DES LANCHES", "télésiège", 2.5),
    "CRÊTES": Arc("CRÊTES", "télésiège", 2),
    "PLANTREY": Arc("PLANTREY", "télésiège", 3.5),
    "TOVETS": Arc("TOVETS", "télésiège", 2),
    "3 VALLÉES": Arc("3 VALLÉES", "télésiège", 4.3),
    "CHAPELETS": Arc("CHAPELETS", "télésiège", 3.5), 
    "SIGNAL": Arc("SIGNAL", "télésiège", 4.5),
    "GRAVELLES": Arc("GRAVELLES", "télésiège", 2.2),
    "AIGUILLE DU FRUIT": Arc("AIGUILLE DU FRUIT", "télésiège", 4.6),
    # Télécabines
    "VIZELLE": Arc("VIZELLE", "télécabine", 3.8),
    "JARDIN ALPIN": Arc("JARDIN ALPIN", "télécabine", 3.2),
    "LA TANIA": Arc("LA TANIA", "télécabine", 5.2),
    "FORET": Arc("FORET", "télécabine", 4.6),
    "PRAZ": Arc("PRAZ", "télécabine", 5),
    "CHENUS": Arc("CHENUS", "télécabine", 4.3),
    "VERDONS": Arc("VERDONS", "télécabine", 4),
    "GRANGETTES": Arc("GRANGETTES", "télécabine", 2.3),
    "ARIONDAZ": Arc("ARIONDAZ", "télécabine", 5.6),
    # Téléphériques
    "SAULIRE": Arc("SAULIRE", "téléphérique", 4.1),
    # Pistes vertes
    "Renard": Arc("Renard", "piste verte", 2.3),
    "Verdons A": Arc("Verdons A", "piste verte", 2.3),
    "Verdons B": Arc("Verdons B", "piste verte", 1.7),
    "Lac Bleu": Arc("Lac Bleu", "piste verte", 3.7),
    "Loze Est": Arc("Loze Est", "piste verte", 3.4),
    "Plan Fontaine A": Arc("Plan Fontaine A", "piste verte", 2.1),
    "Plan Fontaine B": Arc("Plan Fontaine B", "piste verte", 3.3),
    "Belvédère": Arc("Belvédère", "piste verte", 3.2),
    "Praline A": Arc("Praline A", "piste verte", 3),
    "Praline B": Arc("Praline B", "piste verte", 2.5),
    # Pistes bleues
    "Plan Mugnier": Arc("Plan Mugnier", "piste bleue", 3.2),
    "Mont Russes": Arc("Mont Russes", "piste bleue", 3.2),
    "Pyramide": Arc("Pyramide", "piste bleue", 3.2),
    "Altiport A": Arc("Altiport A", "piste bleue", 0.7),
    "Altiport B": Arc("Altiport B", "piste bleue", 2.4),
    "Altiport C": Arc("Altiport C", "piste bleue", 1.2),
    "Super Pralong": Arc("Super Pralong", "piste bleue", 1.8),
    "Pralong A": Arc("Pralong A", "piste bleue", 1.7),
    "Pralong B": Arc("Pralong B", "piste bleue", 1.8),
    "Biollay Verdons A": Arc("Biollay Verdons A", "piste bleue", 1.8),
    "Biollay Verdons B": Arc("Biollay Verdons B", "piste bleue", 1.7),
    "Biollay": Arc("Biollay", "piste bleue", 3.2),
    "Anémones": Arc("Anémones", "piste bleue", 4.3),
    "Col de la Loze": Arc("Col de la Loze", "piste bleue", 2.5),
    "Folyères": Arc("Folyères", "piste bleue", 3.3),
    "Arolles A": Arc("Arolles A", "piste bleue", 1.5),
    "Arolles B": Arc("Arolles B", "piste bleue", 2.3),
    "Crêtes A": Arc("Crêtes A", "piste bleue", 1),
    "Crêtes B": Arc("Crêtes B", "piste bleue", 1.5),
    "Stade": Arc("Stade", "piste bleue", 2.3),
    "Tovets": Arc("Tovets", "piste bleue", 2.3),
    "Provères": Arc("Provères", "piste bleue", 2.3),
    "Cospillot": Arc("Cospillot", "piste bleue"),
    "Piste Bleue": Arc("Piste Bleue", "piste bleue", 4.1),
    "Marquis": Arc("Marquis", "piste bleue", 4.1),
    "Granges": Arc("Granges", "piste bleue", 1.5),
    "Carabosse": Arc("Carabosse", "piste bleue", 1.2),
    "Grandes Bosses A": Arc("Grandes Bosses A", "piste bleue", 1.8),
    "Grandes Bosses B": Arc("Grandes Bosses B", "piste bleue", 3),
    "Ariondaz": Arc("Ariondaz", "piste bleue", 1.7),
    "Indiens": Arc("Indiens", "piste bleue", 4.1),
    "Gravelles": Arc("Gravelles", "piste bleue", 0.6),
    "Prameruel": Arc("Prameruel", "piste bleue", 3.1),
    # Pistes rouges
    "Jean Pachod": Arc("Jean Pachod", "piste rouge", 4.4),
    "Roc Merlet": Arc("Roc Merlet", "piste rouge", 1.7),
    "Creux A": Arc("Creux A", "piste rouge", 6.2),
    "Creux B": Arc("Creux B", "piste rouge", 2.7),
    "Roc Mugnier": Arc("Roc Mugnier", "piste rouge", 3.6),
    "Lac Creux A": Arc("Lac Creux A", "piste rouge", 3.5),
    "Lac Creux B": Arc("Lac Creux B", "piste rouge", 2.6),
    "Roches Grises": Arc("Roches Grises", "piste rouge", 3.6),
    "Combe Saulire A": Arc("Combe Saulire A", "piste rouge", 1.3),
    "Combe Saulire B": Arc("Combe Saulire B", "piste rouge", 3.2),
    "Combe Saulire C": Arc("Combe Saulire C", "piste rouge", 1.2),
    "Park City": Arc("Park City", "piste rouge", 2.3),
    "Rama": Arc("Rama", "piste rouge", 1.5),
    "Stade Descente": Arc("Stade Descente", "piste rouge", 3.3),
    "Marquetty": Arc("Marquetty", "piste rouge", 3.4),
    "Cave des Creux": Arc("Cave des Creux", "piste rouge", 2.2),
    "Mur": Arc("Mur", "piste rouge", 2.8),
    "Lanches": Arc("Lanches", "piste rouge", 3.5),
    "Bouc Blanc A": Arc("Bouc Blanc A", "piste rouge", 2.7),
    "Bouc Blanc B": Arc("Bouc Blanc B", "piste rouge", 2),
    "Moretta Blanche": Arc("Moretta Blanche", "piste rouge", 3.3),
    "Murettes": Arc("Murettes", "piste rouge", 3.8),
    "Amoureux": Arc("Amoureux", "piste rouge", 6),
    "Saint Bon": Arc("Saint Bon", "piste rouge", 4),
    "Brigues": Arc("Brigues", "piste rouge", 6),
    "Loze": Arc("Loze", "piste rouge", 3.7),
    "Dou du Midi": Arc("Dou du Midi", "piste rouge", 5.5),
    "Petit Dou": Arc("Petit Dou", "piste rouge", 3.7),
    "Jantzen": Arc("Jantzen", "piste rouge", 4.3),
    "Chenus": Arc("Chenus", "piste rouge", 3.7),
    "Déviation 1550": Arc("Déviation 1550", "piste rouge", 5.5),
    "Stade": Arc("Stade", "piste rouge", 1.1),
    "Bel Air": Arc("Bel Air", "piste rouge", 2.1),
    "Rochers A": Arc("Rochers A", "piste rouge", 2.8),
    "Rochers B": Arc("Rochers B", "piste rouge", 2.1),
    "Chapelets": Arc("Chapelets", "piste rouge", 3.5),
    # Pistes noires
    "Chanrossa": Arc("Chanrossa", "piste noire", 4.45),
    "Turcs A": Arc("Turcs A", "piste noire", 2.3),
    "Turcs B": Arc("Turcs B", "piste noire", 2.3),
    "Suisses": Arc("Suisses", "piste noire", 4.6),
    "Combe Pylones": Arc("Combe Pylones", "piste noire", 3.2),
    "Grand Couloir": Arc("Grand Couloir", "piste noire", 3.2),
    "m": Arc("m", "piste noire", 4),
    "Dou des Lanches": Arc("Dou des Lanches", "piste noire", 2.5),
    "Jockeys": Arc("Jockeys", "piste noire", 3.8),
    "Jean Blanc": Arc("Jean Blanc", "piste noire", 6),
}

sommets = [
    Sommet(
        [arcs["CHANROSSA"], arcs["ROC MERLET"]],
        [arcs["Chanrossa"], arcs["Jean Pachod"], arcs["Roc Merlet"]],
        "CHANROSSA"
    ),
    Sommet(
        [arcs["Creux A"], arcs["Jean Pachod"], arcs["Chanrossa"], arcs["Rama"]],
        [arcs["CHANROSSA"], arcs["MARMOTTES"], arcs["Creux B"]],
        "CREUX"
    ),
    Sommet(
        [arcs["Roc Mugnier"], arcs["Creux B"], arcs["Gravelles"], arcs["Cave des Creux"], arcs["Mur"], arcs["Prameruel"]],
        [arcs["ROC MUGNIER"], arcs["AIGUILLE DU FRUIT"], arcs["GRAVELLES"]],
        "PRAMEUEL"
    ),
    Sommet(
        [arcs["ROC MUGNIER"], arcs["COMBE"], arcs["Pyramide"], arcs["Mont Russes"], arcs["Plan Mugnier"], arcs["Grandes Bosses A"]],
        [arcs["Roc Mugnier"], arcs["PYRAMIDE"], arcs["Grandes Bosses B"]],
        "2"
    ),
    Sommet(
        [arcs["PYRAMIDE"], arcs["Roc Merlet"]],
        [arcs["Plan Mugnier"], arcs["Mont Russes"], arcs["Pyramide"], arcs["ROC MERLET"]],
        "1"
    ),
    Sommet(
        [arcs["CREUX NOIRS"]],
        [arcs["Roches Grises"]],
        "CREUX NOIRS"
    ),
    Sommet(
        [arcs["SAULIRE"]],
        [arcs["Grand Couloir"], arcs["Creux A"], arcs["Combe Saulire A"], arcs["Lac Creux A"]],
        "SAULIRE"
    ),
    Sommet(
        [arcs["MARMOTTES"], arcs["SUISSES"], arcs["VIZELLE"], arcs["Combe Saulire B"]],
        [arcs["Combe Saulire B"], arcs["Combe Pylones"], arcs["m"], arcs["Turcs A"], arcs["Suisses"]],
        "VIZELLE"
    ),
    Sommet(
        [arcs["Combe Pylones"], arcs["Combe Saulire C"], arcs["Grand Couloir"], arcs["Biollay Verdons A"], arcs["m"], arcs["VERDONS"], arcs["SOURCES"]],
        [arcs["VIZELLE"], arcs["SAULIRE"], arcs["Verdons A"], arcs["Renard"], arcs["Biollay Verdons B"]],
        "VERDONS"
    ),
    Sommet(
        [arcs["Combe Saulire B"], arcs["Grand Couloir"], arcs["ROCHER DE L'OMBRE"]],
        [arcs["Stade Descente"], arcs["Combe Saulire C"]],
        "16"
    ),
    Sommet(
        [arcs["Lac Creux A"]],
        [arcs["Lac Creux B"], arcs["CREUX NOIRS"]],
        "10"
    ),
    Sommet(
        [arcs["Turcs A"], arcs["AIGUILLE DU FRUIT"]],
        [arcs["Turcs B"], arcs["Park City"]],
        "9"
    ),
    Sommet(
        [arcs["GRAVELLES"], arcs["Lac Creux B"], arcs["Park City"]],
        [arcs["Cave des Creux"], arcs["Altiport A"]],
        "7"
    ),
    Sommet(
        [arcs["Turcs B"], arcs["Suisses"], arcs["Altiport A"], arcs["Super Pralong"]],
        [arcs["SUISSES"], arcs["Mur"], arcs["Altiport B"]],
        "8"
    ),
    Sommet(
        [arcs["PRALONG"]],
        [arcs["Super Pralong"], arcs["Pralong A"], arcs["Biollay Verdons A"], arcs["Marquetty"], arcs["Biollay"]],
        "11"
    ),
    Sommet(
        [arcs["Pralong A"], arcs["Altiport B"]], # ajouter ALTIPORT
        [arcs["Prameruel"], arcs["Pralong B"], arcs["Altiport C"]],
        "12"
    ),
    Sommet(
        [arcs["JARDIN ALPIN"], arcs["Biollay Verdons B"]],
        [],
        "13"
    ),
    Sommet(
        [arcs["Biollay"], arcs["Altiport C"], arcs["Pralong B"]],
        [arcs["PRALONG"]], # ajouter ALTIPORT
        "PRALONG"
    ),
    Sommet(
        [arcs["COQS"], arcs["CHENUS"], arcs["CRÊTES"], arcs["PRAZ JUGET"], arcs["Col de la Loze"]],
        [arcs["Crêtes A"], arcs["Lanches"], arcs["Chenus"], arcs["Anémones"], arcs["COL DE LA LOZE"], arcs["Lac Bleu"]],
        "CHENUS"
    ),
    Sommet(
        [arcs["COL DE LA LOZE"], arcs["DOU DES LANCHES"]],
        [arcs["Col de la Loze"], arcs["Dou des Lanches"]],
        "COL DE LA LOZE"
    ),
    Sommet(
        [arcs["Crêtes A"], arcs["LOZE"], arcs["PLANTREY"], arcs["BOUC BLANC"]],
        [arcs["Crêtes B"], arcs["Loze Est"], arcs["Loze"], arcs["Dou du Midi"], arcs["Petit Dou"], arcs["Jean Blanc"], arcs["Bouc Blanc A"], arcs["Déviation 1550"]],
        "LOZE"
    ),
    Sommet(
        [arcs["Crêtes B"], arcs["FORET"]],
        [arcs["CRÊTES"], arcs["Arolles A"]],
        "17"
    ),
    Sommet(
        [arcs["Dou des Lanches"], arcs["Bouc Blanc A"], arcs["Arolles A"], arcs["LA TANIA"]],
        [arcs["DOU DES LANCHES"], arcs["PRAZ JUGET"], arcs["Arolles B"], arcs["Bouc Blanc B"], arcs["Plan Fontaine A"], arcs["Jockeys"], arcs["Murettes"]],
        "PRAZ JUGET"
    ),
    Sommet(
        [arcs["Arolles B"], arcs["Bouc Blanc B"], arcs["Plan Fontaine A"], arcs["GROS MURGER"]],
        [arcs["BOUC BLANC"], arcs["Plan Fontaine B"], arcs["Moretta Blanche"], arcs["Folyères"]],
        "15"
    ),
    Sommet(
        [arcs["Folyères"], arcs["Plan Fontaine B"], arcs["Moretta Blanche"]],
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
        [arcs["Déviation 1550"], arcs["Dou du Midi"], arcs["Provères"], arcs["Tovets"]], #arcs["Stade"]
        [arcs["TOVETS"], arcs["GRANGETTES"]],
        "COURCHEVEL - 1550m"
    ),
    Sommet(
        [arcs["Verdons B"], arcs["Anémones"], arcs["Jantzen"], arcs["Loze"], arcs["GRANGETTES"], arcs["TOVETS"], arcs["Petit Dou"]],
        # On considère que seul Verdons relie Lac à ce sommet
        [arcs["JARDIN ALPIN"], arcs["VERDONS"], arcs["LOZE"], arcs["CHENUS"], arcs["Stade"], arcs["Tovets"], arcs["Provères"], arcs["Brigues"], arcs["Amoureux"]],
        "14"
    ),
    Sommet(
        [arcs["Marquetty"], arcs["Renard"], arcs["Verdons A"], arcs["Stade Descente"], arcs["Loze Est"], arcs["Lac Bleu"], arcs["Chenus"]],
        [arcs["BIOLLAY"], arcs["SOURCES"], arcs["ROCHER DE L'OMBRE"], arcs["COQS"], arcs["Verdons B"]],
        "LAC"
    ),
    Sommet(
        [arcs["Piste Bleue"], arcs["Marquis"], arcs["Indiens"], arcs["Belvédère"]],
        [arcs["3 VALLÉES"], arcs["MARQUIS"], arcs["STE AGATHE"], arcs["ARIONDAZ"]],
        "COURCHEVEL - 1650m"
    ),
    Sommet(
        [arcs["Stade"], arcs["Granges"], arcs["Carabosse"], arcs["Praline B"]],
        [arcs["STADE"], arcs["GRANGES"], arcs["Belvédère"]],
        "4"
    ),
    Sommet(
        [arcs["Chapelets"], arcs["Rochers B"], arcs["Bel Air"], arcs["Praline A"]],
        [arcs["Praline B"], arcs["CHAPELETS"]],
        "3"
    ),
    Sommet(
        [arcs["CHAPELETS"], arcs["SIGNAL"]],
        [arcs["Chapelets"], arcs["Rochers A"], arcs["Grandes Bosses A"]],
        "SIGNAL"
    ),
    Sommet(
        [arcs["Rochers A"], arcs["ARIONDAZ"]],
        [arcs["COMBE"], arcs["Rochers B"], arcs["Bel Air"], arcs["Ariondaz"]],
        "BEL AIR"
    ),
    Sommet(
        [arcs["Ariondaz"], arcs["GRANGES"], arcs["MARQUIS"], arcs["3 VALLÉES"], arcs["Grandes Bosses B"]],
        [arcs["SIGNAL"], arcs["Granges"], arcs["Carabosse"], arcs["Praline A"], arcs["PTE BOSSE"], arcs["Indiens"], arcs["Piste Bleue"], arcs["Marquis"]],
        "BOSSES"
    ),
    Sommet(
        [arcs["PTE BOSSE"]],
        [arcs["Gravelles"]],
        "6"
    ),
    Sommet(
        [arcs["STADE"]],
        [arcs["Stade"]],
        "5"
    )
]

sommets_dict = {sommet.nom: sommet for sommet in sommets}
sommets_dict_bas = {tuple(arc.get_nom() for arc in sommet.entrant): sommet for sommet in sommets}
sommets_dict_haut = {tuple(arc.get_nom() for arc in sommet.sortant): sommet for sommet in sommets}

# Dijkstra

def sommets_adjacents(sommet, sommets):
    """
    Retourne la liste des sommets adjacents à un sommet donné.
    :sommet: Sommet pour lequel trouver les sommets adjacents
    :sommets: liste de tous les sommets du graphe
    :return: liste de sommets adjacents
    """
    adjacents = set()
    for arc in sommet.sortant:
        for s in sommets:
            if arc in s.entrant:
                adjacents.add(s)
                break
    return list(adjacents)

def arc_existe(sommet1, sommet2, sommets):
    """
    Vérifie si un arc existe entre deux sommets donnés.
    :sommet1: premier sommet
    :sommet2: deuxième sommet
    :sommets: liste de tous les sommets du graphe
    :return: booléen indiquant si un arc existe entre les deux sommets
    """
    return sommet2 in sommets_adjacents(sommet1, sommets)

def distance_minimale(sommet1, sommet2, sommets, niveau='debutant'):
    """
    Retourne la distance minimale entre deux sommets adjacents.
    :sommet1: premier sommet
    :sommet2: deuxième sommet
    :sommets: liste de tous les sommets du graphe
    :niveau: niveau du skieur ('debutant' ou 'avance')
    :return: distance minimale entre les deux sommets si ils sont adjacents, None sinon
    """
    if not arc_existe(sommet1, sommet2, sommets):
        return None
    distances = []
    chemin = []
    for arc in sommet1.sortant:
        if arc in sommet2.entrant:
            pass
            if hasattr(arc, 'duree'):
                distances.append(arc.duree)
                chemin.append(arc)
            elif niveau == 'debutant' and hasattr(arc, 'duree_1'):
                distances.append(arc.duree_1)
                chemin.append(arc)
            elif niveau == 'avance' and hasattr(arc, 'duree_2'):
                distances.append(arc.duree_2)
                chemin.append(arc)
    return round(min(distances), 2) if distances else None, chemin[distances.index(min(distances))] if distances else None

def dijkstra(s: Sommet, p: Sommet, niveau="debutant", sommets=sommets):
    """
    Algorithme de Dijkstra pour trouver le plus court chemin entre deux sommets.
    :s: sommet de départ
    :p: sommet d'arrivée
    :sommets: liste de tous les sommets du graphe
    :return: None
    """
    # Initialisation
    V = set(sommets)
    T = {s}
    d = {s: 0}
    pere = {s: None}
    
    if s == p:
        raise ValueError("Les sommets de départ et d'arrivée sont les mêmes.")

    for i in sommets:
        if i != s:
            if arc_existe(s, i, sommets):
                d[i] = distance_minimale(s, i, sommets, niveau)[0]
                pere[i] = s
            else:
                d[i] = float('inf')
    # Boucle principale
    while T != V:
        t = min(V - T, key=lambda x: d[x])
        T.add(t)
        for k in sommets_adjacents(t, sommets):
            if k not in T:
                dist = d[t] + distance_minimale(t, k, sommets, niveau)[0]
                if dist < d.get(k, float('inf')):
                    d[k] = dist
                    pere[k] = t
    chemin = [p]
    try:
        while pere[p] is not None:
            chemin.append(pere[p])
            p = pere[p]
        chemin.reverse()
    except:
        raise ValueError("Il n'existe pas de chemin entre les deux sommets.")

    return chemin, d[max(d, key=lambda x: d[x])] #d

def construire_itineraire(chemin, sommets):
    """
    Construit l'itinéraire à suivre à partir du chemin retourné par Dijkstra.
    :chemin: chemin retourné par Dijkstra
    :sommets: liste de tous les sommets du graphe
    :return: itinéraire à suivre
    """
    itineraire = []
    for i in range(len(chemin) - 1):
        print(chemin[i], chemin[i+1])
        print(distance_minimale(chemin[i], chemin[i+1], sommets))
        itineraire.append(distance_minimale(chemin[i], chemin[i+1], sommets))
    return itineraire

# Interface CLI

def CLI():
    print("> Bienvenue sur l'interface de recherche d'itinéraire de la station de ski de Valmorel.")
    print("> Pour quitter, entrez 'q'.")
    while True:
        print("> Veuillez entrer votre niveau de ski (debutant ou avance) :")
        niveau = input("> ")
        if niveau == 'q':
            break
        print("> Veuillez entrer 'haut' si vous êtes en haut d'une piste/remonté, 'bas' sinon (ou ' ' si vous êtes à une station):")
        position = input("> ")
        if position == 'q':
            break
        print("> Veuillez entrer le nom de la piste/remontée ou de la station où vous vous trouvez :")
        depart = input("> ")
        if depart == 'q':
            break
        if position == 'haut':
            for liste in sommets_dict_haut:
                if depart in liste:
                    depart = sommets_dict_haut[liste]
        elif position == 'bas':
            for liste in sommets_dict_bas:
                if depart in liste:
                    depart = sommets_dict_bas[liste]
        else:
            depart = sommets_dict[depart]
        print("> Veuillez entrer 'haut' si vous voulez aller en haut d'une piste/remonté, 'bas' sinon (ou ' ' si vous voulez aller à une station):")
        position = input("> ")
        if position == 'q':
            break
        print("> Veuillez entrer le nom de la piste/remontée ou de la station où vous voulez aller :")
        arrivee = input("> ")
        if arrivee == 'q':
            break
        if position == 'haut':
            for liste in sommets_dict_haut:
                if arrivee in liste:
                    arrivee = sommets_dict_haut[liste]
        elif position == 'bas':
            for liste in sommets_dict_bas:
                if arrivee in liste:
                    arrivee = sommets_dict_bas[liste]
        else:
            arrivee = sommets_dict[arrivee]
        try:
            chemin = dijkstra(depart, arrivee, niveau=niveau, sommets=sommets)
            for i in range(len(chemin[0]) - 1):
                x = distance_minimale(chemin[0][i], chemin[0][i+1], sommets)[1]
                if x.nature == 'piste verte' or x.nature == 'piste bleue' or x.nature == 'piste rouge' or x.nature == 'piste noire' or x.nature == 'télécabine':
                    print(f"   {i}. Emprunter la {x.nature} {x.nom}")
                else:
                    print(f"   {i}. Emprunter le {x.nature}  {x.nom}")
            print(f"> Temps : {round(chemin[1])} minutes")
        except:
            print("> Il n'existe pas de chemin entre les deux sommets.")

