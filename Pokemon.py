class Pokemon:

    def __init__(self, name: str, type_pokemon: str, niveau: int) -> None:
        self.name = name
        self.type_pokemon = type_pokemon
        self.niveau = niveau
        self.info = {'name' : self.name,
                        'type' : self.type_pokemon,
                        'niveau': self.niveau}
    
    def get_info(self):
        print("Nom:", self.info['name'], "/ Type:", self.info['type'], "/ Niveau:", self.info['niveau'])


if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "Electrique", 5)
    pikachu.get_info()