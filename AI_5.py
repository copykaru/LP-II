def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")
    print("Please, remind me your name.")

def remind_name():
    name = input()
    print(f"What a great name you have, {name}!")

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

def count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input())
    for i in range(num + 1):
        print(f"{i}!")

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    while True:
        answer = int(input())
        if answer == 2:
            break
        else:
            print("Please, try again.")

def end():
    print("Congratulations, have a nice day!")

# Start Chatbot
greet('TE-Chatbot', '2022')
remind_name()
guess_age()
count()
test()
end()


       #OR


# Importing necessary modules  
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer 
 
# Creating a new chatbot instance named 'PyBot' 
my_bot = ChatBot( 
    name='PyBot', 
    read_only=True, 
    logic_adapters=[ 
        'chatterbot.logic.MathematicalEvaluation', 
        'chatterbot.logic.BestMatch' 
    ] 
) 
 
# Training data for small talk 
small_talk = [ 
    'hi there!', 
    'hi!', 
    'how do you do?', 
    'how are you?', 
    'i\'m cool.', 
    'fine, you?', 
    'always cool.', 
    'i\'m ok', 
    'glad to hear that.', 
    'i\'m fine', 
    'glad to hear that.', 
    'i feel awesome', 
    'excellent, glad to hear that.', 
    'not so good', 
    'sorry to hear that.', 
    'what\'s your name?', 
    'i\'m pybot. ask me a math question, please.' 
] 
 
# Training data for mathematical concepts 
math_talk_1 = [ 
    'pythagorean theorem', 
    'a squared plus b squared equals c squared.' 
] 
 
math_talk_2 = [ 
    'law of cosines', 
    'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)' 
] 
 
# Combine all the conversations 
training_data = small_talk + math_talk_1 + math_talk_2 
 
# Training the chatbot with the data 
trainer = ListTrainer(my_bot) 
trainer.train(training_data) 
 
# Function to start the chatbot interaction 
def chatbot(): 
    print("Hello! I am PyBot. Type 'bye' to exit.") 
    while True: 
        user_input = input("You: ") 
        if user_input.lower() == 'bye': 
            print("PyBot: Goodbye! Have a great day!") 
            break 
        response = my_bot.get_response(user_input) 
        print(f"PyBot: {response}") 
 
# Run the chatbot 
if __name__ == "__main__": 
    chatbot()
