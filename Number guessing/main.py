import random

ask = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
num = random.randint(1,10)

def level_of_game(ask):
    if ask == 'easy':
        return 8
    elif ask == 'hard':
        return 4
    else:
        return "Invalid input! Type 'easy' or 'hard': "

    
def game(lives,num):
    while lives>0:
        print(f"You've {lives} lives left ")
        guess = int(input("Guess a number between 1-10: "))
        
        if guess == num:
            print("You guessed it right, its", num)
            break
        elif guess> num:
            print("Too high")
            lives-=1
        elif guess<num:
            print("Too low")
            lives-=1
            
lives= level_of_game(ask)
if lives==0:
    print("You lose")
else:
    game(lives,num)


