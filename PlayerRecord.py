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
