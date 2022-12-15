import Quarto
from Players import RandomPlayer

N_GAMES = 100

if __name__ == "__main__":
    winners = [0, 0]
    draw = 0
    game = Quarto.Quarto()
    players = (RandomPlayer(game), RandomPlayer(game))
    game.set_players(players)
    for _ in range(N_GAMES):
        res = game.run(output_enabled=False)
        if res >= 0:
            winners[res] += 1   
        else:
            draw += 1
        game.reset()

    print(f"Games won by Player 0 : {winners[0]}")
    print(f"Games won by Player 1 : {winners[1]}")
    print(f"Draws : {draw}")
