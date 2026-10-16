
import random
again="y"
while again=="y":
    choose=int(input("what do u choose? Type 0 for scissor, 1 for rock or 2 for paper.\n"))
    game=["""    __________
        ________'   _______)______
                        __________)__
                      _______________)
        ____      (_______)
            '_____(______) """,

    """        _______
        ______'   ____)
                 (_____)
                 (______)
        ______   (_____)
             '___(___) """  ,

    """
                 __________
        ________'   _______)______
                        __________)__
                      _______________)
        _________    _____________)
                 '______________)  """
                 ]
    if choose>=3 or choose<0:
        print("you typed an invalid number, you lose!")
    else:

        print("what you choose")
        print(game[choose])
        print("computer choose:\n")
        guess=random.randint(0,2)
        print(game[guess])
        if choose==0 and guess==2:
            print("you win!")
        elif choose==1 and guess==0:
            print("you win!")
        elif choose==2 and guess==1:
            print("you win!")
        elif choose==guess:
            print("it is draw")

        else:
            print("you lose")
        again = input("do you want to play again? y/n: ").lower()




 






