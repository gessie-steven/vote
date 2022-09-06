#KOUDISSA GESSIE STEVEN EXAUCE

def jeu():

    print("Bienvenu dans jeu ! La partie peut commencer\n")

    nombre_points = 50
    Liste1 = []
    while nombre_points > 0:
    #Saisie de l'utilisateur
        N = int(input("Entrez les joueurs : "))
    #N c'est le nombre des joueurs
    print("Donnez le nom des  joueurs :")
    J1 = input(" Joueur 1 :")
    J2 = input(" Joueur 2 :")
    
    for j in range(50):
        #champ de jeu
        print(f"il vous reste{j - 1} points !!!! ")
        val = int(input(f"Veuillez taper 1 pour voter {J1} ou 2 pour voter {J2}: "))
        Liste1.append(val)
    #le compteur prendra uniquement en charge le nombre de 1 et 2 saisi afin de donner le résultat
    cpt1 = Liste1.count(1)
    cpt2 = Liste1.count(2)
    print(cpt1, cpt2)
    # Vérification de la correspondance entre les compteurs
    if cpt1 > cpt2:
        print(f"Le gagnant est {J1} avec {cpt1} votants sur {cpt2} pour {J2}.")
    elif cpt1 < cpt2:
        print(f"Le gagnant est {J2} avec {cpt2} votants sur {cpt1} pour {J1}.")
    else:
        print("Fin du jeu !!!! ")
jeu() 