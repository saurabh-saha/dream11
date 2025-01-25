

# Cricket Game Simulation

This project simulates a cricket game between two teams, allowing players to register, play, and track scores. It also includes the ability to start and end games, and determine the top scorer.

## Features

- **Create Game**: Create a new game between two teams.
- **Create Team**: Register a team of players for a game.
- **Play**: Update player scores based on batting and bowling.
- **Start Game**: Begin the game after teams have been registered.
- **End Game**: End the game and determine the winner based on scores.
- **Top Scorers**: Retrieve the top K players by score.

## Classes

### `Game`
Represents a cricket game with attributes like the game ID, teams, and game status.

- **Methods**:
  - `check_game_exists(t1, t2)`: Checks if a game between the teams exists.
  - `start()`: Starts the game.
  - `end()`: Ends the game.

### `Player`
Represents a player in the game with attributes like name, team, and scores.

- **Methods**:
  - `add_score(bat_id, bowl_id, score)`: Adds score based on batting and bowling.

## Setup

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository (if applicable):**
   ```bash
   git clone https://github.com/your-repo/cricket-game-simulation.git
   cd cricket-game-simulation
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not present, no additional packages are required for this script.

## Running the Game

You can run the script as follows:

1. Run the Python file:
   ```bash
   python game_simulation.py
   ```

2. This will simulate the creation of a game, team registrations, scoring, and determine the winner.

### Example Execution

```bash
game1 = createGame('ind', 'pak')
print(game1)
createTeamForUser(game1, [1,2,3,4,5,6,7,8,9,10,11], 'p1')
createTeamForUser(game1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21], 'p2')
createTeamForUser(game1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22], 'p3')
startGame(game1)
play(game1, 90, 21, 1)
print('Top Score', getTopKUsers(game1, 1))
endGame(game1)
```

This will create a game between the teams "ind" and "pak," register teams, update scores, and determine the winner.

## Error Handling

- Invalid players are flagged if they don't belong to the predefined batsmen or bowler list.
- Duplicate team registrations are prevented.
- Games cannot be started or ended without the required conditions being met.

