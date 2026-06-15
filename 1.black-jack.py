import random
#jack,queen,king=10
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(hand):
    score=sum(hand)
    if score>21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score=sum(hand)
    return score

def blackjack():
    player = [deal_card(), deal_card()]
    computer =[deal_card(), deal_card()]
    
    game_over=False
    
    while not game_over:
        player_score = calculate_score(player)
        computer_score = calculate_score(computer)
        
        print(f"Your cards: {player}, score: {player_score}")
        print(f"Computer's first cards: {computer}, score: {computer_score}")
        
        if player_score == 21 or computer_score == 21 or player_score>21:
            game_over = True
            
        else:
            choice=input("Type 'hit' for card, 'stand' to pass: ")
            if choice == "hit":
                player.append(deal_card())
            else:
                game_over = True
            
    while computer_score<17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)
        
    print(f"Your cards: {player}, score: {player_score}")
    print(f"Computer's final cards: {computer}, score: {computer_score}")
            
    if player_score >21:
        print("Bust! You lose ") 
    elif computer_score>21:
        print("Computer bust! You win ") 
    elif player_score>computer_score:
        print("You win! ")
    elif player_score<computer_score:
        print("You lose! ")
    else:
        print("Push!  Draw")
        
ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
blackjack()