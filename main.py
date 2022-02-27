from tkinter.tix import InputOnly
from termcolor import cprint
from pyfiglet import figlet_format
import os
import random

r = random.SystemRandom()

dict = open("dictionary.txt", encoding="latin-1")
dictRead = dict.read()
words = dictRead.split("\n")
word = r.choice(words)

stat = open("stats.txt", encoding="latin-1")
stats = stat.read()
nums = stats.split("\n")

red = []
yellow = []
green = []
bank = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

t = 1
g = 1
    
def bankPrint(userGuess):
    global word
    global red
    global yellow
    global green
    global g

    colLet = ""
    g += 1

    for l in bank:
        l = l.upper()
        if(l in userGuess.upper()):
            if(l in word.upper()):
                if(userGuess.upper().index(l) == word.upper().index(l)):
                    colLet += f"\033[0;32m {l}\033[0;37m"
                    green.append(l)
                else:
                    if(l in green):
                        colLet += f"\033[0;32m {l}\033[0;37m"
                    else:
                        colLet += f"\033[1;33m {l}\033[0;37m"
                        yellow.append(l)
            else:
                colLet += f"\033[0;31m {l}\033[0;37m"
                red.append(l)
        else:
            if(l in red):
                colLet += f"\033[0;31m {l}\033[0;37m"
            elif(l in yellow):
                colLet += f"\033[1;33m {l}\033[0;37m"
            elif(l in green):
                colLet += f"\033[0;32m {l}\033[0;37m"
            else:
                colLet += f" {l}"

    if (userGuess.upper() == word.upper()):
        print(f"\033[0;32mYou guess the word correctly\033[0;37m!")
        global t
        global stat
        t = 2
        t = 1
        num = int(nums[0])
        nums[0] = num + 1
        wrd = str(nums[0]) + "\n" + str(nums[1])
        print(wrd)
        stat.close()
        stat = open("stats.txt", 'w')
        stat.write(wrd)
        stat.close()
        input("Click enter to continue\n")
    else:
        print(f"{colLet} \n")

def guessRes():
    guess()
    
def results(guessStr, rep):
    if(rep == False):
        bankPrint(guessStr)

def guess():
    global inval
    global t
    global g
    global stat
    repeated = False
    inval = False
    if(t == 1 or g != 7):
        guessIn = input("Guess (5 Characters): ")
        if len(guessIn) != 5:
            print("\033[0;31m Guess length is not [\033[0;37m5\033[0;31m] characters\033[0;37m!\n")
            inval = True
            guessIn = ""
            repeated = True
            guessRes()
        else:
            repeated = False
    
        found = guessIn in dictRead

        if found == False:
            print("\033[0;31m Guess is not valid in word dictionairy\033[0;37m!\n")
            inval = True
            guessIn = ""
            repeated = True
            guessRes()
        else:
            repeated = False

        os.system('cls||clear')
        results(guessIn, repeated)
    else:
        print("Game over, you lost!")
        num = int(nums[1])
        nums[1] = num + 1
        wrd = str(nums[0]) + "\n" + str(nums[1])
        stat.close()
        stat = open("stats.txt", 'w')
        stat.write(wrd)
        stat.close()
        input("Click enter to continue\n")

def game():
    global lastword
    lastword = "none"
    os.system("title Wordle Unlimited")
    cprint(figlet_format('Wordle Unlimited', font='big'),
       'blue', attrs=['bold'])

    print(f"\033[0;32mWins\033[0;37m: \033[0;37m{nums[0]} \033[0;31mLosses\033[0;37m: \033[0;37m{nums[1]} \nClick enter to continue to the game")
    input("")

    os.system('cls||clear')
    length = range(6)
    for i in length:
        guess()

game()