import random

Points = []
minPlayer = 2
players = 0
maxscore = 100
DiceNum = 2
gameRound = 0

def setPlayers():
    while True:
        players = input("How many players are playing?\n")
        if players.isdigit():
            players = int(players)
            if minPlayer <= players:
                for i in range(players):
                    Points.append(0)
                return players

def diceroll(player, DiceNum):
    throw = 0
    print(f"\n\tPlayer {player + 1}s turn:",end = "")
    for i in range(DiceNum):
        print("\n\tHit Space Bar and Enter to throw die !!",end = " ")
        sp = input()
        if sp == " ":
            die = random.randint(1, 6)
            print(f"\t \tPlayer {player + 1} has thrown die {i + 1} which landed on {die}")
            throw += die
        else:
            print("your turn skipped!!")
    Points[player] += throw
    print(f"\n \tPlayer {player + 1}s score for this round is : {throw}")
    print(f"\tPlayer {player + 1}s total score is now: {Points[player]}")
    return throw

def checkWin(maxscore):
    for player in range(players):
        if (Points[player] >= maxscore):
            print(f"\nPlayer {player + 1} wins!! Congratulations!!")
            return True

    return False


if __name__ == "__main__":
    players = setPlayers()
    while True:
        gameRound += 1
        print(f"\nRound: {gameRound}")
        for i in range(players):
            diceroll(i, DiceNum)
        print(f"\nScores after round {gameRound} ")
        for i in range(players):
            print(f"Player {i+1} --> {Points[i]}")
        if (checkWin(maxscore)):
            break
