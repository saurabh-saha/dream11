import time
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
checks no such exists b/n player before; ind vs pak
'''

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
            print('scores updated', self.name, score)
        if bowl_id in self.players:
            self.score += score
            print('scores updated', self.name, score)

games_map = {}
l = [1,12,23,34,45,56,67,78,89,100,111]
batsmen = []
bowler = []
for i in l:
    batsmen += list(range(i,i+6))
    bowler += list(range(i+6,i+11))


def createGame(team1, team2):
    for gid in games_map:
        if games_map[gid].check_game_exists(team1, team2):
            raise 'game already exists'

    id = int(time.time())
    games_map[id] = Game(id, team1, team2)
    return id


'''
    check for valid gameID
'''
players_map = {}
def createTeamForUser(gameId, players, userName):
    if gameId not in games_map:
        return None

    bat = 0
    bowl = 0
    for p in players:
        if p in batsmen:
            bat += 1
        elif p in bowler:
            bowl += 1
        else:
            raise 'Invalid Player'

    if bat != 6 or bowl != 5:
        raise 'invalid Team'

    if gameId in players_map and userName in players_map[gameId]:
        raise 'Already registered'

    if gameId not in players_map:
        players_map[gameId] = {}
    players_map[gameId][userName] = Player(userName, gameId, players, bat, bowl)
    print('createTeamForUser',userName)

def startGame(gameId):
    if gameId not in games_map:
        raise 'invalid game id'

    #todo handle when game has stopped
    games_map[gameId].started = True
    print(gameId,'started')


def endGame(gameId):
    if gameId not in games_map:
        raise 'invalid game id'

    #todo handle when game has stopped
    games_map[gameId].stopped = True

    #todo return winner
    max = 0
    play = []
    for p in players_map[gameId]:
        pobj = players_map[gameId][p]
        if pobj.score > max:
            max = pobj.score
            play = [pobj]
        elif pobj.score == max:
            play.append(pobj)
    print(gameId,'ended winner score :',max, 'winner', [p.name for p in play])


def play(gameId, bat_id, bowl_id , score):
    if gameId not in players_map:
        raise 'invalid game'

    if not games_map[gameId].started:
        raise 'game not started'

    for team in players_map[gameId]:
        players_map[gameId][team].add_score(bat_id, bowl_id , score)


def getTopKUsers(gameId, K):
    top_score = {}
    for p in players_map[gameId]:
        pobj = players_map[gameId][p]
        if pobj.score not in top_score:
            top_score[pobj.score] = []
        top_score[pobj.score].append(pobj.name)

    count = 0
    u = []
    sarr = sorted(top_score.keys(),reverse=True)
    for s in sarr:
        for p in top_score[s]:
            count += 1
            u.append(p)
            if count == K:
                break
    return u


if __name__ == '__main__':
    game1 = createGame('ind','pak')
    print(game1)
    createTeamForUser(game1, [1,2,3,4,5,6,7,8,9,10,11], 'p1')
    createTeamForUser(game1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21], 'p2')
    createTeamForUser(game1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22], 'p3')
    startGame(game1)
    play(game1, 90, 21, 1)
    print('Top Score',getTopKUsers(game1,1))
    endGame(game1)

    time.sleep(1)
    print(createGame('ind', 'wi'))



