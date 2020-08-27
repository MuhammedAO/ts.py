# the basic idea is that we'll have a secret word that we store inside of our program and then the user will interact with the program to try and guess the secret word

# we want the user to be able to keep guessing what secret word is until they get the secret word.

# create a variable that will store the user's response => guess
# we need to be able to prompt the user to input the secret word but the catch is, if they don't get the secret word, we promt them to enter it again and again.
# remember while loop? we can use it to continously ask the person to guess the word until they guess it correctly.

secret_word = "fantabulous"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
# while guess != secret_word:
#   guess = input("Enter guess: ")


# print("You win!")

# improve the game => set limit for number of trials
# now we need to keep track of how many times the user has guessed
# everytime the loop runs, we want to increase the guess count.
# if outofguesses = true, you've lost the game
#after oog = true (else), first thing to do is when i go through this loop, check if the player hasn't already used up his/her guesses

# the "not" keyword is a logical operator. the return value will be true if the statements are not true.. otherwise it will return false. out_of_guesses is false so 'not' operator evaluated as True

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# when we break out of this loop, there's going to be 2 possible scenarios. it's either the user guess the word correctly or the runs out of guesses

if out_of_guesses:
    print("You're out of guesses! You lost the game")
else:
    print("You Win!")
