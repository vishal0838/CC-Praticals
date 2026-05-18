print("Welcome to Customer Support Chatbot")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "price":
        print("Bot: Our product price starts from 500 rupees.")

    elif user == "delivery":
        print("Bot: Delivery takes 3 to 5 days.")

    elif user == "refund":
        print("Bot: Refund is available within 7 days.")

    elif user == "contact":
        print("Bot: You can contact us at support@gmail.com")

    elif user == "bye":
        print("Bot: Thank you! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")