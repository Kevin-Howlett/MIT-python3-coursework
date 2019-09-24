#Program picks a random word from a txt file named "words.txt"
#and generates an interactive hangman game in which the user must guess letters

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    num=0
    for letter in secretWord:
        if letter not in lettersGuessed:
            num+=1
    if num>0:
        return False
    else:
        return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word=''
    for letter in secretWord:
        if letter in lettersGuessed:
            word+=letter
        else:
            word+='_ '
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    available=''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available+=letter
    return available

secretWord = chooseWord(wordlist).lower()


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!\nI am thinking of a word that is '+str(len(secretWord))+ ' letters long.')
    guessesLeft=8
    lettersGuessed=[]
    while int(guessesLeft)>0:
        if isWordGuessed(secretWord,lettersGuessed)==True:
            print('-------------')
            print('Congratulations, you won!')
            break
        print('-------------')
        print('You have '+str(guessesLeft)+' guesses left.')
        print('Available letters: '+str(getAvailableLetters(lettersGuessed)))
        i=input('Please guess a letter: ')
        if (i in secretWord) and (i in getAvailableLetters(lettersGuessed)):
            lettersGuessed+=i
            print('Good guess: '+str(getGuessedWord(secretWord, lettersGuessed)))
        elif (i not in getAvailableLetters(lettersGuessed)):
            lettersGuessed+=i
            print("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed)))
        elif (i not in secretWord) and (i in getAvailableLetters(lettersGuessed)):
            lettersGuessed+=i
            print('Oops! That letter is not in my word: '+str(getGuessedWord(secretWord, lettersGuessed)))
            guessesLeft-=1
    if guessesLeft==0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was '+str(secretWord))

hangman(secretWord)

