from class_Depot import Depot

class Vehicle:

    def __init__(self, reg_numb, max_speed):
        '''
        :param reg_numb: nr pojazdu
        :param max_speed: prędkość max pojazdu
        '''
        self.reg_numb = reg_numb
        self.max_speed = max_speed

    def __str__(self):
        return f'Nr rejestr.:  {self.reg_numb}, prędkość maks.:  {self.max_speed} km/h, '

