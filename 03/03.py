from dataclasses import dataclass


@dataclass
class Number:
    val: int
    positions: list[tuple[int, int]]

    def get_num_positions(self) -> int:
        return len(self.positions)

    def __len__(self) -> int:
        return len(self.positions)


def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    nums: list[Number] = []
    symbols: set[tuple[int, int]] = set()
    asterisks: list[tuple[int, int]] = []

    for row, line in enumerate(lines):
        for num in get_nums(line, row):
            nums.append(num)
        for col, char in enumerate(line):
            if is_symbol(char):
                if char == "*":
                    asterisks.append((row, col))
                symbols.add((row, col))

    print(part1(nums, symbols))
    print(part2(nums, asterisks))


def is_symbol(char: str) -> bool:
    return char != "." and not char.isdigit()


def test_is_symbol():
    assert is_symbol("a") is True
    assert is_symbol("1") is False
    assert is_symbol(".") is False
    assert is_symbol("!") is True


def get_nums(line: str, row: int) -> list[Number]:
    nums = []
    acc = 0
    cols = []
    for col, char in enumerate(line):
        if char.isdigit():
            acc = acc * 10 + int(char)
            cols.append(col)
        else:
            if acc != 0:
                nums.append(Number(acc, [(row, c) for c in cols]))
                acc = 0
                cols = []
    if acc != 0:
        nums.append(Number(acc, [(row, c) for c in cols]))
    return nums


def test_get_nums():
    assert get_nums("1", 1) == [Number(1, [(1, 0)])]
    assert get_nums("123", 1) == [Number(123, [(1, 0), (1, 1), (1, 2)])]
    assert get_nums("1.2", 0) == [Number(1, [(0, 0)]), Number(2, [(0, 2)])]


def neighbours(r: int, c: int) -> list[tuple[int, int]]:
    deltas = [-1, 0, 1]
    res = []
    for dr in deltas:
        for dc in deltas:
            if dr != 0 or dc != 0:
                res.append((r + dr, c + dc))
    return res


def part1(nums: list[Number], symbols: set[tuple[int, int]]) -> int:
    def has_adj_symbol(r: int, c: int) -> bool:
        return any((rr, cc) in symbols for rr, cc in neighbours(r, c))

    def is_part_num(num: Number) -> bool:
        return any(has_adj_symbol(row, col) for row, col in num.positions)

    return sum(num.val for num in nums if is_part_num(num))


def part2(nums: list[Number], asterisks: list[tuple[int, int]]) -> int:
    pos_to_num = {}
    for num in nums:
        for pos in num.positions:
            pos_to_num[pos] = num.val

    acc = 0

    for r, c in asterisks:
        nbrs = neighbours(r, c)
        nbr_nums = {pos_to_num[nbr] for nbr in nbrs if nbr in pos_to_num}
        if len(nbr_nums) == 2:
            x, y = nbr_nums
            acc += x * y

    return acc


if __name__ == "__main__":
    main()
