import os
import re
import sys

import numpy as np

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def convert_to_digit(s):
    match s:
        case 'zero':
            return '0'
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'


def get_calibration_value(line, include_written_numbers=False):
    if include_written_numbers:
        matches = re.findall('zero|one|two|three|four|five|six|seven|eight|nine|[0-9]', line)
        digits = [match if match.isdigit() else convert_to_digit(match) for match in matches]
    else:
        digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1])


print(np.sum([get_calibration_value(line) for line in lines]))
print(np.sum([get_calibration_value(line, True) for line in lines]))
