class Helmet:

    def __init__(self, boost=False):
        self.name = 'Helmet'
        self.dice_edge_id = 1
        self.power_long = 0
        self.power_short = 0
        self.defence_long = 0
        self.defence_short = 1
        self.steal = 0
        self.add_gold = 0
        if boost:
            self.name = 'Helmet++'
            self.dice_edge_id = 11
            self.add_gold = 1


class Shield:

    def __init__(self, boost=False):
        self.name = 'Shield'
        self.dice_edge_id = 2
        self.power_long = 0
        self.power_short = 0
        self.defence_long = 1
        self.defence_short = 0
        self.steal = 0
        self.add_gold = 0
        if boost:
            self.name = 'Shield++'
            self.dice_edge_id = 12
            self.add_gold = 1


class Axe:

    def __init__(self, boost=False):
        self.name = 'Axe'
        self.dice_edge_id = 3
        self.power_long = 0
        self.power_short = 1
        self.defence_long = 0
        self.defence_short = 0
        self.steal = 0
        self.add_gold = 0
        if boost:
            self.name = 'Axe++'
            self.dice_edge_id = 13
            self.add_gold = 1


class Arrow:

    def __init__(self, boost=False):
        self.name = 'Arrow'
        self.dice_edge_id = 4
        self.power_long = 1
        self.power_short = 0
        self.defence_long = 0
        self.defence_short = 0
        self.steal = 0
        self.add_gold = 0
        if boost:
            self.name = 'Arrow++'
            self.dice_edge_id = 14
            self.add_gold = 1


class Thief:

    def __init__(self, boost=False):
        self.name = 'Thief'
        self.dice_edge_id = 5
        self.power_long = 0
        self.power_short = 0
        self.defence_long = 0
        self.defence_short = 0
        self.steal = 1
        self.add_gold = 0
        if boost:
            self.name = 'Thief++'
            self.dice_edge_id = 15
            self.add_gold = 1


class Nothing:

    def __init__(self, boost=False):
        self.name = 'Nothing'
        self.dice_edge_id = 6
        self.power_long = 0
        self.power_short = 0
        self.defence_long = 0
        self.defence_short = 0
        self.steal = 0
        self.add_gold = 0
        if boost:
            self.name = 'Nothing++'
            self.dice_edge_id = 16
            self.add_gold = 1
