import json
from Player import Player
from Pokemon import Pokemon


choix_pokemon: int = -1

#------------CREATION DES OBJETS------------
joueur = Player("Sasha")
pikachu = Pokemon("Pikachu", "Électrique", 1)
drakofeu = Pokemon("Drakofeu", "Feu", 1)
carapuce = Pokemon("Carapuce", "Eau", 1)
#-------------------------------------------

# Faire un dialogue qui demande au joueur de chosir son pseudo.
with open('dialog.json', 'r', encoding='utf-8') as dialog_file: # name / dialog
    dialog = json.load(dialog_file) # fichier dialog.json charger en mode read


def dialogue_debut():
    for i in dialog["chen"]: # Parcour du dialog de chen
        if i == "choix":
            dialogue_choix(i, "chen")
        else:
            print(dialog["chen"][i])
            input()


def dialogue_choix(i: int, who: str):
    print("Choisir un numéro pour choisir: ")
    for pokemon in dialog[who][i]:
        print(pokemon) # Affichage des 3 pokemon
    choix_pokemon = int(input("Numero : "))
    while choix_pokemon < 0 or choix_pokemon > 3:
        choix_pokemon = int(input("Numero : "))
    if choix_pokemon == 1:
        joueur.add_in_pokedex(pikachu)
    elif choix_pokemon == 2:
        joueur.add_in_pokedex(drakofeu)
    else:
        joueur.add_in_pokedex(carapuce)


dialogue_debut()

# Commencer le jeu.

# Demander au joueur ou il veut aller
def dialogue_change_place():
    for i in dialog["game_dialog"]:
        if i == "choix":
            dialogue_choix(i, "game_dialog")
        else:
            print(dialog["game_dialog"][i])
            input()


def change_place():
    global place # Variable global car la fonction n'a pas accée à la variable place
    while place != 'm':
        place = input("Tapez 'm' pour vous déplacer: ")
    return True


place = input("Tapez 'm' pour vous déplacer: ")
can_change_place = change_place()

if can_change_place:
    dialogue_change_place()