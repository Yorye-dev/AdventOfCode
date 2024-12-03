from utils.api_client import get_advent_of_code_input
import re

def solution01():

    input_str: str = get_advent_of_code_input(
        3, 2024, "Sesion token"
    )
    
    filter_input :str = r'mul\((\d+),(\d+)\)'

    list_of_mul = re.findall(filter_input, input_str)
    
    total_sum = sum(int(x) * int(y) for x, y in list_of_mul)
    
    print(f"Solution01: {total_sum}")

def solution02():

    input_str: str = get_advent_of_code_input(
        3, 2024, "Sesion Token"
    )

    pattern = r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)'

    matches = re.finditer(pattern, input_str)

    should_multiply = True
    total_sum = 0

    for match in matches:
        if match.group() == "do()":
            should_multiply = True 
        elif match.group() == "don't()":
            should_multiply = False
        elif match.group().startswith("mul("):
            x, y = int(match.group(1)), int(match.group(2))
            if should_multiply:
                total_sum += x * y

    print(f"Solution02: {total_sum}")

solution01()
solution02()
