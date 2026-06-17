import random

data = [
    {
        'name': 'instagram',
        'follower_count': 685,
        'description': 'social media platform',
        'country': 'united states'
    },
    {
        'name': 'cristiano ronaldo',
        'follower_count': 664,
        'description': 'footballer',
        'country': 'portugal'
    },
    {
        'name': 'ariana grande',
        'follower_count': 363,
        'description': 'musician and actress',
        'country': 'united states'
    },
    {
        'name': 'dwayne johnson',
        'follower_count': 382,
        'description': 'actor and professional wrestler',
        'country': 'united states'
    },
    {
        'name': 'selena gomez',
        'follower_count': 415,
        'description': 'musician and actress',
        'country': 'united states'
    },
    {
        'name': 'kylie jenner',
        'follower_count': 391,
        'description': 'reality tv star',
        'country': 'united states'
    },
    {
        'name': 'lionel messi',
        'follower_count': 507,
        'description': 'footballer',
        'country': 'argentina'
    },
    {
        'name': 'beyoncé',
        'follower_count': 144,
        'description': 'musician',
        'country': 'united states'
    },
    {
        'name': 'khloe kardashian',
        'follower_count': 293,
        'description': 'reality tv star',
        'country': 'united states'
    },
    {
        'name': 'justin bieber',
        'follower_count': 287,
        'description': 'musician',
        'country': 'canada'
    },
    {
        'name': 'kim kardashian',
        'follower_count': 110,
        'description': 'reality tv star',
        'country': 'united states'
    },
    {
        'name': 'virat kohli',
        'follower_count': 274,
        'description': 'cricketer',
        'country': 'india'
    },
    {
        'name': 'nike',
        'follower_count': 292,
        'description': 'sports brand',
        'country': 'united states'
    },
    {
        'name': 'national geographic',
        'follower_count': 269,
        'description': 'magazine',
        'country': 'united states'
    },
    {
        'name': 'taylor swift',
        'follower_count': 282,
        'description': 'musician',
        'country': 'united states'
    },
    {
        'name': 'lebron james',
        'follower_count': 154,
        'description': 'basketball player',
        'country': 'united states'
    },
    {
        'name': 'shakira',
        'follower_count': 97,
        'description': 'musician',
        'country': 'colombia'
    },
    {
        'name': 'neymar jr',
        'follower_count': 235,
        'description': 'footballer',
        'country': 'brazil'
    },
    {
        'name': 'messi 10 store',
        'follower_count': 70,
        'description': 'brand',
        'country': 'argentina'
    },
    {
        'name': 'kendall jenner',
        'follower_count': 278,
        'description': 'model',
        'country': 'united states'
    },
    {
        'name': 'narendra modi',
        'follower_count': 101,
        'description': 'prime minister',
        'country': 'india'
    },
    {
        'name': 'real madrid',
        'follower_count': 179,
        'description': 'football club',
        'country': 'spain'
    },
    {
        'name': 'miley cyrus',
        'follower_count': 206,
        'description': 'musician and actress',
        'country': 'united states'
    },
    {
        'name': 'fc barcelona',
        'follower_count': 145,
        'description': 'football club',
        'country': 'spain'
    },
    {
        'name': 'priyanka chopra',
        'follower_count': 92,
        'description': 'actress',
        'country': 'india'
    }
]


def format_account(account):
    name = account["name"].title()
    desc = account["description"]
    country = account["country"].title()
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print("🔥 HIGHER LOWER GAME 🔥\n")
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        # Account a will be previous account b
        account_a = account_b
        account_b = random.choice(data)
        
        # make sure both a and b are not same
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_account(account_a)}")
        print("VS")
        print(f"Against B: {format_account(account_b)}")
        
        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"✅ Correct! Score: {score}")
        else:
            game_should_continue = False
            print(f"❌ Wrong! Final Score: {score}")
            print(f"{account_a['name'].title()} = {a_follower_count}M followers")
            print(f"{account_b['name'].title()} = {b_follower_count}M followers")
            
game()


