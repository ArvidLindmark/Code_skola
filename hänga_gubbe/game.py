guesses = []
word_guess_state = []
game = True
win = False
empty_space = " \n" * 100
letter_state = False
lives = -1
lifeline = [
r"""
 ♥ ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥
      O
     /|\
     / \
""",
r"""
      
      O
     /|\
     / \
"""
]


print(f"Spelare 1 väljer ett ord, Spelare 2 har 6 försök på sig att gissa rätt")

word = str(input(f"Spelare 1 skriv in ordet: "))
word = list(word)
print(word)

print(empty_space)
wordlenght = len(word)
word_guess_state = ["_"] * wordlenght
print(f"Ordet är {wordlenght} bokstäver långt")
print(word_guess_state)

while game == True:
    current_pos = 0 

    guess = str(input(f"Gissa en bokstav: "))
    guesses.append(guess)

    for letter in word:     
        if guess == letter and word_guess_state[current_pos] != letter:
            word_guess_state[current_pos] = letter
            print("Bokstaven är rätt")
            letter_state = True
            print(word_guess_state)
        current_pos += 1

    if letter_state == False:
        lives += 1
        print("bokstaven är fel")
        print(lifeline[lives])
        print(word_guess_state)

    elif letter_state == True:
          word_guess_state = " ".join(word_guess_state)
          word = " ".join(word)
          if word_guess_state == word:
              win = True
          else:
               word_guess_state = word_guess_state.split()
               word = word.split()
               letter_state = False

    if lives == 6:
        print(lifeline[lives])
        print("Du förlorade")
        break
    elif win == True:
        print("Du vann")
        break