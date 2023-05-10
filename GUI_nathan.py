from main import *
import tkinter as tk # interface graphique
from PIL import Image, ImageTk # affichage de l'image

# Interface graphique

class GUI(tk.Tk):
    def __init__(self):
        """
        Initialise la fenêtre principale.
        """
        super().__init__()
        self.title("Itinéraire de la station de ski de Courchevel")
        self.geometry("1100x700")
        self.resizable(width=False, height=False)
    
        # Définition des constantes
        image_station = Image.open("/Users/nathan/Desktop/IN408 - Projet pistes de ski/Projet-IN403/plan_pistes_courchevel.jpg")
        image_station.putalpha(128)
        self.image_tk = ImageTk.PhotoImage(image_station)
        self.coordonnees_sommets = {'CHANROSSA': (104, 124),
                                    'CREUX': (246, 194),
                                    'PRAMEUEL': (238, 303),
                                    '2': (125, 263),
                                    '1': (53, 164),
                                    'CREUX NOIRS': (0, 0),
                                    'SAULIRE': (0, 0),
                                    'VIZELLE': (0, 0),
                                    'VERDONS': (0, 0),
                                    '16': (0, 0),
                                    '10': (0, 0),
                                    '9': (0, 0),
                                    '7': (0, 0),
                                    '8': (0, 0),
                                    '11': (0, 0),
                                    '12': (0, 0),
                                    '13': (0, 0),
                                    'PRALONG': (0, 0),
                                    'CHENUS': (0, 0),
                                    'COL DE LA LOZE': (0, 0),
                                    'LOZE': (0, 0),
                                    '17': (0, 0),
                                    'PRAZ JUGET': (0, 0),
                                    '15': (0, 0),
                                    'LA TANIA': (0, 0),
                                    'COURCHEVEL - LE PRAZ - 1300m': (0, 0),
                                    'ST BON - 1100m': (0, 0),
                                    'COURCHEVEL - 1550m': (0, 0),
                                    '14': (0, 0),
                                    'LAC': (0, 0),
                                    'COURCHEVEL - 1650m': (0, 0),
                                    '4': (0, 0),
                                    '3': (0, 0),
                                    'SIGNAL': (0, 0),
                                    'BEL AIR': (0, 0),
                                    'BOSSES': (0, 0),
                                    '6': (0, 0),
                                    '5': (0, 0)}
        print(self.coordonnees_sommets)
        
        # Création des fonctions
        def debutant(self):
            pass

        def avance(self):
            pass

        def debut(self):
            pass

        def fin(self):
            pass

        # Création des widgets
        self.label_niveau = tk.Label(self, text="Niveau du skieur :")
        self.label_niveau.config(font=("Courier", 13))
        self.bouton_debutant = tk.Button(self, text="Débutant", command=debutant)
        self.bouton_debutant.config(font=("Courier", 13))
        self.bouton_avance = tk.Button(self, text="Avancé", command=avance)
        self.bouton_avance.config(font=("Courier", 13))
        self.canevas = tk.Canvas(self, width=220*4-10, height=70*9-10)
        self.bouton_debut = tk.Button(self, text="Début", command=debut)
        self.bouton_debut.config(font=("Courier", 13))
        self.bouton_fin = tk.Button(self, text="Fin", command=fin)
        self.bouton_fin.config(font=("Courier", 13))

        for sommet in sommets_dict:
            pass

        # Placement des widgets
        self.label_niveau.place(x=220/2, y=70/2, width=220-10, height=70-10, anchor="center")
        self.bouton_debutant.place(x=220+220/4, y=70/2, width=220/2-10, height=70-10, anchor="center")
        self.bouton_avance.place(x=220+220/4*3, y=70/2, width=220/2-10, height=70-10, anchor="center")
        self.canevas.place(x=220*4/2, y=70+70*9/2, width=220*4-10, height=70*9-10, anchor="center")
        self.canevas.create_image(220*4/2-5,70*9/2, anchor="center", image=self.image_tk)
        self.bouton_debut.place(x=220*4+220/4, y=70+70/2, width=220/2-10, height=70-10, anchor="center")
        self.bouton_fin.place(x=220*4+220/4*3, y=70+70/2, width=220/2-10, height=70-10, anchor="center")

interface_graphique = GUI()
interface_graphique.mainloop()