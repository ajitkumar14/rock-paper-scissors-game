import random

options =["rock","paper","scissors"]
user =input("Enter rock ,paper or scissors : ")
computer =random.choice(options)

print(f"your choice : {user}")
print(f"computer choice : {computer}")

if user == computer:
    print("Match Draw!!!!!!!!!!")
else:
    if user == "rock" and computer == "scissors":
        print("you win!")
    elif user =="paper" and computer == "rock":
        print("you win!")
    elif user == "scissors" and computer =="paper":
        print("you win!")
    else:
        print("computer win!")
