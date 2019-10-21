import random, os

random_num = 0

print("You have 4 chances to guess an integer between 0 and 100.\nGood luck!\n")

def play_game():

    global random_num
    random_num = random.randint(0, 100)
    lives      = 4

    while lives > 0:
        print("Type your number > ", end="")
        
        while True:
            try:
                user_guess = int(input())
                break
            except ValueError:
                print("Invalid Input. Try again...")
                print("Type your number > ", end="")

        if user_guess == random_num:
            #game win
            return True 
        
        else:
            lives -= 1

            if user_guess > random_num:
                print("Nope... My number is smaller")
            if user_guess < random_num:
                print("Nope... My number is bigger")

    if lives <= 0:
        return False


while True:
    
    os.system("clear")
    status_game = play_game()

    os.system("clear")
    print(f"My number was {random_num}.")

    if status_game == True:
        print("Congrats!, you won.")
    else:
        print("You Lost.\nThat was close!")
    
    print("Do you want to play again? [Y/N] > ", end="")
    play_again = input().upper()

    if play_again == "Y":
        continue
    else:
        print("Bye.")
        break


