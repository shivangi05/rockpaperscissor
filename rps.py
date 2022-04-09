import random

rock= "🪨"
paper = "📃 "
scissor = "✂️"

#Computer's decision
bot = random.randint(0,2)

#Player's decision
player = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor")
p1 = int(player)

#Computer's decision display
if bot == 0:
    print("Computer chose " + rock)
elif bot == 1:
    print("Computer chose " + paper)
elif bot== 2:
    print("Computer chose " + scissor)
    
#Player's decision display
if p1 == 0:
    print("Player chose " +rock)
elif p1 == 1:
    print("Player chose " +paper)
elif p1== 2:
    print("Player chose " +scissor)
    
#Winner display
if p1 == bot:
    print("Game is tie")
elif p1 == 0:
    if bot == 1:
        print("You Won! 👍")
    elif bot == 2:
        print("You lost! 👎")
elif p1 == 1:
    if bot == 0:
        print("You Won! 👍")
    elif bot == 2:
        print("You lost! 👎")
elif p1 == 2:
    if bot == 0:
        print("You lost! 👎")
    if bot == 1:
        print("You Won! 👍")
