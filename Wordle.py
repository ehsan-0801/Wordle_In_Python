import random
guessed_correctly = False

def word_list():
    word_list = []
    word_file = open('5_letter_word.txt')
    for word in word_file:
        word_list.append(word.strip())
    print(word_list)
    return word_list

# word_list = word_list()

def random_word(words):
    random_word = random.choice(words)
    return random_word


def is_real_word(Guessword, word_list):
    return Guessword in word_list

def check_guess(guessed_word, exact_word):
    global guessed_correctly
    position = 0
    clue =""
    repeatedletter = ""
    for letter in guessed_word:
        
        # is in the right position X
        # is in the word (n2<=n1) O
        # if not found in the word or repeated (n2>n1) _        
        
        
        # TAAAN
        # AARAT
        # OX_XO
        
        if letter == exact_word[position]:
            clue += "X"
            repeatedletter += letter
        elif letter in exact_word and repeatedletter.count(letter) < exact_word.count(letter):
            clue += "O"
            repeatedletter += letter
        else:
            clue += "_"
        
        position+=1
    print(clue)
    return clue == "XXXXX"


def next_guess(word_list):
    guess = input("Please enter a guess:").lower()
    if is_real_word(guess, word_list):
        return guess
    else:
        print("That's not a real word!")
        return next_guess(word_list)

def play():
    global guessed_correctly
    word_list = []
    guess_count = 0
    word_file = open('5_letter_word.txt')
    for word in word_file:
        word_list.append(word.strip())
    exact_word = random_word(word_list)
    print(exact_word)
    while guess_count < 5 and  not guessed_correctly:
        if(check_guess(next_guess(word_list), exact_word)):
           guessed_correctly = True
           break
        guess_count+=1
   
    if guessed_correctly:
        print("You Won")
    else:
        print("The word was: ",exact_word)
        print("You Lost")

play()
