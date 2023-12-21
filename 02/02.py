from dataclasses import dataclass

@dataclass
class Pick:
    red: int
    green: int
    blue: int
    
BAG = Pick(12, 13, 14)

def parse_pick(s: str) -> Pick:
    pairs = s.split(', ')
    d = {"red": 0, "green": 0, "blue": 0}
    for pair in pairs:
        count, color = pair.split()
        d[color] = int(count)
    return Pick(**d)

def test_parse_pick():
    assert parse_pick("3 blue, 4 red") == Pick(4, 0, 3)
    assert parse_pick("1 blue") == Pick(0, 0, 1)

def parse_game(line: str) -> list[Pick]:
    picks = line.split(": ")[1].split("; ")
    return [parse_pick(pick) for pick in picks]

def test_parse_game():
    assert parse_game("Game 1: 3 blue, 4 red") == [Pick(4, 0, 3)]
    assert parse_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == [Pick(20, 8, 6), Pick(4, 13, 5), Pick(1, 5, 0)]

def part1(games: list[list[Pick]]) -> int:
    def valid_game(game: list[Pick]) -> bool:
        def valid_pick(pick: Pick) -> bool:
            return BAG.red >= pick.red and BAG.green >= pick.green and BAG.blue >= pick.blue
        return all((valid_pick(pick) for pick in game))
    count = 0
    for id, game in enumerate(games, start=1):
        if valid_game(game):
            count += id
    return count

def max_pick(game: list[Pick]) -> Pick:
    reds = [pick.red for pick in game]
    greens = [pick.green for pick in game]
    blues = [pick.blue for pick in game]
    return Pick(max(reds), max(greens), max(blues))

def power(pick: Pick) -> int:
    return pick.red * pick.green * pick.blue

def test_power():
    assert power(Pick(1, 2, 3)) == 6
    assert power(Pick(0, 0, 0)) == 0

def part2(games: list[list[Pick]]) -> int:
    picks = [max_pick(game) for game in games]
    powers = [power(pick) for pick in picks]
    return sum(powers)


with open("input.txt") as f:
    lines = [line.strip() for line in f]
print(part1([parse_game(line) for line in lines]))
print(part2([parse_game(line) for line in lines]))