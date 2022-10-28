from class_Buss import *
from class_Tram import *
from class_Tram_Depot import *
from class_Buss_Depot import *

bus1 = Bus('BUS 01B',100, 175)
bus2 = Bus('BUS 02B',95,150)
bus3 = Bus('BUS 03B',70,125)

tram1 = Tram('TRM 001T', 50, 3)
tram2 = Tram('TRM 002T', 40, 2)
tram3 = Tram('TRM 003T', 30, 1)

tram_dep1 = Tram_Depot('Zajezdnia Tramwajowa')
bus_dep1 = Bus_Depot('Zajezdnia Autobusowa')

if __name__ == '__main__':
    print(tram1)
    print('#' * 30)
    print(tram_dep1)
    print('#'*30)
    print(bus3)
    print('#' * 30)
    print(bus_dep1)
    print('#' * 30)




