from utils.api_client import get_advent_of_code_input

def is_safe_report(levels: list[int]) -> bool:
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    valid_differences = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

    return (increasing or decreasing) and valid_differences

from utils.api_client import get_advent_of_code_input

def is_safe_report_v2(levels: list[int]) -> bool:
    is_increasing = all(
        1 <= (levels[i + 1] - levels[i]) <= 3 for i in range(len(levels) - 1)
    )
    is_decreasing = all(
        1 <= (levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)
    )
    return is_increasing or is_decreasing

def is_safe_with_dampener(levels: list[int]) -> bool:
    
    if is_safe_report(levels):
        return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe_report_v2(modified_levels):
            return True

    return False

def solution02():
   
    solution_input: str = get_advent_of_code_input(
        2, 2024, "SESION COOKIE"
    )

    reports = [list(map(int, line.split())) for line in solution_input.splitlines()]

    safe_reports = sum(1 for report in reports if is_safe_with_dampener(report))

    print(f"So, in this example with Dampener, {safe_reports} reports are safe.")


def solution01():
    
    solution_input: str = get_advent_of_code_input(
        2, 2024, "SESION COOKIE"
    )

    reports = [list(map(int, line.split())) for line in solution_input.splitlines()]

    safe_reports = sum(1 for report in reports if is_safe_report(report))

    print(f"So, in this example, {safe_reports} reports are safe.")


solution01()
solution02()
