from random import randint

# 36 карт, 1-9 стоимость, 4 масти
def zap_colod(coloda):
    for i in range(9):
        for j in range(4):
            coloda.append(i);

def player_coloda(coloda, player_coloda):
    for i in range(18):
        random = randint(0, len(coloda)-1)
        player_coloda.append(coloda[random])
        coloda.pop(random)

def igra(first, second):
    n = 1
    j = 2
    while(len(first) != 0 and len(second) != 0):
        if first[0] > second[0] or first[0] == 0 and second[0] == 8:
            first.append(second[0])
            second.pop(0)
        elif first[0] < second[0] or second[0] == 0 and first[0] == 8:
            second.append(second[0])
            first.pop(0)
        elif first[0] == second[0]: # спор
            spor = [first[0], second[0]]
            j = 2
            while True:
                if j+1 > len(first) or j+1 > len(second):
                    first = second
                    second = []
                    break

                if first[j] > second[j]:
                    first = first + spor
                    for i in range(j+1):
                        second.pop(0)
                    break
                elif first[j] < second[j]:
                    second = second + spor
                    for i in range(j+1):
                        first.pop(0)
                    break
                else:
                    spor.append(first[j])

                    spor.append(second[j])

                    j = j + 2
        n = n + 1
    return n

def full_game(coloda, first, second):
    zap_colod(coloda)
    player_coloda(coloda, first)
    player_coloda(coloda, second)
    return igra(first, second)

coloda = []
first_player = []
second_player = []

sum = 0

for i in range(10000):
    sum = sum + full_game(coloda, first_player, second_player)
    coloda = []
    first_player = []
    second_player = []

print(sum / 10000)