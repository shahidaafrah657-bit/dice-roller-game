import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("🎲 Welcome to the Dice Game!")
    
    while True:
        choice = input("\nRoll the dice? (y/n): ").lower()
        
        if choice == 'y':
            player_roll = roll_dice()
            computer_roll = roll_dice()
            
            print(f"\nYou rolled: {player_roll}")
            print(f"Computer rolled: {computer_roll}")
            
            if player_roll > computer_roll:
                print("🎉 You win!")
            elif player_roll < computer_roll:
                print("😢 Computer wins!")
            else:
                print("🤝 It's a tie!")
        
        elif choice == 'n':
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play_game()