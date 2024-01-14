# Day 11 BlackJack

import random
from os import system
from art import logo


def donne_carte():
    """Fonction pour donner une carte"""
    paquet = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carte = random.choice(paquet)
    return carte


def affiche_carte(qty):
    print(f"Les cartes du joueur : {joueur} pour un total de {sum(joueur)}")
    if qty == 2:
        print(f"Les cartes du CPU : {cpu} pour un total de {sum(cpu)}")
    else:
        print(f"La carte du CPU est : {cpu[0]}")


def calcule_total(carte):
    if sum(carte) == 21 and len(carte) == 2:
        return 0
    if 11 in carte and sum(carte) > 21:
        carte.remove(11)
        carte.append(1)
    return sum(carte)


end_of_game = False
cpu = []
joueur = []

print(logo)

while not end_of_game:
    for _ in range(2):
        joueur.append(donne_carte())
        cpu.append(donne_carte())
    total_joueur = calcule_total(joueur)
    total_cpu = calcule_total(cpu)
    affiche_carte(1)
    while input("voulez-vous obtenir une nouvelle carte (o/n)? ") == 'o':
        system('cls')
        print(logo)
        joueur.append(donne_carte())
        affiche_carte(1)
        if sum(joueur) > 21:
            end_of_game = True
            break
    while sum(cpu) < 17 and not end_of_game:
        cpu.append(donne_carte())
        if sum(cpu) > 21:
            end_of_game = True
    system('cls')
    print(logo)
    affiche_carte(2)
    if end_of_game and sum(cpu) > 21:
        print("Vous avez gagné! CPU Busted!")
    elif end_of_game and sum(joueur) > 21:
        print("CPU a gagné! Joueur Busted!")
    elif sum(joueur) == sum(cpu):
        print("Partie nulle")
    elif sum(joueur) > sum(cpu):
        print("Vous avez gagner!")
    else:
        print("CPU a gagné!")

    if input("Voulez-vous rejouer (o/n)? ") == 'n':
        end_of_game = True
    else:
        joueur = []
        cpu = []
        end_of_game = False
        system('cls')
        print(logo)
