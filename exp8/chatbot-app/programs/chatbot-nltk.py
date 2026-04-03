import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["My name is Python Chatbot.", "You can call me PyBot."]
    ],
    [
        r"how are you ?",
        ["I am doing well.", "I am fine, thank you!"]
    ],
    [
        r"who created you ?",
        ["I was created using Python and NLTK."]
    ],
    [
        r"what can you do ?",
        ["I can chat with you and answer simple questions."]
    ],
    [
        r"(.*) help (.*)",
        ["I will try to help you. Please ask your question."]
    ],
    [
        r"where are you from ?",
        ["I live inside a Python program!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day.", "Bye! See you soon."]
    ]
]

def start_chat():
    print("Hello! I am a Python Chatbot. Type 'bye' to exit.")
    
    # Create the chatbot instance
    chatbot = Chat(pairs, reflections)
    
    # Start conversation
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
