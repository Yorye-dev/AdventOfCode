from functools import reduce
from utils.file_utils import read_input, format_input_file
from collections import Counter

def parse_input(data):
    return list(map(int, data))

def calculate_distance(list01, list02):
    pairs = zip(sorted(list01), sorted(list02)) 
    return sum(abs(a-b) for a, b in pairs)

def calculate_frecuence(numbers):
    return Counter(numbers)


def solve01():
    format_input_file("day01/input.txt","day01/formatted_input.txt" )
    data = read_input("day01/formatted_input.txt")
    list01, list02 = [], []
    for line in data:
        nums = line.strip().split("\t")
        list01.append(int(nums[0]))
        list02.append(int(nums[1]))
    
    list01 = sorted(list01)
    list02 = sorted(list02)
    
    return calculate_distance(list01, list02)

def solve02():

    result = 0
    format_input_file("day01/input.txt","day01/formatted_input.txt" )
    data = read_input("day01/formatted_input.txt")
    list01, list02 = [], []
    for line in data:
        nums = line.strip().split("\t")
        list01.append(int(nums[0]))
        list02.append(int(nums[1]))
    
    list01 = sorted(list01)
    list02 = sorted(list02)

    list02_frequencies = calculate_frecuence(list02)

    for number in list01:
        result += number * list02_frequencies.get(number,0)

    return result


if __name__ == "__main__":
    print ("Result first part: ", solve01())
    print ("Result second part: ", solve02())


