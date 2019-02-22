import random

# function to chose a random word
def chooseWord():
    wordsList = []
    # read in file and add to wordsList
    with open('SOWPODS dict.txt', 'r') as f:
        line = f.readline().strip()
        wordsList.append(line)

        while line:
            line = f.readline().strip()
            wordsList.append(line)

    myWord = wordsList[random.randint(0, len(wordsList)-1)]
    return myWord

# ask the user for a guess
def askForGuess():
    letter = input("Guess a letter! ")
    return letter.strip().upper()   

# generate word string
def wordString(word, guessedLetters):
    output = []
    for letter in word:
        if letter in guessedLetters:
            output.append(letter.upper())
        else:
            output.append('_')
    return " ".join(output)    


# main driver
if __name__ == '__main__':
    print ('Welcome to Hangman!')
    word = chooseWord()
    lettersToGuess = set(word)
    correctLetters = set()
    incorrectLetters = set()
    guessesCount = 0

    while (len(lettersToGuess) > 0) and guessesCount < 6:
        guess = askForGuess()
        
        # check if letter has already been guessed
        if guess in correctLetters or guess in incorrectLetters:
            print ("You already guessed that letter.")
            continue

        # if letter is in word    
        if guess in lettersToGuess:
            lettersToGuess.remove(guess)
            correctLetters.add(guess) 
        # if letter is not in word
        else:
            incorrectLetters.add(guess)
            guessesCount += 1

        wordStr = wordString(word, correctLetters)
        print(wordStr)
        print("You have {} guesses left".format(6-guessesCount))

    # tell if won or lost
    if guessesCount < 6:
        print("You win! You guessed the word {}".format(word))
    else:
        print("Sorry, you lose. The word was {}".format(word))




