import random

def create():
    print("How much would you like to add as your initial bankroll?")
    return int(input())

bank = create()
print(f"How much would you like to bet from your ${bank} on this round?")
bet = int(input())
while bet <= 0:
    print("Invalid amount, try again.")
    bet = int(input())

while bank > 0 and bet > 0:
    roll = random.randint(2,12)

    print(f"You have rolled a {roll}")

    if roll == 7 or roll == 11:
        print("You win!")
        bank = bank + bet
        print(f"You now have ${bank}")

    elif roll == 2 or roll == 3 or roll == 12:
        print("You lose!")
        bank = bank - bet
        print(f"You now have ${bank}")
    else:
        print(f"You have made point with {roll}, you must roll that value again to win or roll a 7 to lose.")
        point = roll

        roll = random.randint(2,12)
        while roll != point and roll != 7:
            print(f"you have rolled a {roll}, let's roll again")
            roll = random.randint(2,12)

        if roll == point:
            bank = bank + bet
            print(f"You have won with a roll of {roll}!  You now have {bank}")
        else:
            bank = bank - bet
            print(f"You have lost with a roll of {roll}!  You now have {bank}")

    print("Would you like to play again? Y or N")
    choice = input()
    if choice == "Y":
        print(f"How much would you like to bet from your ${bank} on this round?")
        bet = int(input())
        if(bet > bank):
            print("You have bet more than you have available, the game will now end.")
            bet = 0
    else:
        bet = 0
