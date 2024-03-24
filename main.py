import random
def guess(x):
    rand_num=random.randint(1,x)
    guess=0
    while guess != rand_num:
        guess=int(input(f'Enter the number between 1 and {x}:'))
        if guess < rand_num:
            print("Sorry the number you have guessed is too low")
        elif guess > rand_num:
            print("Sorry the number you have entered is too high")
    print(f"wow you have guessed the correct number {rand_num}. hurreyyyy!")
guess(20)





