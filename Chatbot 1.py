import re

# Function to ensure proper grammar in the response
def format_response(response):
    response = response.strip()
    if not response.endswith(('.', '!', '?')):  # Ensure proper punctuation
        response += '.'
    return response.capitalize()  # Capitalize the first letter


# Bunny ASCII Art
bunny = r"""
             (\(\  
       („• ֊ •„)<(Hello...)
        ━O━O━━━━━
"""

import random

ascii_art = [r"""(\(\  
       („• ֊ •„)<(Hello...)
        ━O━O━━━━━""" ,r"""‎             
                                       /;    ;\
                                   __  \\____//
                                  /{_\_/   `'\____
                                  \___   (o)  (o  }
       _____________________________/          :--'  
   ,-,'`@@@@@@@@       @@@@@@         \_    `__\
  ;:(  @@@@@@@@@        @@@             \___(o'o)
  :: )  @@@@          @@@@@@        ,'@@(  `===='       
  :: : @@@@@:          @@@@         `@@@:
  :: \  @@@@@:       @@@@@@@)    (  '@@@'
  ;; /\      /`,    @@@@@@@@@\   :@@@@@)
  ::/  )    {_----------------:  :~`,~~;
 ;;'`; :   )                  :  / `; ;
;;;; : :   ;                  :  ;  ; :              
`'`' / :  :                   :  :  : :
    )_ \__;      ";"          :_ ;  \_\       `,','
    :__\  \    * `,'*         \  \  :  \   *  8`;'*  *
        `^'     \ :/           `^'  `-^-'   \v/ :  \/ """, r"""    
    /\_____/\
        /  o   o  \
       ( ==  ^  == )
        )         (
       (           )
      ( (  )   (  ) )
     (__(__)___(__)__)""", r"""  ‎    
    __
___( o)>
\ <_. )
 `---' """, r"""‎    
 ⠀⠀⠀⠠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣴⣿⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣧⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⢀⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠹⣿⣿⣿⣷⣦⣄⡀⣿⣱⡀⠀⠀⠀⠀⠀⠀⢸⢿⣧⣠⣴⣾⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠛⢷⣿⣟⡿⠿⠿⡟⣓⣒⣛⡛⡛⢟⣛⡛⠟⠿⣻⢿⣿⣻⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⢻⡭⠖⡉⠥⣈⠀⣐⠂⡄⠔⢂⢦⡹⢬⡕⠊⠳⠈⢿⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣼⣷⣋⠲⢮⣁⠀⣐⠆⡤⢊⣜⡀⡾⣀⠀⢠⢻⣌⣤⣥⣓⣌⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣟⣽⢳⣯⣝⣦⡀⠓⡤⢆⠇⠂⠄⠤⡝⣂⠋⠖⢋⠀⣡⣶⣾⡿⡷⣽⡿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡜⢯⣿⣿⣿⣷⣿⣤⣧⣶⣬⣝⣃⣓⣈⣥⣶⣿⣾⣿⣿⢣⠇⢻⡞⣯⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣼⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡔⡯⢧⢟⣟⣱⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡼⡼⢁⡌⢼⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢇⡼⢃⡿⣼⣛⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠟⣡⣫⣢⢏⣼⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡾⢕⣻⣽⣵⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣮⣿⡼⢭⡟⠳⠞⡖⢛⣶⣷⣯⡶⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠛⠛⠿⠟⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀""", r"""    ‎       
             _____
                   .d88888888bo.
                 .d8888888888888b.
                 8888888888888888b
                 888888888888888888
                 888888888888888888
                  Y8888888888888888
            ,od888888888888888888P
         .'`Y8P'```'Y8888888888P'
       .'_   `  _     'Y88888888b
      /  _`    _ `      Y88888888b   ____
   _  | /  \  /  \      8888888888.d888888b.
  d8b | | /|  | /|      8888888888d8888888888b
 8888_\ \_|/  \_|/      d888888888888888888888b
 .Y8P  `'-.            d88888888888888888888888
/          `          `      `Y8888888888888888
|                        __    888888888888888P
 \                       / `   dPY8888888888P'
  '._                  .'     .'  `Y888888P`
     `"'-.,__    ___.-'    .-'
    jgs  `-._````  __..--'`
             ``````""", r"""   ‎    
                    
        .--'''''''''--.
     .'      .---.      '.
    /    .-----------.    \
   /        .-----.        \
   |       .-.   .-.       |
   |      /   \ /   \      |
    \    | .-. | .-. |    /
     '-._| | | | | | |_.-'
         | '-' | '-' |
          \___/ \___/
       _.-'  /   \  `-._
     .' _.--|     |--._ '.
     ' _...-|     |-..._ '
            |     |
            '.___.'
              | |
             _| |_
            /\( )/\
           /  ` '  \
          | |     | |
          '-'     '-'
          | |     | |
          | |     | |
          | |-----| |
       .`/  |     | |/`.
       |    |     |    |
       '._.'| .-. |'._.'
             \ | /
             | | |
             | | |
             | | |
            /| | |\
          .'_| | |_`.
          `. | | | .'
       .    /  |  \    .
      /o`.-'  / \  `-.`o\
     /o  o\ .'   `. /o  o\
     `.___.'       `.___.' """]

def Graffiti():
    return random.choice(ascii_art)

def roll_dice():
    return random.randint(1, 6)

# Function to perform the gamble (rolling the dice)
def Gamble(roll_count):

    roll_count = 1 
    # Calculate the jackpot probability based on roll_count
    jackpot_probability = min(0.05 + (roll_count - 1) * 0.02, 1.0)

    # Roll three random numbers between 1 and 9
    roll1 = random.randint(1, 9)
    roll2 = random.randint(1, 9)
    roll3 = random.randint(1, 9)


    # Check if the rolls are a jackpot (all three numbers are the same)
    if random.random() < jackpot_probability:
        roll_count = 1  # Set jackpot_hit to True if all three rolls are the same
        return f"Jackpot! {roll1}, {roll1}, {roll1}!"
    
     # Check if the jackpot was already hit
    else :
        roll_count += 1  # Increment roll count for the next roll
    return f"Rolls: {roll1}, {roll2}, {roll3}"
     # If no jackpot, return the rolls
    





# Function to generate the chatbot's response
def chatbot_response(user_input, roll_count, last_response=None):
    responses = {
        "hi": "Hi",
        "bye": "Goodbye",
        "how are you": "I'm good, thanks for asking!",
        "bunny": bunny,  # Responds with the bunny ASCII art when the user types "bunny"
        "roll dice": f"The dice rolled a {roll_dice()}!!",
        "ascii art": f"{Graffiti()}",
        "gamble": f"{Gamble(roll_count)}", 
        "inputs": r"""hi, bye, how are you, bunny, roll dice, ascii art, gamble, what can you do""", 
    }

    
   



    

    # Check if the user input is a math expression
    math_pattern = r'(-?\d+(\.\d+)?)\s*([+\-*/])\s*(-?\d+(\.\d+)?)'
    match = re.search(math_pattern, user_input.strip())
   
    if match:
        # Extract the operands and operator
        operand1 = float(match.group(1))  # First number
        operator = match.group(3)         # Operator (+, -, *, /)
        operand2 = float(match.group(4))  # Second number


        # Perform the calculation based on the operator
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            if operand2 == 0:
                return "Sorry, I can't divide by zero."
            result = operand1 / operand2


        # Return the result as a string
        return f"The result is {result}"


    if re.search(r'\bwhat\b', user_input.lower()):
        if last_response:
            return f"I said, {last_response}"  # Repeat last response if available
        else:
            return "I don't have a previous response to repeat."  # No previous response
   
    # Check for predefined responses
    for pattern, response in responses.items():
        if re.search(pattern, user_input.lower()):
            return response
       
    # Default response if no match found
    return "Sorry, I didn't understand that."


# Function to display the message with the sender label
def display_message(message, sender="User"):
    # Print the message with the sender's label in one line
    print(f"{sender}: {message}")


# Print the title
print("Welcome to ChatBOTT! How can I assist you today?\n")

last_response = None
roll_count = 1 

# Start an interactive loop for the chatbot
while True:
    user_input = input("You: ")  # Take input from the user
    if user_input.lower() == "bye":  # Check if the user says 'bye' to end the conversation
        display_message("Goodbye! Have a great day!", sender="Pandora")
        break
   # If user asks to roll three numbers, increase roll count and check for jackpot
   
   
   
    # Get the chatbot's response
    response = chatbot_response(user_input, roll_count, last_response)
   
    # Format the response to ensure proper grammar
    formatted_response = format_response(response)
   
    # Store the last response for possible future repetition
    last_response = formatted_response
   
    # Display the chatbot's response
    display_message(formatted_response, sender="Pandora")
