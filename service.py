def play_game(TennisGame, p1Points, p2Points, player1_name, player2_name):
    game = TennisGame(player1_name, player2_name)
    for i in range(max(p1Points, p2Points)):
        if i < p1Points:
            game.won_point(player1_name)
        if i < p2Points:
            game.won_point(player2_name)
    return game