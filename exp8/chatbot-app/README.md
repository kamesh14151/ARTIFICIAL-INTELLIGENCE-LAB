# Chatbot Implementation

## 🎯 Aim
To design and implement a simple **chatbot** using Python that interacts with users and responds to basic queries using **rule-based and pattern-matching techniques**.

---

## 📚 Algorithm

1. Start the program
2. Display a **welcome message** to the user
3. Accept **user input**
4. Convert input to **lowercase** for easy matching
5. Check input against **predefined patterns**:
   - If input matches **greeting** → respond with greeting
   - If input matches **known questions** → give predefined response
   - If input contains **keywords** → return suitable answer
6. If no match found → display **default response**
7. Repeat until user types `bye` / `exit` / `quit`
8. **End** the program

---

## 💻 Code

[`exp8/chatbot-app/chat.py`](exp8/chatbot-app/chat.py)

---

## 🖼️ Output

![Chatbot Output](exp8/chatbot-app/chat.png)

---

## 📋 Sample Output

```
Hello! I am a Python Chatbot. Type 'bye' to exit.

You: hi
Bot: Hello!

You: what is your name
Bot: I am a Python chatbot.

You: how are you
Bot: I am fine. Thank you!

You: help me
Bot: Sure! Tell me how I can help you.

You: bye
Bot: Goodbye! Have a nice day.
```

---

## ✅ Result
A simple **chatbot** was successfully developed using Python. The chatbot interacts with the user, processes input, and provides appropriate responses based on **predefined rules and patterns**.
