import time
from game import Game
from player import Player


class GameManager:
    def __init__(self):
        self.games_map = {}
        self.players_map = {}
        self.batsmen = []
        self.bowler = []
        self._init_players()

    def _init_players(self):
        l = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 111]
        for i in l:
            self.batsmen += list(range(i, i + 6))
            self.bowler += list(range(i + 6, i + 11))

    def create_game(self, team1, team2):
        for gid in self.games_map:
            if self.games_map[gid].check_game_exists(team1, team2):
                raise 'game already exists'

        game_id = int(time.time())
        self.games_map[game_id] = Game(game_id, team1, team2)
        return game_id

    def create_team_for_user(self, game_id, players, user_name):
        if game_id not in self.games_map:
            return None

        bat = 0
        bowl = 0
        for p in players:
            if p in self.batsmen:
                bat += 1
            elif p in self.bowler:
                bowl += 1
            else:
                raise 'Invalid Player'

        if bat != 6 or bowl != 5:
            raise 'invalid Team'

        if game_id in self.players_map and user_name in self.players_map[game_id]:
            raise 'Already registered'

        if game_id not in self.players_map:
            self.players_map[game_id] = {}
        self.players_map[game_id][user_name] = Player(user_name, game_id, players, bat, bowl)
        print('Create Team For User', user_name)

    def start_game(self, game_id):
        if game_id not in self.games_map:
            raise 'invalid game id'

        self.games_map[game_id].start()
        print('Game Started ID', game_id)

    def end_game(self, game_id):
        if game_id not in self.games_map:
            raise 'invalid game id'

        self.games_map[game_id].end()

        # Return winner
        max_score = 0
        play = []
        for p in self.players_map[game_id]:
            pobj = self.players_map[game_id][p]
            if pobj.score > max_score:
                max_score = pobj.score
                play = [pobj]
            elif pobj.score == max_score:
                play.append(pobj)
        print('Game Ended ID', game_id)
        print('Winner score:', max_score)
        print('Winner', [p.name for p in play])

    def play(self, game_id, bat_id, bowl_id, score):
        if game_id not in self.players_map:
            raise 'invalid game'

        if not self.games_map[game_id].started:
            raise 'game not started'

        for team in self.players_map[game_id]:
            self.players_map[game_id][team].add_score(bat_id, bowl_id, score)

    def get_top_k_users(self, game_id, k):
        top_score = {}
        for p in self.players_map[game_id]:
            pobj = self.players_map[game_id][p]
            if pobj.score not in top_score:
                top_score[pobj.score] = []
            top_score[pobj.score].append(pobj.name)

        count = 0
        u = []
        sarr = sorted(top_score.keys(), reverse=True)
        for s in sarr:
            for p in top_score[s]:
                count += 1
                u.append(p)
                if count == k:
                    break
        return u
