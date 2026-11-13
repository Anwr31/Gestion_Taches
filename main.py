
taches = []

while True:
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tâche : ").strip()

        if titre == "":
            print("Erreur : le titre ne peut pas être vide.")
        else:
            taches.append(titre)
            print("Tâche ajoutée avec succès.")

    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tâche pour le moment.")
        else:
            print("\n=== LISTE DES TÂCHES ===")
            for i, tache in enumerate(taches, start=1):
                print(f"{i}. {tache}")

    elif choix == "3":
        mot_cle = input("Entrez un mot-clé : ").strip().lower()

        trouve = False

        for i, tache in enumerate(taches, start=1):
            if mot_cle in tache.lower():
                print(f"{i}. {tache}")
                trouve = True

        if not trouve:
            print("Aucune tâche correspondante trouvée.")

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Erreur : choix invalide. Veuillez réessayer.")
