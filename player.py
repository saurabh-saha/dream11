class Player:
    def __init__(self, name, gameid, players, bat, bowl):
        self.name = name
        self.gameid = gameid
        self.players = players
        self.bat = bat
        self.bowl = bowl
        self.score = 0

    def add_score(self, bat_id, bowl_id, score):
        if bat_id in self.players:
            self.score += score
            print('Scores updated', self.name, score)
        if bowl_id in self.players:
            self.score += score
            print('Scores updated', self.name, score)