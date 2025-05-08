# Help Desk Management System - Simple Expert System
# Dictionary of problems and solutions
problem_dict = {
    "Printer not working": "Check that it's turned on and connected to the network.",
    "Can't log in": "Make sure you're using the correct username and password.",
    "Software not installing": "Check that your computer meets the system requirements.",
    "Internet connection not working": "Restart your modem or router.",
    "Email not sending": "Check that you're using the correct email server settings."
}

# Function to handle user input
def handle_request(user_input):
    if user_input.lower() == "exit":
        return "Goodbye!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "I'm sorry, I don't know how to help with that problem."

# Main loop
while True:
    user_input = input("What's the problem? Type 'exit' to quit. ")
    response = handle_request(user_input)
    print(response)
    if user_input.lower() == "exit":
        break
