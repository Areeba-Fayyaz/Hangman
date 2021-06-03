import guess as g
import countdown as co
import random
with open("words.txt") as f:
    word_list=f.readlines()
    v=random.choice(word_list)
    c=v.split()
    secret_word=random.choice(c)
print('loading wordlist form file.... \n 55900 words loaded')
print('welcome to the game hangman!')
print("Instructions: \n 1)you have three warnings and 6 guesses \n \
2) On every wrong guess you have to lose guesses.\n\
3) If the  wrong guess is vowel then 2 guesses are lost otherwise 1 guess is lost \n\
4) If the guessed letter is not among available letter then 1 warning is lost\n\
5) you have to guess the word within 1min or 60 seconds")
print(f'\nI am thinking of a word that is {len(secret_word)} letters long')
v=''
for i in secret_word:
    if secret_word.count(i)==1:
        v+=i
unique=len(v)
co.count_down(3)
g.get_guess(secret_word,unique)

        
