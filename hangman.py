# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:49:26 2022

@author: Tom
"""

import random

def chooseWord():
    with open('sowpods.txt', 'r') as f:
        all_text = f.read()
        all_list = all_text.split()
        i = random.randint(0, len(all_list))
        return all_list[i]
    
answerWord = chooseWord()
answerList = list(answerWord)
displayList =  ['_ '] * len(answerList)
usedLetters = []
count = 6
condition = False

print('Welcome to hangman!')
print(''.join(displayList))


def checkEnd():
    global count
    if '_ ' not in displayList:
        print('Well done!')
        return True
    elif count == 0:
        print('The word was ' + answerWord)
        return True
    else:
        return False
    
def checkUsed(guess):
    for i in range(len(usedLetters)):
        if usedLetters[i] == guess:
            print('Already Used!')
            return False
    usedLetters.append(guess)
    
def loop():
    global condition
    global count
    hit = False
    guess = str(input('Guess a letter: ')).upper()
    if guess == 'QUIT':
        print('Good night.')
        condition = True
    elif checkUsed(guess) == False:
        return False
    else:
        count-=1
        for i in range(len(answerList)):
            if answerList[i] == guess:
                displayList[i] = guess
                hit = True
        if hit == False:
            print('Incorrect!')
        print(''.join(displayList))
        print('You have ' + str(count) + ' guesses remaining')
        condition = checkEnd()
    
while condition == False:
    loop()