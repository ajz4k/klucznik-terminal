import random
from math import sqrt

GAME_HEIGHT = 10
GAME_WIDTH = 10

def generate_random_position():
    return random.randint(1, GAME_WIDTH), random.randint(1, GAME_HEIGHT)

def calculate_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_border(x, y):
    return x == 0 or y == 0 or x == GAME_WIDTH + 1 or y == GAME_HEIGHT + 1

print("Witaj, wyobraź sobie planszę", GAME_WIDTH, 'x', GAME_HEIGHT, ". Gdzieś na tej planszy jest klucz")

player_x, player_y = 1, 1
key_x, key_y = generate_random_position()
player_key = False
steps = 0
distance_before = calculate_distance(key_x, key_y, player_x, player_y)

while not player_key:
    print('Twoja aktualna pozycja: X =', player_x, '| Y =', player_y)
    move = input("Sterowanie: [W/A/S/D]: ").lower()

    if move in {"w", "a", "s", "d"}:
        if move == "w":
            player_y += 1
        elif move == "a":
            player_x -= 1
        elif move == "s":
            player_y -= 1
        elif move == "d":
            player_x += 1

        steps += 1

        if check_border(player_x, player_y):
            print('\nBłąd: Dotknąłeś granicy mapy!\n')
            player_x, player_y = max(1, min(player_x, GAME_WIDTH)), max(1, min(player_y, GAME_HEIGHT))
            steps -= 1
        else:
            if (player_x, player_y) == (key_x, key_y):
                print('----------')
                print('Wygrałeś!')
                print('Przeszedłeś grę w', steps, 'ruchach!')
                print('----------')
                player_key = True
            else:
                distance_after = calculate_distance(key_x, key_y, player_x, player_y)
                if distance_before > distance_after:
                    print('Cieplej')
                else:
                    print('Zimniej')

                distance_before = distance_after
    elif move == "debug":
        print('----------')
        print('Pozycja klucza: X =', key_x, '| Y =', key_y)
        print('----------')
    else:
        print('Niepoprawny ruch. Użyj [W/A/S/D] do poruszania się lub "debug" do wyświetlenia pozycji klucza.')