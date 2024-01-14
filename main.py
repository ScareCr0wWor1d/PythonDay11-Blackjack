# Day 11 BlackJack

import random
from os import system
from art import logo


def donne_carte():
    """Fonction pour donner une carte"""
    paquet = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #paquet = [11, 10]
    carte = random.choice(paquet)
    return carte


def affiche_carte(qty):
    print(f"Les cartes du joueur : {joueur} pour un total de {sum(joueur)}")
    if qty == 2:
        print(f"Les cartes du CPU : {cpu} pour un total de {sum(cpu)}")
    else:
        print(f"La carte du CPU est : {cpu[0]}")


def calcule_total(carte):
    """Calcule le total des cartes"""
    if sum(carte) == 21 and len(carte) == 2:
        return 0
    return sum(carte)

def swapace(cartes):
    cartes.remove(11)
    cartes.append(1)
    return cartes

end_of_game = False
cpu = []
joueur = []

print(logo)

while not end_of_game:
    #Donne des cartes
    for _ in range(2):
        joueur.append(donne_carte())
        cpu.append(donne_carte())

    #Check si Blackjack
    if calcule_total(joueur) > 21:
        swapace(joueur)
    if calcule_total(cpu) > 21:
        swapace(cpu)
    total_joueur = calcule_total(joueur)
    total_cpu = calcule_total(cpu)
    affiche_carte(1)

    #check si le joueur veut d'autres cartes
    if total_joueur != 0:
        while input("voulez-vous obtenir une nouvelle carte (o/n)? ") == 'o':
            system('cls')
            print(logo)
            joueur.append(donne_carte())
            if calcule_total(joueur) > 21 and 11 in joueur:
                joueur = swapace(joueur)
            affiche_carte(1)
            if calcule_total(joueur) > 21:
                end_of_game = True
                break

    #Ajuste deck cpu if < 17
    if calcule_total(cpu) != 0:
        while sum(cpu) < 17 and not end_of_game and calcule_total(cpu) != 0:
            cpu.append(donne_carte())
            if calcule_total(cpu) > 21 and 11 in cpu:
                cpu = swapace(cpu)
            if sum(cpu) > 21:
                end_of_game = True

    total_cpu = calcule_total(cpu)
    total_joueur = calcule_total(joueur)
    system('cls')
    print(logo)
    affiche_carte(2)

    if total_joueur == total_cpu:
        print("Partie nulle")
    elif total_joueur == 0:
        print("Joueur a BLACKJACK et gagne!")
    elif total_cpu == 0:
        print("CPU a BLACKJACK et gagne!")
    elif total_joueur > 21:
        print("Joueur BUST, CPU Gagne")
    elif total_cpu > 21:
        print("CPU BUST, joueur Gagne")
    elif sum(joueur) > sum(cpu):
        print("Joueur gagne!")
    else:
        print("CPU gagne!")

    if input("Voulez-vous rejouer (o/n)? ") == 'n':
        end_of_game = True
    else:
        joueur = []
        cpu = []
        end_of_game = False
        system('cls')
        print(logo)
