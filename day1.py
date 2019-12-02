import math

modules = [88623, 101095, 149899, 89383, 54755, 73496, 115697, 99839, 65903,
           140201, 95734, 144728, 113534, 82199, 98256, 107126, 54686, 61243,
           54763, 119048, 58863, 134097, 84959, 130490, 145813, 115794, 130398,
           69864, 133973, 58382, 75635, 77153, 132645, 91661, 126536, 118977,
           137568, 100341, 142080, 63342, 84557, 51961, 61956, 87922, 92488,
           107572, 51373, 70148, 80672, 134880, 105721, 100138, 80394, 145117,
           50567, 122606, 112408, 110737, 111521, 144309, 65761, 113147, 58920,
           96623, 65479, 66576, 94244, 64493, 142334, 65969, 99461, 143656,
           134661, 90115, 122994, 66994, 135658, 134336, 102958, 111410,
           107930, 54711, 101397, 111350, 86453, 134383, 134276, 130342,
           80522, 64875, 68182, 83400, 121302, 105996, 123580, 130373, 123987,
           107932, 78930, 132068]
sum_fuel = 0
sum_fuel_for_fuel = 0

for module in modules:
    fuel = math.floor(module/3) - 2
    print("Fuel consumption for module '" + str(module) + "': " + str(fuel))
    sum_fuel += fuel

    fuel_for_fuel = fuel
    while fuel_for_fuel > 0:
        fuel_for_fuel = math.floor(fuel_for_fuel/3) - 2
        if fuel_for_fuel < 0:
            fuel_for_fuel = 0
        sum_fuel_for_fuel += fuel_for_fuel


print("Total fuel consumption of modules: " + str(sum_fuel))
print("Total fuel consumption of fuel: " + str(sum_fuel_for_fuel))
print("Total fuel consumption: " + str(sum_fuel + sum_fuel_for_fuel))
