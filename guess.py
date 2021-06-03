import dashes as d
def get_guess(secret_word,unique):
    import time as t
    dashes = "-" * len(secret_word)
    guesses_left = 6
    warnings=3
    letters='a b c d e f g h i j k l  m n o p q r s t u v w x y z'
    c=letters.split()
    z=0
    while guesses_left > 0 and not dashes == secret_word:
        x=t.perf_counter()
        print('Available letters:',letters)
        print(dashes)
        print ('Guesses left: ',guesses_left)
        guess = input("Guess:")
        y=t.perf_counter()
        z+=(y-x)
        if z>60.0:
            print('you run out of time')
            break
        guess = guess.lower()
        if len(guess) != 1 or guess not in letters:
            if warnings>0:
                warnings-=1
            print (f'You have {warnings} warnings left')
        elif guess in secret_word:
            print ("That letter is in the secret word!")
            dashes = d.update_dashes(secret_word,dashes,guess)
            c.remove(guess)
            space=''
            letters=space.join(c)
        else:
            print ("That letter is not in the secret word!")
            if guess not in 'aeiou':
                guesses_left -= 1
                c.remove(guess)
                space=''
                letters=space.join(c)
            elif guess in 'aeiou':
                guesses_left-=2
                c.remove(guess)
                space=''
                letters=space.join(c)
        if warnings<1:
            guesses_left-=1
    if guesses_left < 1 or z>60.0:
        print ("You lose. The word was: " + str(secret_word))
    else:
        print ("Congrats! You win. The word was: " + str(secret_word))
        print("your score is :",unique*guesses_left)
        
