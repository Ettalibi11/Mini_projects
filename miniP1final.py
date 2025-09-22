commande_client = [
    {'nom': 'Latte', 'prix': 4.25, 'quantite': 2},
    {'nom': 'Muffin', 'prix': 3.25, 'quantite': 1}
]

def generer_recu(liste_commande, taux_taxe, code_reduction=None):
    new = []
    total_cmd = 0  # Total avant réduction

    for item in liste_commande:
        nom = item['nom']
        prix = item['prix']
        quantite = item['quantite']
        total_article = prix * quantite
        total_cmd += total_article
        # Format : nom gauche (10), x quantité (3), prix droit (7)
        new.append(f"{nom:<10} x {quantite:<2}  {total_article:>7.2f}€")

    montant_reduction = 0
    reduction = ""

    if code_reduction == 'SAVE10':
        montant_reduction = total_cmd * 0.10
        reduction = "(10%)"
    elif code_reduction == '5OFF':
        montant_reduction = total_cmd * 0.05
        reduction = "(5%)"

    total_apres_reduc = total_cmd - montant_reduction
    taxe = total_apres_reduc * taux_taxe
    grand_total = total_apres_reduc + taxe
    points_fidelite = int(grand_total // 5)

    # Affichage
    print("==== Reçu du Café ====")
    for ligne in new:
        print(ligne)
    print("-" * 30)

    print(f"Sous-total:         {total_cmd:>8.2f}€")
    if montant_reduction > 0:
        print(f"Réduction {reduction}:   {-montant_reduction:>8.2f}€")
    print(f"Taxe ({taux_taxe:.0%}):     {taxe:>12.2f}€")
    print(f"Total:              {grand_total:>8.2f}€")

    print("=" * 30)
    print(f"Points de fidélité gagnés: {points_fidelite}")
    print("---")

    return grand_total

generer_recu(commande_client, 0.07, code_reduction='SAVE10')