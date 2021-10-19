letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Build your Point Dictionary
letter_to_points = {key:value for key,value in zip(letters, points)}
letter_to_points.update({key.lower():value for key,value in zip(letters, points)})

print("Letter to Points:")
print(letter_to_points)
letter_to_points[" "] = 0


# Score a Word
def score_word(word):
    point_total = 0
    for c in word:
        point_total += letter_to_points.get(c, 0)
    return point_total


brownie_points = score_word("BROWNIE")
# print(brownie_points)


# Score a Game
players = ["player1", "wordNerd", "Lexi Con", "Prof Reader"]
words = [["BLUE", "TENNIS", "EXIT"], ["EARTH", "EYES", "MACHINE"], ["ERASER", "BELLY", "HUSKY"], ["ZAP", "COMA", "PERIOD"]]
player_to_words = {key:value for key,value in zip(players, words)}

print("Player to Word:")
print(player_to_words)

player_to_points = {}
for player,words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print("Player to Points:")
print(player_to_points)

# More Stuff

# Updates total points of the player
def update_point_totals(player, word):
    try:
        player_to_points[player] += score_word(word)
    except KeyError:
        player_to_points[player] = score_word(word)


# Takes player and word, and add word to the list of words they've played
def play_word(player, word):
    try:
        player_to_words[player].append(word)
    except KeyError:
        player_to_words[player] = [word]
    update_point_totals(player, word)

play_word("player1", "PURPLE")
play_word("newPlayer", "NEW")
print(player_to_words)
print(player_to_points)

# empty line