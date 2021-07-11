from random import choice
def word_generator():
    word_list = ["python","abacus","java","spyder","jupyter",]
    return choice(word_list)

word = word_generator()
guessed = ""
turns = int(len(word)*1.5)



while (True):
    print(" You're left with {} turns".format(turns))
    inp = input("\nMake a guess : ")
    turns -= 1
    if inp in word:
        guessed = guessed + inp
    unguessed_char = 0
    for i in word:
        if i in guessed:
            print(i,end="")
        else:
            unguessed_char += 1
            print("*",end="")
    if unguessed_char == 0:
        print("\nHurray!! You Won...!")
        break
    if turns == 0:
        print("\nOops! You ran out of attempts.")
        break

