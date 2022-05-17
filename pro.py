import random
print("ROCK PAPER SCISSORS - GAME")
print("""THE RULES ARE:
         Rock wins against scissors.
         Scissors win against paper.
         Paper wins against rock.""")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lis=[rock,paper,scissors]
while(1):
    user=int(input("Press 1 for ROCK,   Press 2 for PAPER,   press 3 for SCISSORS,  press 4 for EXIT: "))
    if(user in [1,2,3]):
        usertaken=lis[user-1]
        print("You choose :",usertaken)
        comp=random.choice(lis)
        print("Computer choose:",comp)
        if(usertaken==paper and comp==rock or (usertaken==rock and comp==scissors) or (usertaken==scissors and comp==paper)):
            print("🥳CONGRATULATIONS YOU WON🥳")
            break
        elif(usertaken==comp):
           print("😲DRAW PLAY AGAIN😲")
           continue
        else:
            print("😥YOU LOSE😥")
            break
    else:
        print("OOPS!! YOU ENTERED INVALID...ENTER VALID ITEM")
        continue
