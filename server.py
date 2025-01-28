import time
from game_manager import GameManager


def main():
    manager = GameManager()

    # Create a game between 'ind' and 'pak'
    game1 = manager.create_game('ind', 'pak')
    print('Game Created ID', game1)

    # Create teams for the game
    manager.create_team_for_user(game1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'p1')
    manager.create_team_for_user(game1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21], 'p2')
    manager.create_team_for_user(game1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22], 'p3')

    # Start the game
    manager.start_game(game1)

    # Play the game and update scores
    manager.play(game1, 90, 21, 1)

    # Get the top player
    print('Top Score', manager.get_top_k_users(game1, 1))

    # End the game
    manager.end_game(game1)

    # Wait for 1 second before creating a new game
    time.sleep(1)

    game2 = manager.create_game('ind', 'wi')
    print('Game Created ID', game2)

if __name__ == '__main__':
    main()
