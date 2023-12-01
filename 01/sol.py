import re

input_file = open("01/input.txt", "r")
calibration_lines = input_file.read().split('\n')
input_file.close()

calibration_long_numbers = [re.sub("\D","",x) for x in calibration_lines]
calibration_numbers = [int(x[0] + (x[-1])) for x in calibration_long_numbers if x]
calibration_sum = sum(calibration_numbers)

print(calibration_sum)