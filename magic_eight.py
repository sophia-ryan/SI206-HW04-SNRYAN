# Homework Four
# Sophia Ryan, Lauren Zielinski #NAMES
# snryan, laurzie, #UNIQUE NAMES

import random

def userInput():
    answer = input("What is your question? ")
    return answer

list_of_anwsers = ["Reply hazy try again","Ask again later", "Better not tell you now",
"Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no",
"My sources say no", "Outlook not so good", "Very doubtful","It is certain", "It is decidedly so",
"Without a doubt", "yes definitly", "You may rely on it", "as i see it, yes", "Most likey",
"Outlook good", "yes", "signs point to yes"]

def checkInput():
    suffix = "?"
    sorry = "I’m sorry, I can only answer questions."
    randomAnswer = random.choice(list_of_anwsers)
    while True:
        asking_question = userInput()
        if asking_question == "quit" or asking_question == "Quit":
            return False
        elif asking_question.endswith(suffix) != True:
            print(sorry)
        else:
            print(randomAnswer)


checkInput()
