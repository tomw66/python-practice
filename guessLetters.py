# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:36:03 2022

@author: Tom
 For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
"""
answerWord = 'ATONE'
answerList = list(answerWord)
displayList =  ['_ '] * len(answerList)
usedLetters = []
count = 0
condition = False

print('Welcome to hangman!')
print(''.join(displayList))


def checkEnd():
    if '_ ' not in displayList:
        print('Well done!')
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
    hit = False
    guess = str(input('Guess a letter: ')).upper()
    if checkUsed(guess) == False:
        return False
    else:
        #print(guess)
        for i in range(len(answerList)):
            #print(answerList,i,  guess)
            if answerList[i] == guess:
                displayList[i] = guess
                hit = True
        if hit == False:
            print('Incorrect!')
        #count+=1
        print(''.join(displayList))
        global condition
        condition = checkEnd()
    
while condition == False:
    loop()
    
