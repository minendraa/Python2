import json
import random
import logging


logging.basicConfig(filename='chat_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

try:
    with open('response.json') as f:
        responses = json.load(f)
except Exception as e:
    logging.error(f"Error loading JSON: {e}")
    print("Error loading response data. Please check 'response.json'.")
    exit()


def start_chat():
    print("This is the University of Poppleton chatbot.")
    user_name = input("Your name: ").strip()  
    agent_name = random.choice(["Hailey", "Tony", "Hena"])  
    print(f"{agent_name}: Hi {user_name}! How can I help?")


    while True:
        user_input = input(f"{user_name}: ") 
        if user_input in ['bye', 'exit', 'quit']:  
            print(f"{agent_name}: Goodbye {user_name}!")
            break

        answer = random.choice(responses['random_responses'])
        for word in user_input.split():
            if word in responses['conversation']:
                answer = responses['conversation'][word]
                break  

        print(f"{agent_name}: {answer}")

        if random.random() < 0.1:  
            print(f"{agent_name}: Oops, I got disconnected")
            break

if _name_ == "_main_":
    start_chat()