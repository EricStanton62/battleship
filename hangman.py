import tkinter
from PIL import ImageTk, Image

#wordlist
words=["anxiety","battery","apricot","chapter","diamond","example","finance","genetic","husband","intense","journal","killing","limited","manager","nowhere","operate","parking","quality","receipt","stretch","typical","utility","virtual","writing","perform"]

#import randint
from random import randint

#function to choose the word
def choose_word():
    x=randint(0,len(words)-1)
    return words[x]

#function to assure input is valid
def valid_input():
    while True:
        x=input("input a single letter a-z:")
        if len(x) ==1 and x.isalpha()==True:
            return x

#function for changing the board if guessed correctly
def board_change(guess):
    if actual_word.find(guess)>=0:
        if dunno[actual_word.find(guess)]==guess:
            print("you already guessed that letter")
            return 1
        elif actual_word.count(guess)>=1:
            for i in range(len(actual_word)):
                if actual_word[i]==guess:
                    dunno[i]=guess
            return 0
    else:
        return 1


#hangman image that changes
def dude(guess):
    print("guesses remaining:")
    if guess==6:
        print("""  __\n |  |\n    |\n    |\n    |""")
    elif guess==5:
        print("""  __\n |  |\n o  |\n    |\n    |""")
    elif guess==4:
        print("""  __\n |  |\n o  |\n |  |\n    |""")
    elif guess==3:
        print("""  __\n |  |\n o  |\n\|  |\n    |""")
    elif guess==2:
        print("""  __\n |  |\n o  |\n\|/ |\n    |""")
    elif guess==1:
        print("""  __\n |  |\n o  |\n\|/ |\n/   |""")
    elif guess==0:
        print("""  __\n |  |\n o  |\n\|/ |\n/ \ |""")


guesses=7
letter=""
y=0
inp=""

while guesses>0:
    if guesses==7:
        guesses-=1
        actual_word=choose_word()
        dunno=[]

#adds lines for however many letters the word is
        for i in range(len(actual_word)):
            dunno.append("__")
    
    print (actual_word)
    print(*dunno, sep=' ')
    dude(guesses)
    letter=valid_input()
    y=board_change(letter)

#if you win enter this
    if not "__" in dunno:
        print("You win, the word was:", actual_word)
        inp=input('Care to play again?(y/n)')
        if inp.lower()=="y" or inp.lower()=="yes":
            guesses=7
            continue
        else:
            break

    guesses-=y
    if guesses==0:
        jpegdata=Image.open('hangman.jpeg')
        jpegdata.show()
        jpegdata.close()
        inp=input("Game over. Do you want to play again with a new word?(y/n)")
        if inp.lower()=="y" or inp.lower()=="yes":
            guesses=7
            continue
        else:
            print('Better luck next time, Farewell')



