import random

print("the fantastic game of rock paper and scissor")
random_num = random.randint(1,3)
wordfy = str(random_num)
user =input("choose from rock , paper and scissor \n").lower()

if user == "rock":
    user = 'rock'
    print(r'''
            __________________
                .-'  \ _.-''-._ /  '-.
            .-/\   .'.      .'.   /\-.
            _'/  \.'   '.  .'   './  \'_
            :======:======::======:======:  
            '. '.  \     ''     /  .' .'
            '. .  \   :  :   /  . .'
                '.'  \  '  '  /  '.'
                ':  \:    :/  :'
                    '. \    / .'
                    '.\  /.'    miK
                        '\/'
    ''')
elif user == "paper":
    user = 'paper'
    print(r'''
         __________________
        |\                /|
        | \              / | P
        | /\____________/\ | r
        |/                \| 5
        |__________________|
            ''')
elif user == "scissor":
    user = 'scissor'
    print(r'''
            ____
        / __ \
        ( (__) |___ ___
        \________,'   """""----....____
        _______<  () dd       ____----'
        / __   __`.___-----""""
        ( (__) |
        \____/
    ''')

if wordfy == "1":
    computer = "rock"
    print("Computer")
    print("rock")
    print(r'''
        __________________
            .-'  \ _.-''-._ /  '-.
        .-/\   .'.      .'.   /\-.
        _'/  \.'   '.  .'   './  \'_
        :======:======::======:======:  
        '. '.  \     ''     /  .' .'
        '. .  \   :  :   /  . .'
            '.'  \  '  '  /  '.'
            ':  \:    :/  :'
                '. \    / .'
                '.\  /.'    miK
                    '\/'
    ''')
elif wordfy == "2":
    computer = "paper"
    print("Computer")
    print("paper")
    print(r'''
         __________________
        |\                /|
        | \              / | P
        | /\____________/\ | r
        |/                \| 5
        |__________________|
    ''')
elif wordfy == "3":
    computer = "scissor"
    print("Computer")
    print("scissor")
    print(r'''
            ____
            / __ \
            ( (__) |___ ___
            \________,'   """""----....____
            _______<  () dd       ____----'
            / __   __`.___-----""""
            ( (__) |
            \____/
    ''')

if user == computer:
    print("it's a draw")
elif user == "scissor" and computer == "rock":
    print("u lose i win the computer is the greatest")
elif user == "scissor" and computer == "paper":
    print("whatever it's just a stupid game anyway")
elif user =="paper" and computer == "scissor":
    print("like u have a chance just stop trying u will never beat me")
elif user == "paper" and computer == "rock":
    print("not fair i wasn't ready ")
elif user == "rock" and computer == "paper":
    print("at this point u should give up u will never win , since am nice i will help you wrap this rock in this envelope")
elif user == "rock" and computer == "scissor":
    print("am just letting u win so u wouldn't cry")


