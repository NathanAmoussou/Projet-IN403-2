from main import *
from tkinter import *
from PIL import Image, ImageTk
 
root = Tk()
root.title('Station de ski')
root.geometry('1400x700')

# Ouverture de l'image
image = Image.open('plan_pistes_courchevel_sommets.jpg')

# Redimensionnement de l'image
width, height = image.size
ratio = 0.5 # le ratio de redimensionnement souhaité
image = image.resize((int(width*ratio), int(height*ratio)))

# Affichage de l'image dans un Label
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.pack(side=LEFT)

# Ajout de deux boutons avec du texte au-dessus de l'image
frame_boutons = Frame(root)
frame_boutons.pack(side=TOP)

label_niveau = Label(frame_boutons, text='Niveau du skieur :')
label_niveau.pack(side=LEFT, padx=5)

niveau = StringVar() # variable pour stocker le niveau sélectionné

def set_niveau(n):
    niveau.set(n)

# Fonction pour changer la couleur du bouton
def changer_couleur_bouton():
    if niveau.get() == 'debutant':
        button_debutant.config(bg='green') # Met le fond en vert
        button_avance.config(bg='SystemButtonFace') # Remet le fond par défaut
    elif niveau.get() == 'avance':
        button_avance.config(bg='green') # Met le fond en vert
        button_debutant.config(bg='SystemButtonFace') # Remet le fond par défaut

button_debutant = Button(frame_boutons, text='debutant', command=lambda: [set_niveau('debutant'), changer_couleur_bouton()])
button_debutant.pack(side=LEFT, padx=5)

button_avance = Button(frame_boutons, text='avance', command=lambda: [set_niveau('avance'), changer_couleur_bouton()])
button_avance.pack(side=LEFT, padx=5)


# Ajout des 3 entrées à droite de l'image
frame_entries = Frame(root)
frame_entries.pack(padx=10, pady=10)

label_ou_etes_vous = Label(frame_entries, text="Où êtes-vous ?(En haut ou en bas d'une piste ?)")
label_ou_etes_vous.pack()

entry_emplacement = Entry(frame_entries)
entry_emplacement.pack(padx=5, pady=5)

label_nom_piste = Label(frame_entries, text='Veuillez entrer le nom de la piste')
label_nom_piste.pack(pady=5)

entry_nom_piste = Entry(frame_entries)
entry_nom_piste.pack(padx=5, pady=5)

label_ou_souhaitez_vous_aller = Label(frame_entries, text='Où souhaitez-vous aller ?')
label_ou_souhaitez_vous_aller.pack(pady=5)

entry_destination = Entry(frame_entries)
entry_destination.pack(padx=5, pady=5)

# Fonction appelée par le bouton "Start"
def afficher_resultat():
    emplacement = entry_emplacement.get()
    nom_piste = entry_nom_piste.get()
    destination = entry_destination.get()
    niveau_selectionne = niveau.get() # on récupère le niveau sélectionné
    
    resultat = f"Vous êtes actuellement {emplacement} sur la piste {nom_piste} et vous souhaitez aller à {destination}. Niveau : {niveau_selectionne}."
    
    # Création d'un Label pour afficher le résultat
    label_resultat = Label(frame_entries, text=resultat)
    label_resultat.pack(pady=5)
    
    # Création du bouton "Itinéraire"
    button_itineraire = Button(frame_entries, text='Itinéraire', command=Itineraire)
    button_itineraire.pack(pady=5)
    

    itineraire = []
    for i in range(len(chemin) - 1):
        print(chemin[i], chemin[i+1])
        print(distance_minimale(chemin[i], chemin[i+1], sommets))
        itineraire.append(distance_minimale(chemin[i], chemin[i+1], sommets))
    return itineraire

    # Création d'un Label pour afficher le résultat
    label_itineraire = Label(frame_entries, text=itineraire)
    label_itineraire.pack(pady=6)


# Ajout du bouton "Start"
button_start = Button(frame_entries, text='Start', command=afficher_resultat)
button_start.pack(pady=5)



def Itineraire():
    niveau = StringVar()
    
    emplacement = entry_emplacement.get()
    nom_piste = entry_nom_piste.get()
    destination = entry_destination.get()
    niveau_selectionne = niveau.get()

    while True:
        niveau = niveau_selectionne
        position = emplacement
        depart = nom_piste

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
        
        position = emplacement
        arrivee = destination
        
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
            
            chemin = dijkstra(depart, arrivee, niveau, sommets=sommets)

            for i in range(len(chemin[0]) - 1):
                x = distance_minimale(chemin[0][i], chemin[0][i+1], sommets)[1]
                if x.nature == 'piste verte' or x.nature == 'piste bleue' or x.nature == 'piste rouge' or x.nature == 'piste noire' or x.nature == 'télécabine':
                    print(f"   {i}. Emprunter la {x.nature} {x.nom}")
                else:
                    print(f"   {i}. Emprunter le {x.nature}  {x.nom}")
            print(f"> Temps : {round(chemin[1])} minutes")
        except:
            print("> Il n'existe pas de chemin entre les deux sommets.")




root.mainloop()
