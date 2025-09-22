inventaire={'Dune': 15, '1984': 5, 'Fondation': 3}

#fonction qui affiche le menu d'inventaire
def afficher_menu():
    print("<<Bienvenue sur le programme>>")
    print("*Menu inventaire")
    print("1. Voir tout l'inventaire")
    print("2. Ajouter un article")
    print("3. Supprimer un article")
    print("4. Modifier un article")
    print("5. Chercher un article")
    print("6. Stock inferieur à un seuil")
    print("7. quitter")
    print("")

#fonction aide pour vérifier les entrées pour les fonctions suivantes
def valider_quantite(quantite):
    while True:
        new_quantite=input(quantite)
        if new_quantite.isdigit() and int(new_quantite)>0 and new_quantite!='':
           return int(new_quantite)
        else:
             print("quantite entrée non valide. Entrer une quantité valide")


#permettre d'afficher tout l'inventaire d'une maniere lisible
def voir_inventaire():
    if not inventaire:
        print("inventaire vide")
    print(f"voici l'inventaire courant".upper())
    print("_" * 35)
    print(f"{'Article':<20} | {'stock':>5}")
    print("_"*35)
    for key,value in inventaire.items():
        print(f"{key:<20} | {value:>5}")
    print("_" * 35)

#Fonction pour rechercher un article par son nom et afficher son stock
def  rechercher_article():
   while True:
     article=input("Entrer le nom d'article:")
     if article in inventaire:
        print("_" * 30)
        print(f"{'Article':<20}|{'quantite':<5}")
        print("_"*30)
        print(f"{article:<20} | {inventaire[article]:>5}")
        print("_"*30)
        break
     else:
         print("Article n'existe pas.")


   ''' cette fonction permettre d'ajouter un article à l'inventaire
   en saisissant son nom avec son stock tout en vérifiant les champ d'entee
   de stock avec la fonction valider_quantite()'''
def ajouter_article():
    print("Ajouter un article")
    while True:
        article=input("Entrer le nom d'article:")
        new_article=article.replace(" ","")
        if new_article=="":
           print("Le champ entrée est vide, entrer le nom d'article ")
        else:
          break
    if new_article in inventaire:
        print("article deja exist.")
    else:
        quantite=valider_quantite(f"Entrer une quantite pour {new_article}:")
        inventaire[new_article]=quantite
        print("article ajouté")

'''la fonction suivante permet à l'utilisateur 
   de supprimer un article avec son stock de l'invenatire'''
def supprimer_article():
    print("*supprimer un article*")
    while True:
        article=input("Entrer le nom d'article:")
        if article in inventaire:
            del inventaire[article]
            print(f"l'article {article} est supprimé")
            break
        else:
            print("article non existant. Entrer un nom article existant")


#la foncion modifier_article() permet de modifier le stock d'un article
def modifier_article():
  print("*Modifier un article*")
  while True:
    article=input("Entrer le nom d'article:")
    if article in inventaire:
        new_quantite=valider_quantite(f"Entrer la nouvelle quantite pour {article}:")
        inventaire[article]=new_quantite
        print(f"stock d'article {article} a été modifié")
        break
    else:
        print("article non existant. Entrer un nom article existant")

#La fonction modifier_article() a pour but de mettre à jour la quantité en stock d'un article
def voir_stock_faible():
    print("voir le stock inférieur à un seuil*")
    seuil=valider_quantite(f"Entrer une quantite seuil :")

    articles_faibles = {k: v for k, v in inventaire.items() if v < seuil}
    if not articles_faibles:
         print(f"Aucun article avec un stock inférieur à {seuil}")
         return
    print(f"Articles avec stock inférieur à {seuil}:")
    print(f"{'Article':<20} | {'Stock':>5}")
    print("-" * 33)
    for k, v in articles_faibles.items():
            print(f"{k:<20} | {v:>5}")



def main():

    while True:
        afficher_menu()
        choice=input("Entrer un choix :")
        if choice=="1":
            voir_inventaire()
        if choice=="2":
            ajouter_article()
        if choice=="3":
            supprimer_article()
        if choice=="4":
            modifier_article()
        if choice=="5":
            rechercher_article()
        if choice=="6":
            voir_stock_faible()
        if choice=="7":
            break

if _name=="main_":
    main()