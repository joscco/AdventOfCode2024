import re
import time

with open("input.txt") as f:
    lines = [list(map(int, re.findall(r"\d+", line))) for line in f]

    def check_result(expected_result, previous_result, numbers_left, allow_concat=False):
        # All operators make the result bigger, so if the expected result is exceeded, we can stop
        if previous_result and expected_result < previous_result:
            return False

        if not numbers_left:
            return expected_result == previous_result

        if previous_result is None:
            add_prev = 0
            mul_prev = 1
            concat_prev = ""
        else:
            add_prev = previous_result
            mul_prev = previous_result
            concat_prev = str(previous_result)

        if check_result(expected_result, add_prev + numbers_left[0], numbers_left[1:], allow_concat):
            return True

        if check_result(expected_result, mul_prev * numbers_left[0], numbers_left[1:], allow_concat):
            return True

        if allow_concat and check_result(expected_result, int(concat_prev + str(numbers_left[0])), numbers_left[1:], allow_concat):
            return True

        return False

    calibration_sum_1 = sum(line[0] for line in lines if check_result(line[0], None, line[1:]))
    print(calibration_sum_1)

    # Part 2
    calibration_sum_2 = sum(line[0] for line in lines if check_result(line[0], None, line[1:], True))
    print(calibration_sum_2)