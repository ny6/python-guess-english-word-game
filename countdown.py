print('\n*********************************************')
print('************** COUNTDOWN ********************')
print('*********************************************\n')

p1 = None
p2 = None
winning_streak = None
p1_score = 0
p2_score = 0
word_asked_by = None
word_guessed_by = None
current_word = None
guessed_word = []
guessed_alphabet = None
max_tries = 10
current_tries = 0

while not winning_streak:
  winning_streak = input('Enter winning streak: ')
  if winning_streak:
    winning_streak = int(winning_streak)

print('\n')

while not p1:
  p1 = input('Player 1 enter your name: ')

print('\n')

while not p2:
  p2 = input('Player 2 enter your name: ')
  if p2.lower() == p1.lower():
    p2 = None

p1 = p1.capitalize()
p2 = p2.capitalize()
word_asked_by = p1
word_guessed_by = p2

print('\n*********************************************')
print(f'Welcome {p1} & {p2}!')
print(f"Let's play COUNTDOWN, first player who wins {winning_streak} games, will be winner!")
print('*********************************************\n')

while p1_score < winning_streak and p2_score < winning_streak:
  while not current_word:
    print('\n*********************************************')
    print(f'{p1} score: {p1_score}')
    print(f'{p2} score: {p2_score}')
    print(f'Winning streak: {winning_streak}')
    print('*********************************************\n')
    current_word = input(f'{word_asked_by} enter your word: ')
    if current_word:
      current_word = [x.lower() for x in current_word]
      guessed_word = ['' for x in current_word]

  print('*********************************************\n' * 50)

  while current_word != guessed_word and current_tries < max_tries:
    guessed_alphabet = input(f'{word_guessed_by}, enter your guess: ')
    if guessed_alphabet in current_word:
      i = current_word.index(guessed_alphabet.lower())
      guessed_word[i] = guessed_alphabet
      print(f'\nYou guessed it right! {guessed_word}')
    else:
      current_tries += 1
      print(f'Wrong! pending tries: {max_tries - current_tries}')

  if current_word == guessed_word:
    if word_guessed_by == p1:
      p1_score += 1
    else:
      p2_score += 1

  if word_guessed_by == p1:
    word_asked_by = p1
    word_guessed_by = p2
  else:
    word_asked_by = p2
    word_guessed_by = p1

  current_tries = 0
  current_word = []
  guessed_word = []


print('*********************************************\n')
if p1_score == winning_streak:
  print(f'{p1} wins!')

if p2_score == winning_streak:
  print(f'{p2} wins!')
