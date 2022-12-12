import q3

if __name__ == '__main__':
    player1 = q3.Player(0,10)
    player2 = q3.Player(1,20)

    players = q3.Players()
    players.add_player(player1)
    players.add_player(player2)

    print(players)
    d = q3.isParetoImprovement(players,player1.number_id)

    print(d)