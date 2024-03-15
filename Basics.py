'''
name= input("Hey There!! How are you? Please enter your name here: ");

print("The Name of the person is: ", name);


for i in range(len(name)):
    print(name[i+1]);
    '''

def sum(num1,num2):
    return num1 + num2

print("The sum is", sum(8,9))

def wins_rock_scissors_paper(player1,player2):
     player_throw = player_throw.lower()
     opponent_throw = opponent_throw.lower()

   if player_throw == "rock" and opponent_throw == "scissors":
        return True
    elif player_throw == "paper" and opponent_throw == "rock":
        return True
    elif player_throw == "scissors" and opponent_throw == "paper":
        return True