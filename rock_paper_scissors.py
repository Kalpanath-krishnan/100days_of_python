import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[rock,paper,scissors]

user_choice=int(input("enter your choice!!! 0 for rock 1 for paper and 2 foe scissors"))
# choice=""
# if user_choice==0:
#     choice="rock"
# elif user_choice==1:
#     choice="paper"
# elif user_choice==2:
#     choice="scissors"
# else:
#     choice=="invalid choice"



# choice1=""
computer_choice=random.randint(0,2)
# if computer_choice==0:
#     choice1="rock"
# elif computer_choice==1:
#     choice1="paper"
# else:
#     choice1="scissors"




print(f"user chose {game_images[user_choice]}")
print(f"computer chose {game_images[computer_choice]}")

if user_choice == computer_choice:
    print("its a draw")
elif user_choice==0 and computer_choice==2:
    print("you won")
elif user_choice==2 and computer_choice==1:
    print("you won")
elif user_choice==2 and computer_choice==0:
    print("computer won")
elif user_choice==0 and computer_choice==1:
    print("computer won")
elif user_choice==1 and computer_choice==2:
    print("computer won")
else:
    print("invalid")



