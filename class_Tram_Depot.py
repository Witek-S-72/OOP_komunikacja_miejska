from class_Depot import *
from class_Tram import *

class Tram_Depot(Depot):

    TYPE = "Tramwajowa"

    def __init__(self, nazwa):
        super().__init__(nazwa)

    def __str__(self):
        Tram.revoke_trams()
        Tram.railcar_sum()
        return f'Nazwa: {self.nazwa}'

