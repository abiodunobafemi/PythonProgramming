#Rock, Paper, Scissors
import random

print("Welcome to our Rock, Paper, Scissors game!")

for i in range(5):
    player1 = "rock"
    #player2 = "scissors"
    computer = random.choice(['rock', 'paper', 'scissors'])
    
    if player1 == 'rock' and computer == 'scissors':
        print("Player 1 wins!")
    elif player1 == 'rock' and computer == 'paper':
        print("Player 2 wins!")
    elif player1 == 'rock' and computer == 'rock':
        print("It's a TIE!!!!")
