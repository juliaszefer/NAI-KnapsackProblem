import math

from Knapsack import Knapsack
from BestOne import BestOne

knapsack_data = "Data/plecak.txt"


def read_file(path):
    ffile = open(path, 'r')
    counter = 0
    _k = 0
    _n = 0
    _values = list()
    _weights = list()
    for line in ffile:
        counter += 1
        if counter == 1:
            tmpkn = line.split(" ")
            _k = tmpkn[0]
            _n = tmpkn[1]
        elif counter == 2:
            tmpkn = line.split(",")
            for i in tmpkn:
                _values.append(i)
        elif counter == 3:
            tmpkn = line.split(",")
            for i in tmpkn:
                _weights.append(i)
    knapsack = Knapsack(_k, _n, _values, _weights)
    return knapsack


def int_to_binary(number, length):
    binary = bin(number)[2:]
    binary = binary.zfill(length)
    return binary


def check_weights(number_arr, _knapsack):
    weights_sum = 0
    for i in number_arr:
        weights_sum += int(_knapsack.weights[i])
        if weights_sum > int(_knapsack.k):
            return False
    return True


def sum_values(number_arr, _knapsack):
    values_sum = 0
    for i in number_arr:
        values_sum += int(_knapsack.values[i])
    return values_sum


def find_best(_possibilities, _knapsack):
    best = BestOne(0, 0)
    for i in range(_possibilities):
        print(f"\nIteration number: {i}\n")
        tmp_arr = list()
        binary = int_to_binary(i, int(_knapsack.n))
        binary_list = list(binary)
        for j in range(len(binary_list)):
            if int(binary_list[j]) == 1:
                tmp_arr.append(j)
        if check_weights(tmp_arr, _knapsack):
            current = BestOne(binary, sum_values(tmp_arr, _knapsack))
            if int(current.value) >= int(best.value):
                best = current
        print(f"\nBest one so far: {best.binar}\n")
    return best


knapsack_object = read_file(knapsack_data)
possibilities = math.pow(2, int(knapsack_object.n))
print(f"\n\nAnswer: {find_best(int(possibilities), knapsack_object)}")
