def wins_rock_scissors_paper(player1, player2):
    player_throw = player1.lower()
    opponent_throw = player2.lower()

    if player_throw == "rock" and opponent_throw == "scissors":
        return True
    elif player_throw == "paper" and opponent_throw == "rock":
        return True
    elif player_throw == "scissors" and opponent_throw == "paper":
        return True
    else:
        return False

# Correct function call
result = wins_rock_scissors_paper("rock", "paper")
print(result)
