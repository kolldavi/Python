import random

def hangman(word):
    wrong =  0
    stages = [""," _______________            "
                ,"|             |             "
                ,"|             |             "
                ,"|             0             "
                ,"|            /|\            "
                ,"|            / \            "
                ,"|                           "
                ,"|_____________              "]
    rletters = list(word)
    board = ["__"] * len(word);
    win = False
    print("Welcome to Hangman")
    while wrong  < len(stages)-1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind]  = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong+1]))
        print("You lose! It was {}".format(word))

word_list = ["python", "java", "computer", "hacker", "painter"]
random_number = random.randint(0, 4)
word = word_list[random_number]
hangman(word)
