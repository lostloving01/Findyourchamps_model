class PlayerRcd:
    def __init__(self, name="", account_id=""):
        self.name = name
        self.account_id = account_id
        self.count = 0
        self.gameid = []
        self.res = []
        self.champ_use = []

    def add_a_match(self, game_id, game_res, champ):
        self.gameid.append(game_id)
        self.res.append(game_res)
        self.champ_use.append(champ)
        self.count += 1


class GeneralRcd:
    def __init__(self):
        self.game_count = 0
        self.game_id_set = set([])
        self.player_count = 0
        self.player_set = set([])
        self.champ_use = {}
        self.champ_result = {}

    def add_a_game(self, game_id):
        self.game_id_set.add(game_id)
        self.game_count = self.game_id_set.__len__()

    def add_a_player(self, player):
        self.player_set.add(player)
        self.player_count = self.player_set.__len__()

    def add_a_match(self, champ, result):
        if champ in self.champ_use:
            self.champ_use[champ] += 1
        else:
            self.champ_use[champ] = 1
            self.champ_result[champ] = 0
        if result:
            self.champ_result[champ] += 1



