import csv
import random

def evaluateGuess(answer, guess, wordsDict):
        if len(guess) != 5:
            return {0: 'Guess must be 5 letters long. \n'}

        if guess not in wordsDict.values():
            return {0: 'Not a valid word. \n'}
        
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
                wordsDict[count] = row[0]
                count = count + 1


        #Pick Word
        chosenEntryNumber = random.randint(0, len(wordsDict)-1)
        answer = wordsDict[chosenEntryNumber]

        print("actual answer", answer)

        #Setup Game
        guesses = dict()
        numAllowedGuesses = 6
        hasWon = False
        print('''
        Welcome to The Guessing Game
        ---------------------------


        ''')
        
        for i in range(1, numAllowedGuesses + 1):
            print("Guess ", i)
            guess = str(input("Enter your guess: \n"))
            guesses[i] = guess
            result = evaluateGuess(answer, guess, wordsDict)

            #Handle Error scenarios
            while len(result) != 5:
                print("Error: ", result[0])
                guess = str(input("Try Again: \n"))
                result = evaluateGuess(answer, guess, wordsDict)

            listValues = result.values()
            if all(element == 'green' for element in listValues):
                hasWon = True
                print('''
                You won !!
                The answer was:
                ''', answer)
                break
            print("Result for guess: ", guess)
            print(result, "\n")

        if hasWon == False:
            print('''
            Sorry, you lost.
            The answer was:
            ''', answer)


