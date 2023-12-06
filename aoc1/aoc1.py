all_digits = []


def get_letters_digits(string):
    digits = [0, 0]
    letters = ""
    for l in string:
        try:
            digits[0] = int(l)
            break
        except ValueError:
            letters = letters + l
            if spelled_num_to_int(letters) is not None:
                digits[0] = spelled_num_to_int(letters)
                break
    letters = ""
    for l in reversed(string):
        try:
            digits[1] = int(l)
            break
        except ValueError:
            letters = l + letters
            if spelled_num_to_int(letters) is not None:
                digits[1] = spelled_num_to_int(letters)
                break
    all_digits.append("".join([str(d) for d in digits]))
    return int("".join([str(d) for d in digits]))


def open_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def get_first_last_digit():
    sum = 0
    lines = open_file("aoc1.txt")

    for line in lines:
        digits = "".join(filter(lambda i: i.isdigit(), line))
        sum += int(digits[0] + digits[-1])
    return sum


def get_first_last_digit_by_name_or_number():
    sum = 0
    # lines = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen",
    # ]
    # lines = [
    #     "5eightsevenjtwonem",
    # ]
    lines = open_file("aoc1.txt")
    for line in lines:
        line = line.strip("\n")
        sum += get_letters_digits(line)
    return sum


def spelled_num_to_int(num_str):
    num_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    num_str_len = len(num_str)
    for i in range(len(num_str) - 1):
        beg_num = num_str[i:]
        if beg_num in num_dict:
            return num_dict[beg_num]
        end_num = num_str[: i + 1]
        if end_num in num_dict:
            return num_dict[end_num]
    return None


if __name__ == "__main__":
    # string = "zkjkctxvssix1dqb22five"
    # print(get_first_last_digit())
    # print(get_letters_digits(string))
    print(get_first_last_digit_by_name_or_number())
    # with open("aoc1-digits.txt", "w") as f:
    #     f.write("\n".join(all_digits))
