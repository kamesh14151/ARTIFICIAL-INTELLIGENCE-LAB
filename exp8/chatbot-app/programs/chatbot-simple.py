import random

greetings = ["hello", "hi", "hey"]
greet_responses = ["Hello!", "Hi there!", "Hey! How can I help you?"]

questions = {
    "name": ["I am a Python AI chatbot.", "You can call me PyBot."],
    "how are you": ["I am fine!", "Doing great!"],
    "creator": ["I was created using Python."],
    "help": ["Sure! Tell me how I can help you."]
}

print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("AI Chatbot: Goodbye! Have a nice day.")
        break

    elif user in greetings:
        print("AI Chatbot:", random.choice(greet_responses))

    else:
        found = False
        for key in questions:
            if key in user:
                print("AI Chatbot:", random.choice(questions[key]))
                found = True
                break

        if not found:
            print("AI Chatbot: Sorry, I don't understand. Can you ask something else?")
