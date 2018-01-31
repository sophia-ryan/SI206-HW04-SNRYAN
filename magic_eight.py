# Homework Four
# Sophia Ryan, Lauren Zielinski #NAMES
# snryan, laurzie, #UNIQUE NAMES

import random

def userInput():
    answer = input("What is your question?")
    return answer

 list_of_questions = ["Reply hazy try again","Ask again later", "Better not tell you now",
 "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no",
 "My sources say no", "Outlook not so good", "Very doubtful","It is certain", "It is decidedly so",
 "Without a doubt", "yes definitly", "You may rely on it", "as i see it, yes", "Most likey",
 "Outlook good", "yes", "signs point to yes"]

def checkInput():
    input = userInput()
    suffix = "?"
    sorry = “I’m sorry, I can only answer questions.”
    randomAnswer = random.choice(list_of_questions)
    while input != "quit" or "Quit":
        if input.endswith(suffix) != true:
            print(sorry)
        else:
            return randomAnswer
