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

button_debutant = Button(frame_boutons, text='Débutant')
button_debutant.pack(side=LEFT, padx=5)

button_avance = Button(frame_boutons, text='Avancé')
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
    
    resultat = f"Vous êtes actuellement {emplacement} sur la piste {nom_piste} et vous souhaitez aller à {destination}."
    
    # Création d'un Label pour afficher le résultat
    label_resultat = Label(frame_entries, text=resultat)
    label_resultat.pack(pady=5)
    
    # Création du bouton "Itinéraire"
    button_itineraire = Button(frame_entries, text='Itinéraire')
    button_itineraire.pack(pady=5)

# Ajout du bouton "Start"
button_start = Button(frame_entries, text='Start', command=afficher_resultat)
button_start.pack(pady=5)

root.mainloop()