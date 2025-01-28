class Game:
    def __init__(self, gameid, team1, team2):
        self.gameid = gameid
        self.team1 = team1
        self.team2 = team2
        self.started = False
        self.ended = False

    def check_game_exists(self, t1, t2):
        cur_teams = [self.team1, self.team2]
        if t1 in cur_teams and t2 in cur_teams:
            return True
        return False

    def start(self):
        self.started = True

    def end(self):
        self.ended = True