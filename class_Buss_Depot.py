from class_Depot import *
from class_Buss import *


class Bus_Depot(Depot):

    TYPE = "Autobusowa"

    def __init__(self, nazwa):
        super().__init__(nazwa)

    def __str__(self):
        Bus.revoke_bus()
        Bus.fuel_sum()
        return f'Nazwa: {self.nazwa}'



