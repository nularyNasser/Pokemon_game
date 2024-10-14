import json
from Player import Player
from Pokemon import Pokemon


choix_pokemon: int = -1

#------------CREATION DES OBJETS------------
joueur = Player("Sasha")
pikachu = Pokemon("Pikachu", "Électrique", 1)
drakofeu = Pokemon("Drakofeu", "Feu", 1)
carapuce = Pokemon("Carapuce", "Eau", 1)
roucoups = Pokemon("Roucoups", "Vent", 1)
#-------------------------------------------

# Faire un dialogue qui demande au joueur de chosir son pseudo.
with open('dialog.json', 'r', encoding='utf-8') as dialog_file: # name / dialog
    dialog = json.load(dialog_file) # fichier dialog.json charger en mode read


def dialogue_debut():
    for i in dialog["chen"]: # Parcour du dialog de chen
        if i == "choix":
            print("Choisir un numéro pour choisir: ")
            for pokemon in dialog["chen"][i]:
                print(pokemon) # Affichage des 3 pokemon
            choix = int(input("Numero : "))
            while choix < 0 or choix > 3:
                choix = int(input("Numero : "))
            if choix == 1:
                joueur.add_in_pokedex(pikachu)
            elif choix == 2:
                joueur.add_in_pokedex(drakofeu)
            elif choix == 3:
                joueur.add_in_pokedex(carapuce)
            elif choix == 4:
                joueur.add_in_pokedex(roucoups)
        else:
            print(dialog["chen"][i])
            input()


dialogue_debut()

# Commencer le jeu.

# Demander au joueur ou il veut aller
def dialogue_change_place():
    for i in dialog["game_dialog"]: # Parcour du dialog de chen
        if i == "choix":
            print("Choisir un numéro pour choisir: ")
            for pokemon in dialog["game_dialog"][i]:
                print(pokemon) # Affichage des 3 pokemon
            choix = int(input("Numero : "))
            while choix < 0 or choix > 3:
                choix = int(input("Numero : "))
#            if choix == 1:
#                joueur.add_in_pokedex(pikachu)
#            elif choix == 2:
#                joueur.add_in_pokedex(drakofeu)
#            elif choix == 3:
#                joueur.add_in_pokedex(carapuce)
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