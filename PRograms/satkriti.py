import random

def agents_name():
    agents = ["Ammy", "Monica", "Savana", "John", "Leesa"]
    return random.choice(agents)

def input_user_name(user_name):
    return input(f"{user_name}: ")

def greet_user(user_name):
    print(f"Hello, {user_name}! I'm {agents_name()}, your virtual assistant.")
    print("How can I help you? (Type 'bye' to exit)")

def exit_condition(user_input):
    return user_input.lower() in ['bye']

def response_to_words(user_input, user_name):
    if "admissions" in user_input.lower():
        print("Agent: You can find information about admissions on our website.")
    
    elif "courses" in user_input.lower():
        list_courses()

    elif "library" in user_input.lower():
        print("Agent: The library is open from 9 AM to 5 PM on weekdays.")
    
    elif "sports" in user_input.lower():
        print(f"Agent: We have various types of sports, {user_name}! You can join our sports clubs.")
    
    elif "tuition fees" in user_input.lower():
        print("Agent: Tuition fees vary by program. Please check our website for further details.")
    
    elif "appointment" in user_input.lower():
        book_appointment(user_name)
    
    else:
        print(f"Agent: I'm not sure about that, {user_name}, but I can help with other questions!")

def book_appointment(user_name):
    print(f"{user_name}, would you like to book an appointment? (yes/no)")
    response = input()

    if response.lower() == 'yes':
        date = input("Please enter the preferred date (YYYY-MM-DD): ")
        time = input("Please enter the preferred time (HH:MM): ")
        appointment_type = input("What type of appointment would you like to book? ")
        
        print(f"Booking your {appointment_type} appointment on {date} at {time}...")
        print("Your appointment has been successfully booked!")
        print(f"Confirmation: {user_name}, your {appointment_type} appointment is scheduled for {date} at {time}.")
    else:
        print("Okay, let me know if you need anything else!")

def list_courses():
    courses = [
        "Computer Science",
        "Business Administration",
        "Mathematics",
        "Engineering",
        ]

    print("Agent: Here are the courses we offer:")
    for course in courses:
        print(f"- {course}")

def chatbot():
    print("Welcome to the University of Poppleton Chatbot!")
    
    user_name = input("Please enter your name: ")
    
    greet_user(user_name)

    while True:
        user_input = input_user_name(user_name)
    
        if exit_condition(user_input):
            print(f"Goodbye, {user_name}! Have a great day!")
            break

        response_to_words(user_input, user_name)

if __name__ == "__main__":
    chatbot()