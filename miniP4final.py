def analyser_fichier_log(fichier_log):

    comptes_niveaux = {}
    comptes_horaires = {}
    erreurs_uniques = set()

    ''''on supprime les  caracetre spéciaux par strip() get 
    on divise le text en des lignes avec splitlines()'''
    logs = fichier_log.strip().splitlines()

    '''dans cette boucle on va analyser chaque ligne de logs, extraire
       l'ensemble des événements, le nombre des événements pour chaque heure'''
    for ligne in logs:
        ligne = ligne.strip()
        if not ligne:
            continue
        divis = ligne.split(' - ', 1)

        if len(divis) < 2:
            print(f"Attention: Ignorons la ligne de journal mal formée (séparateur ' - ' manquant) : {ligne}")
            continue
        chaine = divis[0]
        message = divis[1]

        #parties_chaines liste contenant les éléments de la premiere partie
        parties_chaine = chaine.split(' ')
        #print("$$$$$les parties chaines$$$$$$$$\n", parties_chaine)

        if len(parties_chaine) < 3:
            print(f"Attention: vous avez ignorez une parte de la chaine : {ligne}")
            continue
        heure = parties_chaine[1]
        niveau = parties_chaine[2]

        heure_exacte = heure[0:2]
        niveau_net = niveau[1:-1]

        comptes_niveaux[niveau_net] = comptes_niveaux.get(niveau_net, 0) + 1
        comptes_horaires[heure_exacte] = comptes_horaires.get(heure_exacte, 0)+1
        print( "compte_niveaux", comptes_niveaux)
        print("compte_horaire", comptes_horaires)
        if niveau_net == 'ERROR':
            erreurs_uniques.add(message)

    return {
        'comptes_niveaux': comptes_niveaux,
        'comptes_horaires': comptes_horaires,
        'erreurs_uniques': erreurs_uniques
    }


log_data = """
2025-09-18 09:15:23 [INFO] -  L'utilisateur 'admin' s'est connecté .
2025-09-18 09:22:41 [ERROR] - Échec de la connexion à la base de données.
2025-09-18 09:23:15 [WARNING] - Le temps de réponse du disque est élevé.
2025-09-18 10:05:00 [INFO] - Sauvegarde nocturne terminée.
2025-09-18 10:11:34 [ERROR] - Expiration de l'authentification de l'utilisateur.
"""

resultats_analyse = analyser_fichier_log(log_data)

print("===== Rapport d'analyse de log Complet =====")

print("\n--- Comptes par Niveau de Log ---")
for niveau, compte in resultats_analyse['comptes_niveaux'].items():
    print(f"{niveau}: {compte}")

print("\n--- Événements par heure ---")
for heure, compte in sorted(resultats_analyse['comptes_horaires'].items()):
    print(f"Heure {heure}: {compte} événements")

print("\n--- Messages d'erreur uniques ---")
for message_erreur in resultats_analyse['erreurs_uniques']:
    print(f"- {message_erreur}")

print("====================================")