from class_Vehicle import *


class Tram(Vehicle):

    tram_list = []
    railcar_qtty = []

    def __init__(self, reg_numb, max_speed, railcar_numb):
        super().__init__(reg_numb, max_speed)
        self.railcar_number = railcar_numb
        self.tram_list.append(self)
        self.railcar_qtty.append(self.railcar_number)

    def __str__(self):
        return f'Nr rejestr.:  {self.reg_numb}, prędkość maks.:  {self.max_speed} km/h, ' \
               f'ilość wagoników: {self.railcar_number}'

    @classmethod
    def revoke_trams(cls) ->str:
        for tram in Tram.tram_list:
            print(str(tram))

    @classmethod
    def railcar_sum(cls)->float:
        print(f'Łączna ilość wagonów tramwajowych: {sum(Tram.railcar_qtty)} szt.')
