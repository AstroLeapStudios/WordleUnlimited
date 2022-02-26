from termcolor import cprint
from pyfiglet import figlet_format
import os
import random

r = random.SystemRandom()

dict = open("dictionary.txt", encoding="latin-1")
dictRead = dict.read()
words = dictRead.split("\n")

def results(guessStr):
    global lastword
    global coloredBank
    os.system('cls||clear')
    char1 = word[0].upper()
    char2 = word[1].upper()
    char3 = word[2].upper()
    char4 = word[3].upper()
    char5 = word[4].upper()

    guess1 = guessStr[0].upper()
    guess2 = guessStr[1].upper()
    guess3 = guessStr[2].upper()
    guess4 = guessStr[3].upper()
    guess5 = guessStr[4].upper()

    if(lastword != "none" or lastword == "none"):
        found = guess1 in lastword

        if(found != True):
            if(guess1 == char1):
                ind = bank.index(guess1)
                bank[ind] = f"\033[0;32m{guess1}\033[0;37m"
            elif(guess1 == char2 or guess1 == char3 or guess1 == char4 or guess1 == char5):
                ind = bank.index(guess1)
                bank[ind] = f"\033[1;33m{guess1}\033[0;37m"
            else:
                ind = bank.index(guess1)
                bank[ind] = f"\033[0;31m{guess1}\033[0;37m"


        found = guess2 in lastword

        if(found != True):
            if(guess2 == char2):
                ind = bank.index(guess2)
                bank[ind] = f"\033[0;32m{guess2}\033[0;37m"
            elif(guess2 == char1 or guess2 == char3 or guess2 == char4 or guess2 == char5):
                ind = bank.index(guess2)
                bank[ind] = f"\033[1;33m{guess2}\033[0;37m"
            else:
                ind = bank.index(guess2)
                bank[ind] = f"\033[0;31m{guess2}\033[0;37m"

        found = guess3 in lastword

        if(found != True):
            if(guess3 == char3):
                ind = bank.index(guess3)
                bank[ind] = f"\033[0;32m{guess3}\033[0;37m"
            elif(guess3 == char2 or guess3 == char1 or guess3 == char4 or guess3 == char5):
                ind = bank.index(guess3)
                bank[ind] = f"\033[1;33m{guess3}\033[0;37m"
            else:
                ind = bank.index(guess3)
                bank[ind] = f"\033[0;31m{guess3}\033[0;37m"

        found = guess4 in lastword

        if(found != True):
            if(guess4 == char4):
                ind = bank.index(guess4)
                bank[ind] = f"\033[0;32m{guess4}\033[0;37m"
            elif(guess4 == char2 or guess4 == char1 or guess4 == char3 or guess4 == char5):
                ind = bank.index(guess4)
                bank[ind] = f"\033[1;33m{guess4}\033[0;37m"
            else:
                ind = bank.index(guess4)
                bank[ind] = f"\033[0;31m{guess4}\033[0;37m"

        found = guess5 in lastword

        if(found != True):
            if(guess5 == char5):
                ind = bank.index(guess5)
                bank[ind] = f"\033[0;32m{guess5}\033[0;37m"
            elif(guess5 == char2 or guess5 == char1 or guess5 == char3 or guess5 == char4):
                ind = bank.index(guess5)
                bank[ind] = f"\033[1;33m{guess5}\033[0;37m"
            else:
                ind = bank.index(guess5)
                bank[ind] = f"\033[0;31m{guess5}\033[0;37m"

        lastword = guess1 + guess2 + guess3 + guess4 + guess5

    print(*bank)

def guess():
    guessIn = input("Guess (5 Characters): ")
    if len(guessIn) != 5:
        print("\033[0;31m Guess length is not [\033[0;37m5\033[0;31m] characters\033[0;37m!")
        guess()
    
    found = guessIn in dictRead

    if found == False:
        print("\033[0;31m Guess is not valid in word dictionairy\033[0;37m!")
        guess()


    listed = [guessIn[0], guessIn[1], guessIn[2], guessIn[3], guessIn[4]]
    countText = []
    for i in range(5):
            count = 0
            l = listed
            for c in l:
                if(c.upper() == guessIn[i - 1].upper()):
                        count += 1
            countText = [countText, count]

    found = 2 in countText

    if found:
        print("\033[0;31m Guess includes a character twice\033[0;37m!")
        guess()

    results(guessIn)

while(True):
    global lastword
    lastword = "none"
    os.system("title Wordle Unlimited")
    cprint(figlet_format('Wordle Unlimited', font='big'),
       'blue', attrs=['bold'])

    print("\nClick enter to continue to the game")
    input("")

    os.system('cls||clear')
    length = range(6)
    bank = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    word = r.choice(words)
    for i in length:
        print(*bank)
        guess()