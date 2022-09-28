import random
repeat_flag=1
choice_list = ["rock", "paper", "scissor"]

while repeat_flag==1:
    flag=1
    while(flag==1):
        human_choice=input("What do you want to choose Human?")
        if choice_list[0]==human_choice.lower():
            human_choice_int=0
        elif choice_list[1]==human_choice.lower():
            human_choice_int=1
        elif choice_list[2]==human_choice.lower():
            human_choice_int=2
        else:
            print("Incorrect input, try again!")
            continue
        flag=0
    computer_choice = random.randint(0, 2)
    computer_choice_string = choice_list[computer_choice]
    print(f"Computer chose: {computer_choice_string}")
    if human_choice_int==computer_choice:
        print("It is a draw!!")
    elif human_choice_int == 2 and computer_choice == 0:
        print("Computer wins!!")
    elif human_choice_int == 0 and computer_choice == 2:
        print("You win!!")
    elif human_choice_int>computer_choice:
        print("You win!!")
    else: print("You lose!!")
    Quit = input("Do you want to quit the game?")
    if Quit == "Yes" or "y" or "Y":
        repeat_flag = 0
    elif Quit == "No" or "n" or "N":
        continue
    else:
        print("Sorry I didn't get you try again please?")