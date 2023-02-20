import random


def coin_winner(stavka, player_to_throw, player_not_to_throw):
    player_throw = player_to_throw
    player_not_throw = player_not_to_throw
    side = random.choice(['Vkid', 'Uzzi'])
    if side == 'Vkid':
        print("Выпал Vkid")
        if stavka == "Vkid":
            winner, loser = player_throw, player_not_throw
        elif stavka == 'Uzzi':
            winner, loser = player_not_throw, player_throw
        else:
            print('Какая-то ошибочка')
            exit()
    elif side == 'Uzzi':
        print("Выпал Uzzi")
        if stavka == "Vkid":
            winner, loser = player_not_throw, player_throw
        elif stavka == 'Uzzi':
            winner, loser = player_throw, player_not_throw
        else:
            print('Какая-то ошибочка')
            exit()
    print('Победил', winner)
    return winner, loser, side