import random
print("the fantastic game of rock paper and scissor")
random_num = random.randint(1,3)
wordfy = str(random_num)
user =input("choose from rock , paper and scissor").lower()

if user == "rock":
    user = 'rock'
    print(r'''
            ____, O
        /   /M|
        /|MMMMMMMM
        {| | // |}
        -_}| |/ \ |{_apx
    ''')
elif user == "paper":
    user = 'paper'
    print(r'''
            |DAILY NEWS|
                |&&& ======|
                |=== ======|
                |=== == %%$|
                |[_] ======|
                |=== ===!##|
        ejm97   |__________|
            ''')
elif user == "scissor":
    user = 'scissor'
    print(r'''
                _       ,/'
        (_).  ,/'
        __  ::
        (__)'  `\.
                    `\.
    ''')

if wordfy == "1":
    computer = "rock"
    print("Computer")
    print("rock")
    print(r'''
                ____, O
            /   /M|
            /|MMMMMMMM
            {| | // |}
            -_}| |/ \ |{_apx
    ''')
elif wordfy == "2":
    computer = "paper"
    print("Computer")
    print("paper")
    print(r'''
            |PAPER|
                |&&& ======|
                |=== ======|
                |=== == %%$|
                |[_] ======|
                |=== ===!##|
        ejm97   |__________|
    ''')
elif wordfy == "3":
    computer = "scissor"
    print("Computer")
    print("scissor")
    print(r'''
                _       ,/'
        (_).  ,/'
        __  ::
        (__)'  `\.
                    `\.
    ''')

if user == computer:
    print("it's a draw")