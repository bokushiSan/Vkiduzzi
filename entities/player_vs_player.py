class PVP:
    """
    Class PVP in which calculations of battle between two players are performed.
    """
    def __init__(self):
        """
        Initialize class variables.
        """
        pass

    @staticmethod
    def calculations(picked_list):
        """
        Counting all abilities of every of six picked dices and summarize them.
        :param picked_list: list | list of six picked dices
        :return abilities: dict | dictionary of all abilities' summarize
        """
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

    def pretreatment(self, player1, player2):
        """
        Pretreatment of picked list of dices.
        :param player1: class | first player
        :param player2: class | second player
        :return calc_p1: list | list of first player's picked dices
        :return calc_p2: list | list of second player's picked dices
        """
        p1_picked = [i.name for i in player1.dice_sides]
        p2_picked = [i.name for i in player2.dice_sides]
        calc_p1 = self.calculations(p1_picked)
        calc_p2 = self.calculations(p2_picked)
        return calc_p1, calc_p2

    def damage_count(self, player1, player2):
        """
        Counting summarize of players damage.
        :param player1: class | first player
        :param player2: class | second player
        :return p1_power: int | summarized first player's damage
        :return p2_power: int | summarized second player's damage
        """
        calc_p1, calc_p2 = self.pretreatment(player1, player2)
        p1_power = max((max(calc_p1['Power long'] - calc_p2['Defence long'], 0)) + (
            max(calc_p1['Power short'] - calc_p2['Defence short'], 0)), 0)
        p2_power = max((max(calc_p2['Power long'] - calc_p1['Defence long'], 0)) + (
            max(calc_p2['Power short'] - calc_p1['Defence short'], 0)), 0)
        return p1_power, p2_power

    def gold_added(self, player1, player2):
        """
        Counting summarize of players added gold (all dices with boost=True).
        :param player1: class | first player
        :param player2: class | second player
        :return p1_add_gold: int | first player's added gold
        :return p2_add_gold: int | second player's added gold
        """
        calc_p1, calc_p2 = self.pretreatment(player1, player2)
        p1_add_gold = calc_p1['Add gold']
        p2_add_gold = calc_p2['Add gold']
        return p1_add_gold, p2_add_gold

    def gold_stolen(self, player1, player2):
        """
        Counting summarize of players stolen gold (if Thief was used).
        :param player1: class | first player
        :param player2: class | second player
        :return p1_add_gold: int | first player's stolen gold
        :return p2_add_gold: int | second player's stolen gold
        """
        calc_p1, calc_p2 = self.pretreatment(player1, player2)
        p1_steal_gold = calc_p1['Steal']
        p2_steal_gold = calc_p2['Steal']
        return p1_steal_gold, p2_steal_gold

    def pvp(self, player1, player2):
        """
        Results of the battle.
        :param player1: class | first player
        :param player2: class | second player
        """
        p1_power, p2_power = self.damage_count(player1, player2)
        player1.life -= p2_power
        player2.life -= p1_power
        player1.life = max(player1.life, 0)
        player2.life = max(player2.life, 0)
        p1_plus_gold, p2_plus_gold = self.gold_added(player1, player2)
        player1.gold += p1_plus_gold
        player2.gold += p2_plus_gold
        p1_stolen, p2_stolen = self.gold_stolen(player1, player2)
        player1.gold -= p2_stolen
        player2.gold += p2_stolen
        player2.gold -= p1_stolen
        player1.gold += p1_stolen
