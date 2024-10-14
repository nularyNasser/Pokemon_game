from Pokemon import Pokemon

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.pokedex = {} # Vide de base
    
    def info_pokedex(self): # info_pokedex()
        cpt: int = 1
        for pokemon in self.pokedex:
            print(cpt, pokemon)
            cpt += 1
    
    def add_in_pokedex(self, object): # add_in_pokedex()
        self.pokedex[object.name] = object


if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "Electrique", 5)
    ratata = Pokemon("Ratata", "Je ne sais pas", 2)
    nasser = Player("Nasser")
    nasser.add_in_pokedex(pikachu)
    nasser.add_in_pokedex(ratata)
    nasser.info_pokedex()
    pikachu.get_info()