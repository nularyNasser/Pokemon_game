import json
from Player import Player
from Pokemon import Pokemon


pseudo: str = input("Comment vous appellez-vous: ")
choix_pokemon: int = -1

#------------CREATION DES OBJETS------------
joueur = Player(pseudo)
pikachu = Pokemon("Pikachu", "Électrique", 1)
drakofeu = Pokemon("Drakofeu", "Feu", 1)
carapuce = Pokemon("Carapuce", "Eau", 1)
#-------------------------------------------

# Faire un dialogue qui demande au joueur de chosir son pseudo.
with open('Pokemon_game/dialog.json', 'r', encoding='utf-8') as dialog_file: # name / dialog
    dialog = json.load(dialog_file) # fichier dialog.json charger en mode read

for i in dialog["chen"]["dialog"]: # Parcour du dialog de chen
    if i == "choix":
        print("Choisir un numéro pour choisir un pokémon: ")
        for pokemon in dialog["chen"]["dialog"][i]:
            print(pokemon) # Affichage des 3 pokemon
        choix_pokemon = int(input("Pokemon numero : "))
        while choix_pokemon < 0 or choix_pokemon > 3:
            choix_pokemon = int(input("Pokemon numero : "))
        if choix_pokemon == 1:
            joueur.add_in_pokedex(pikachu)
        elif choix_pokemon == 2:
            joueur.add_in_pokedex(drakofeu)
        else:
            joueur.add_in_pokedex(carapuce)
    else:
        print(dialog["chen"]["dialog"][i])
        input()

# Commencer le jeu.
