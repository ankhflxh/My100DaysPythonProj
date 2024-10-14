import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

print('''

█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
''')

print("WELCOME TO ASHLEY'S COMPUTER VS YOU!!!\n")
game = [rock, paper, scissors]
comp = (random.choice(game))
choice = int(input("WHAT DO YOU CHOOSE? TYPE 0 FOR ROCK, 1 FOR PAPER OR 2 FOR SCISSORS\n"))
if choice == 0:
    print("YOU CHOSE ROCK\n")
    print(rock)
    print("THE COMPUTER CHOOSE:\n")
    print(comp)
    if comp == game[1]:
        print("YOU LOSE!!!")
    elif comp == game[2]:
        print("YOU WIN!!!")
    else:
        print ("DRAW!!!")
elif choice == 1:
    print("YOU CHOSE PAPER\n")
    print(paper)
    print("THE COMPUTER CHOOSE:\n")
    print(comp)
    if comp == game[0]:
        print("YOU WIN!!!")
    elif comp == game[2]:
        print("YOU LOSE!!!")
    else:
        print("DRAW!!!")
elif choice == 2:
    print("YOU CHOSE SCISSORS\n")
    print(scissors)
    print("THE COMPUTER CHOOSE:\n")
    print(comp)
    if comp == game[0]:
        print("YOU WIN!!!")
    elif comp == game[1]:
        print("YOU LOSE!!!")
    else:
        print("DRAW!!!")
else:
    print("PLEASE PICK A NUMBER")
