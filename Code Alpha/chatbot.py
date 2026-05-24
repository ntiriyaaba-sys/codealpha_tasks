import random
greetings = ["Hi there!","Hello friend!","Nice to meet you!"]

while True:
    user_input = input('You: ').lower()
    if  user_input in ['hello','hi','hey']:
        print(f'Bot:{random.choice(greetings)} I am AlphaBot')  
    elif user_input == 'How are you'.lower():
        print("Bot: I'm doing great")
    elif user_input == 'bye':
        print('Bot: Goodbye!')
    else:
        print("Bot: I don't understand that yet.")
        