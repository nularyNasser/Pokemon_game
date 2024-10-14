class House:

    def __init__(self, nb_etages: int) -> None:
        self.nb_etage = nb_etages
        self.etage_min = 0
        self.etage_max = nb_etages
        self.etage_actuel = self.etage_min
    
    def go_etage(self, etage: int) -> int:
        """ Aller à l'étage
        input
        -----
            int -- etage
        output
        ------
            int -- etage dans lequel je me suis tp
        exemple
        -------
        >>> go_etage(3)
        3
        >>> go_etage(1)
        1
        """
        return etage