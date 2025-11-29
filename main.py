import json

#création d'une liste de cadeau vide

liste_cadeaux = []

#creation de la fonction pour ajouter des cadeaux dans la liste

def ajout_cadeaux():
    global liste_cadeaux
    ajout = True
    while ajout:
        nom_cadeau = input('Quelle cadeaux voulez-vous ?\n')
        prix = input('quel est son prix ?\n')
        description = input('Quelle est sa description ?\n')

        nombre_cadeaux = len(liste_cadeaux)+1

        liste_cadeaux.insert((int(nombre_cadeaux)), {nombre_cadeaux:{"Nom": nom_cadeau, "Prix": prix,"Description": description}})

        liste_continue = input("Voulez-vous continuez ? oui/non \n")
        if not liste_continue == "oui":
            ajout = False
            utilisateur_choix()
        
#fonction pour modifer un cadeau de la liste
def modifier_cadeau():
    global liste_cadeaux
    print(liste_cadeaux)
    modif_cadeaux = input("Quel cadeaux souhaitez-vous modifier ?")
    print(modif_cadeaux)
    print(f"vous allez modifier ce cadeau de la liste : \n {liste_cadeaux[(int(modif_cadeaux)-1)]}")
    nom_cadeau = input('Nouveau nom du cadeau : \n')
    prix = input("Nouveau prix : \n")
    description = input("Nouvelle description :\n")
    liste_cadeaux[(int(modif_cadeaux)-1)] = ( {int(modif_cadeaux):{"Nom": nom_cadeau, "Prix": float(prix),"Description": description}})


#fonction pour supprimer un cadeau de la liste
def suppression_cadeaux():
    global liste_cadeaux
    print(liste_cadeaux, "\n")
    choix_suppression = input("Quelle cadeaux voulez-vous supprimer de la liste ?\n")
    del liste_cadeaux[(int(choix_suppression)-1)]
    print(f"le cadeau {choix_suppression} a été supprimé.")
    print(liste_cadeaux)
    utilisateur_choix()


#fonction pour lire la liste de cadeaux
def lecture_cadeaux():
    global liste_cadeaux
    print((liste_cadeaux))



#fonction pour sauvegarder la liste sous un fichier JSON
def sauvegarde_liste():
    global liste_cadeaux
    with open ("projet_1/listedecadeaux.json", "w", encoding="utf-8") as f:
        json.dump(liste_cadeaux, f, indent=4, ensure_ascii=False)
    print("La liste est sauvegardée.")


#fonction pour charger une liste déjà existante
def chargement_liste():
    global liste_cadeaux
    try:
        with open("projet_1/listedecadeaux.json", "r") as f:
            liste_cadeaux = json.load(f)
            print(liste_cadeaux)
        print("La liste à été chargé avec succès.")
    except(FileNotFoundError, json.JSONDecodeError):
        return []


#fonction pour enregistrer le choix utilisateur
def utilisateur_choix():    
    choix_utilisateur = input("Que voulez vous faire ? \n 1-Ajout de cadeaux \n 2-Modifier un cadeau \n 3-Suppression de cadeaux \n 4-lire la liste de cadeaux\n 5-Sauvegarder la liste\n 6-Charger la liste\n 7-Quitter\n")
    if choix_utilisateur == "1":
        ajout_cadeaux()
    if choix_utilisateur =="2":
        modifier_cadeau()
    if choix_utilisateur == "3":
        suppression_cadeaux()
    if choix_utilisateur == "4":
        lecture_cadeaux()
    if choix_utilisateur =="5":
        sauvegarde_liste()
    if choix_utilisateur =="6":
        chargement_liste()
    if choix_utilisateur == "7":
        #appel la fonction pour quitter l'application
        quit()
    else:
        utilisateur_choix()

#appel la fonction pour le choix de l'utilisateur, démarre l'application
utilisateur_choix()
