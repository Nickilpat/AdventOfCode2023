import re

input_file = open("01/input.txt", "r")
calibration_lines = input_file.read().split('\n')
input_file.close()

calibration_sum = sum([int(x[0] + (x[-1])) for x in [re.sub("\D","",x) for x in calibration_lines] if x])

print(calibration_sum)