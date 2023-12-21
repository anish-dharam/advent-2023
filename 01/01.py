def part1(lines: list[str]) -> int:
    def calibration(line: str) -> int:
        digits = [char for char in line if char.isdigit()]
        return int(digits[0]) * 10 + int(digits[-1])

    return sum([calibration(line) for line in lines])


def test_part1():
    assert part1(["79"]) == 79
    assert part1([]) == 0
    assert part1(["1", "1"]) == 22
    assert part1(["1230\n", "bc5d"]) == 65


def part2(lines: list[str]) -> int:
    num_to_val = {
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

    def calibration(line: str) -> int:
        digits = [char for char in line if char.isdigit()]
        indexed_digits: list[tuple[int, int]] = [
            (i, int(char)) for i, char in enumerate(line) if char.isdigit()
        ]
        for num, val in num_to_val.items():
            if num in line:
                indexed_digits.append((line.find(num), val))
                indexed_digits.append((line.rfind(num), val))
        indexed_digits.sort()
        return indexed_digits[0][1] * 10 + indexed_digits[-1][1]

    return sum([calibration(line) for line in lines])


def test_part2():
    assert part2(["79"]) == 79
    assert part2([]) == 0
    assert part2(["1", "1"]) == 22
    assert part2(["1230\n", "bc5d"]) == 65
    assert part2(["two1230\n", "bc5d"]) == 75
    assert part2(["five"]) == 55
    assert part2(["three", "eight"]) == 121
    assert part2(["2one"]) == 21
    assert part2(["twone"]) == 21
    assert part2(["2one", "three4"]) == 55
    assert part2(["ktkgsvkthreevone2xxrxzgdqpnone2xnf"]) == 32


f = open("01-input.txt")
lines = [line for line in f]
print(f"part 1: {part1(lines)}")
print(f"part 2: {part2(lines)}")
