import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

def ask_question(index, question, options):
  print(f'Question {index}: {question}')
  for option in options:
    print(option)

  return input('Your answer: ').upper().strip()  

def run_quiz(quiz):
  random.shuffle(quiz)

  score = 0

  for index, item in enumerate(quiz, 1):
    answer = ask_question(index, item[QUESTION], item[OPTIONS])

    if answer == item[ANSWER]:
      cprint('Correct!', 'green')
      score += 1
    else:
      cprint(f'Wrong! The correct answer is {item[ANSWER]}', 'red')
    
    print()

  print(f'Quiz over! Your final score is {score} out of {len(quiz)}')


def main():  
  quiz = [
    {
      QUESTION: 'Who was the last prophet in islam?',
      OPTIONS: ['A. Musa', 'B. Isa', 'C. Mohammad', 'D. Yusuf'],
      ANSWER: 'C'
    },
    {
      QUESTION: 'Which prophet could control the jin?',
      OPTIONS: ['A. Nooh', 'B. Sulaiman', 'C. Musa', 'D. muhammad'],
      ANSWER: 'B'
    },
    {
      QUESTION: 'Which prophet built the first boat?',
      OPTIONS: ['A. Adam', 'B. Harun', 'C. Isa', 'D. Nooh'],
      ANSWER: 'D'
    }
  ]  
  run_quiz(quiz)

if __name__ == '__main__':
  main()