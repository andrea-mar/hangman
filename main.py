'''
Hangman game

secret word chosen at radom from a list of strings

secret word can be any length

show the user how many letters in the secret word  by printing _ for each letter, all on one line

prompt the user for a letter - assume the user inputs only one lower case letter

ex for secret word 'table':
Input: 
  You have 5 guesses
  _ _ _ _ _ 
  letter: v

Output (if letter not in the secret word):
  Letter not in the word
  You have 4 guesses left
  _ _ _ _ _
  letter: a (user input)

Output if letter in the secret word:
  _ a _ _ _
  letter:

decrease number of guesses only if the letter guessed is not in the word

end game if guesses = 0 or if user guessed all the letters in the word

Output if user guesses all letters:
  Correct!
Output is user doesn t guess and runs out of guesses:
  The word was: table
'''


from random import choice

def main(): 
    words = ["fuzzy", "sheep", "table"]

    word_to_guess = choice(words)
    #print(word_to_guess)
    max_guesses = 5
    guessed_so_far = ['_'] * len(word_to_guess)

    pattern = r''
    print('You have ' + str(max_guesses) + ' guesses')
    print(*guessed_so_far)
    # for i in word_to_guess:
    #   print('_', end=' ')
    # print()

    while max_guesses != 0 and '_' in guessed_so_far:
        guess = input('letter: ')       
        
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_so_far[i] = guess 
        else:
            max_guesses = max_guesses - 1
            print('Letter not in the word')
            print('You have ' + str(max_guesses) + ' guesses left')

        print(*guessed_so_far)
        # for i in guessed_so_far:
        #   print(i, end=' ')
        # print()

    if '_' in guessed_so_far:
        print("the word was: " + word_to_guess)
    else:
        print('Correct!')


if __name__ == '__main__':
    main()