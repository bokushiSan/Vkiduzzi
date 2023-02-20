import random


def coin_winner(bet, player_to_throw, player_not_to_throw):
    """
    Random player toss the coin. If the guess is correct, he wins, else, he loses.
    :param bet: str | player's bet - 'Vkid' or 'Uzzi'
    :param player_to_throw: str | name of a player, who throw the coin
    :param player_not_to_throw: str | name of a player, who not throw the coin
    :return winner: str | name of winner of the coin toss
    :return loser: str | name of loser of the coin toss
    """
    player_throw = player_to_throw
    player_not_throw = player_not_to_throw
    side = random.choice(['Vkid', 'Uzzi'])
    if side == 'Vkid':
        if bet == "Vkid":
            winner, loser = player_throw, player_not_throw
        elif bet == 'Uzzi':
            winner, loser = player_not_throw, player_throw
        else:
            exit()
    elif side == 'Uzzi':
        if bet == "Vkid":
            winner, loser = player_not_throw, player_throw
        elif bet == 'Uzzi':
            winner, loser = player_throw, player_not_throw
        else:
            exit()
    return winner, loser, side
