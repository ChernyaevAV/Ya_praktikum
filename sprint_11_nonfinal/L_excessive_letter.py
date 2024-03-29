from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    for symbol in shorter:
        longer = longer.replace(symbol, '', 1)
    return longer


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))