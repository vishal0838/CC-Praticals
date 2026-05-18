def pizza_bot():
    print("🍕 Welcome to PizzaBot! 🍕")
    print("Bot: Hello! How can I help you today? (Type 'menu', 'hours', 'track', or 'bye')\n")
    
    while True:
        # Get input and make it lowercase
        user_input = input("You: ").lower()
        
        # 1. Exit
        if "bye" in user_input or "exit" in user_input:
            print("Bot: Thank you! Have a delicious day! 🍕")
            break
            
        # 2. Greetings
        elif "hi" in user_input or "hello" in user_input:
            print("Bot: Hello! You can ask me for our 'menu', 'hours', or 'track' an order.")
            
        # 3. Menu
        elif "menu" in user_input or "pizza" in user_input:
            print("Bot: Our Menu:\n - Margherita Pizza ($10.99)\n - Pepperoni Pizza ($12.99)\n - Veggie Pizza ($11.99)")
            print("Bot: What would you like to order?")
            
        # 4. Ordering
        elif "margherita" in user_input or "pepperoni" in user_input or "veggie" in user_input:
            print("Bot: 🎉 Order confirmed! Your pizza will arrive in 30 minutes.")
            
        # 5. Tracking
        elif "track" in user_input or "status" in user_input:
            print("Bot: Your order is currently out for delivery with our rider!")
                
        # 6. Hours
        elif "hours" in user_input or "open" in user_input:
            print("Bot: We are open everyday from 11:00 AM to 11:00 PM.")
            
        # 7. Don't understand
        else:
            print("Bot: I'm not sure I understand. Try asking for 'menu' or 'hours'.")
            
        print("-" * 40)

# Run the chatbot
pizza_bot()