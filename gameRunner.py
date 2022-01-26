import csv
import random

def evaluateGuess(answer, guess):
        #add check for len==5
            
        #add check for word is valid
        
        evaluatedGuess = {0: 'white', 1: 'white', 2: 'white', 3: 'white', 4: 'white'}
        answerChars = list(answer)

        #evaluate Greens and Blacks
        for i in range(0,5): 
            if answer[i] == guess[i]:
                evaluatedGuess[i] = 'green'
                answerChars.remove(guess[i])
            elif guess[i] not in answerChars:
                evaluatedGuess[i] = 'black'

        #evaluate Yellows
        for i in range(0,5):
                    #go to next if already evaluated this character
                    if evaluatedGuess[i] != 'white':
                        continue
                    
                    if guess[i] in answerChars:
                        evaluatedGuess[i] = 'yellow'
                        answerChars.remove(guess[i])

                    #duplicate of previous correct guess  
                    else:
                        evaluatedGuess[i] = 'black'
     
        return evaluatedGuess 
     
     
        
with open('words.csv') as file:

        #Create Dict
        reader = csv.reader(file)
        wordsDict = dict()
        count = 0
        for row in reader:
                wordsDict[count] = row
                count = count + 1


        #Pick Word
        chosenEntryNumber = random.randint(0, len(wordsDict)-1)
        answer = wordsDict[chosenEntryNumber]

        print("actual answer" , answer)

        #Setup Game
        guesses = dict()
        numAllowedGuesses = 6
        
        print('''
        Welcome to The Guessing Game
        ---------------------------

        ''')
        
        for i in range(1, numAllowedGuesses + 1):
            print("Guess ", i)
            guess = str(input("Enter your guess:"))
            guesses[i] = guess
            result = evaluateGuess(answer[0], guess)
            print("Result for guess: ", guess)
            print(result)

