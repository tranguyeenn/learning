import random 

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    randoms = random.choices(choices, k=10)
    return randoms[5]

'''possible outcomes: 
- Player wins
    - Rock > Scissors
    - Paper > Rock
    - Scissors > Paper
- Computer wins
    - Rock > Scissors
    - Paper > Rock
    - Scissors > Paper
- Tie
    - Both player and computer choose the same option
'''

def winner(player, computer):
    if player == computer:
        return "Tie"
    
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        return "Player wins"
    
    elif (computer == 'rock' and player == 'scissors') or (computer == 'paper' and player == 'rock') or (computer == 'scissors' and player == 'paper'):
        return "Computer wins"
    
    else: 
        not_valid = True
        while not_valid:
            player = input("Enter your choice (rock, paper, scissors): ").lower()
            if player in ['rock', 'paper', 'scissors']:
                not_valid = False
                return winner(player, computer)
            else:
                print("Invalid input. Please choose rock, paper, or scissors.")
    
def play_game():
    computer_score = 0 
    player_score = 0 
    status = True

    while status:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        computer = computer_choice()
        result = winner(player, computer)

        print(f'Computer chose: {computer}')
        print()
        print(f'Result: {result}')

        if result == "Player wins":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1
        else:
            player_score += 1
            computer_score += 1
        
        print()
        print(f'Player score: {player_score} | Computer score: {computer_score}')
        print("-" * 30)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        print("-" * 30)
        if play_again != 'yes':
            status = False
            print("Thanks for playing! Final scores:")
            print(f'Player score: {player_score} | Computer score: {computer_score}')

if __name__ == "__main__":
    play_game()