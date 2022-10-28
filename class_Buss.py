from class_Vehicle import *


class Bus(Vehicle):

    bus_list = []
    fuel_list = []

    def __init__(self, reg_numb, max_speed, fuel_consum):
        super().__init__(reg_numb, max_speed)
        self.fuel_consum = fuel_consum
        self.bus_list.append(self)
        self.fuel_list.append(self.fuel_consum)

    def __str__(self):
        return f'Nr rejestr.:  {self.reg_numb}, prędkość maks.:  {self.max_speed} km/h, ' \
               f'zużycie paliwa/m-c: {self.fuel_consum}'

    @classmethod
    def revoke_bus(cls)->str:
       for bus in Bus.bus_list:
            print(bus)

    @classmethod
    def fuel_sum(cls)->float:
        print(f'Łączna ilość paliwa w miesiącu: {sum(Bus.fuel_list)} litrów')



