class PVP:

    def __init__(self):
        pass

    def calculations(self, picked_list):
        power_long = list()
        power_short = list()
        defence_long = list()
        defence_short = list()
        steal = list()
        add_gold = list()
        for i in picked_list:
            power_long.append(i.power_long)
            power_short.append(i.power_short)
            defence_long.append(i.defence_long)
            defence_short.append(i.defence_short)
            steal.append(i.steal)
            add_gold.append(i.add_gold)
        abilities = {'Power long': sum(power_long), 'Power short': sum(power_short),
                     'Defence long': sum(defence_long), 'Defence short': sum(defence_short),
                     'Steal': sum(steal), 'Add gold': sum(add_gold)}
        return abilities

    def predobrabotka(self, player1, player2):
        p1_picked = [i.name for i in player1.dice_sides]
        p2_picked = [i.name for i in player2.dice_sides]
        calc_p1 = self.calculations(p1_picked)
        calc_p2 = self.calculations(p2_picked)
        return calc_p1, calc_p2

    def powaaa(self, player1, player2):
        calc_p1, calc_p2 = self.predobrabotka(player1, player2)
        p1_power = max((max(calc_p1['Power long'] - calc_p2['Defence long'], 0)) + (
            max(calc_p1['Power short'] - calc_p2['Defence short'], 0)), 0)
        p2_power = max((max(calc_p2['Power long'] - calc_p1['Defence long'], 0)) + (
            max(calc_p2['Power short'] - calc_p1['Defence short'], 0)), 0)
        return p1_power, p2_power

    def give_me_gold(self, player1, player2):
        calc_p1, calc_p2 = self.predobrabotka(player1, player2)
        p1_add_gold = calc_p1['Add gold']
        p2_add_gold = calc_p2['Add gold']
        return p1_add_gold, p2_add_gold

    def take_my_gold(self, player1, player2):
        calc_p1, calc_p2 = self.predobrabotka(player1, player2)
        p1_steal_gold = calc_p1['Steal']
        p2_steal_gold = calc_p2['Steal']
        return p1_steal_gold, p2_steal_gold

    def pvp(self, player1, player2):
        p1_power, p2_power = self.powaaa(player1, player2)
        player1.life -= p2_power
        player2.life -= p1_power
        player1.life = max(player1.life, 0)
        player2.life = max(player2.life, 0)
        p1_plus_gold, p2_plus_gold = self.give_me_gold(player1, player2)
        player1.gold += p1_plus_gold
        player2.gold += p2_plus_gold
        p1_snitched, p2_snitched = self.take_my_gold(player1, player2)
        player1.gold -= p2_snitched
        player2.gold += p2_snitched
        player2.gold -= p1_snitched
        player1.gold += p1_snitched




