import json
import math


def fuel_needed_for_module(weight):
    calculated_fuel = math.floor(weight / 3) - 2
    return calculated_fuel if calculated_fuel > 0 else 0


def first_exercise(data):
    fuels_for_modules = map(fuel_needed_for_module, data)
    sum_of_fuel = sum(fuels_for_modules)
    print(sum_of_fuel)
    return sum_of_fuel


def fuel_needed_for_module_with_fuel(weight):
    fuel_for_module = fuel_needed_for_module(weight)
    fuel_for_fuel = 0 if fuel_for_module <= 0 else fuel_needed_for_module_with_fuel(fuel_for_module)
    return fuel_for_module + fuel_for_fuel


def second_exercise(data):
    fuels_for_modules_with_fuels = map(fuel_needed_for_module_with_fuel, data)
    total_sum = sum(fuels_for_modules_with_fuels)
    print(total_sum)
    return total_sum


if __name__ == '__main__':
    with open("input_data.txt", "r") as fin:
        input_data = list(map(lambda x: int(x), fin.readlines()))
    first_output = first_exercise(input_data)
    second_output = second_exercise(input_data)
    with open("output_data.json", "w") as fout:
        json.dump({
            "First Exercise": first_output,
            "Second Exercise": second_output
        }, fout)
