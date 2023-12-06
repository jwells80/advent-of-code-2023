MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()


def play_games(filename):
    games = read_file(filename)
    game_total = 0
    for game in games:
        game_total += process_game(game)

    print(game_total)


def play_games_fewest(filename):
    games = read_file(filename)
    game_total = 0
    for game in games:
        game_total += process_game_fewest(game)
    return game_total


def process_game(game):
    game_id, possiblities = game.split(":")
    grabs = possiblities.split(";")
    for grab in grabs:
        dice_colors = grab.split(",")
        for dice in dice_colors:
            dice = dice.strip()
            dice = dice.split(" ")
            if MAX_CUBES[dice[1]] < int(dice[0]):
                return 0
    return int(game_id.split(" ")[1])


def process_game_fewest(game):
    dice_max = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    grabs = game.split(":")[1].split(";")
    for grab in grabs:
        dice_colors = grab.split(",")
        for dice in dice_colors:
            dice = dice.strip().split(" ")
            if dice_max[dice[1]] <= int(dice[0]):
                dice_max[dice[1]] = int(dice[0])
    return dice_max["red"] * dice_max["blue"] * dice_max["green"]


if __name__ == "__main__":
    # str = "Game 1: 9 red, 2 green, 13 blue; 10 blue, 2 green, 13 red; 8 blue, 3 red, 6 green; 5 green, 2 red, 1 blue"
    # play_games("aoc2.txt")
    # print(process_game_fewest(str))
    print(play_games_fewest("aoc2.txt"))
