import random

def main():
    display_instructions()
    word = correct_word()
    remaining_guesses = 4
    underscores = "_ " * len(word)
    completion = False
    while completion == False:
        guess = game_play(underscores, word, remaining_guesses)
        remaining_guesses = chance(guess, word, remaining_guesses)
        underscores = replace_underscores(underscores, word, guess, remaining_guesses)        
        if guess not in word:
            completion = if_wrong(underscores, word, remaining_guesses)
        else:
            completion = if_right(underscores, word)           
    else:
        print("Press enter to end the game.")

def display_instructions():
    # display the instructions from a file
    instruction_file = open("instructions.txt", "r")
    instructions = instruction_file.read()
    instruction_file.close()
    print(instructions)

def correct_word():
    # randomly select a word from the file
    word_list_file = open("list_of_words.txt", "r")
    word_list_str = word_list_file.read()
    word_list_file.close()
    word_list = word_list_str.splitlines()
    word = random.choice(word_list)
    return word    

def game_play(underscores, word, remaining_guesses):
    # promt player to input a letter
    print("The answer so far is " + underscores)
    guess = input("guess a letter" + "(" + str(remaining_guesses) + " guesses remaining): ")
    guess = guess.lower()
    return guess

def chance(guess, word, remaining_guesses):
    # count the remaining number of chances
    if guess not in word or guess == "":                # or guess == "" is added
        remaining_guesses = remaining_guesses - 1
    else:                                               # if guess in word:
        remaining_guesses = remaining_guesses               #remaining_guesses = remaining_guesses + 1
    return remaining_guesses

def replace_underscores(underscores, word, guess, remaining_guesses):
    # replace the underscores with guesses letter at the correct position, if the guess is correct
    underscores = underscores.split()
    for idx in range(len(word)):
        if word[idx] == guess:
            underscores = underscores[:idx] + [guess] + underscores[idx + 1:]
    underscores = " ".join(underscores)        
    return underscores

def if_wrong(underscores, word, remaining_guesses):
    if remaining_guesses == 0:
        print("Not quite, the correct word was " + word + ". Better luck next time")
        completion = True
    else:
        completion = False
    return completion

def if_right(underscores, word):
        if "_" not in underscores: 
            print("Good job! You found the word " + word)
            completion = True
        else:
            completion = False
        return completion
main()
