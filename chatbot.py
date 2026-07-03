from datetime import datetime

print("=" * 55)
print("🤖 ADVANCED AI CHATBOT")
print("Developed by: Raghavendra Lankelapalli")
print("Type 'help' to see commands.")
print("Type 'bye' to exit.")
print("=" * 55)

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! Welcome to the Advanced AI Chatbot.")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: I'm an Advanced AI Chatbot.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language used in AI, web development, automation, and data science.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence, where computers perform tasks that normally require human intelligence.")

    elif user == "what is flask":
        print("Bot: Flask is a lightweight Python web framework.")

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif user == "joke":
        print("Bot: Why did the Python developer wear glasses? Because they couldn't C.")

    elif user == "motivate me":
        print("Bot: Success comes from consistent practice.")

    elif user == "help":
        print("""
Available commands:
- hello
- how are you
- what is your name
- what is python
- what is ai
- what is flask
- date
- time
- joke
- motivate me
- help
- bye
""")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")
