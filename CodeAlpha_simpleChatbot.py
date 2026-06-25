def get_reply(msg):
    msg = msg.lower().strip()

    if "hello" in msg or "hi" in msg or "hey" in msg:
        return "Hey there! 👋 Nice to meet you!"

    elif "how are you" in msg or "hows it" in msg:
        return "I'm just code, but I feel GREAT! 😄"

    elif "joke" in msg:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"

    elif "your name" in msg or "who are you" in msg:
        return "I'm ByteBot — made of if-elif and dreams. 🤖"

    elif "thanks" in msg or "thank you" in msg:
        return "You're welcome! 😊"

    elif "bye" in msg or "goodbye" in msg:
        return "Goodbye! It was fun chatting. 👋"

    else:
        return "Hmm, I didn't get that 🤔 Try: hello, how are you, joke, bye"


print("\n🤖 ByteBot is online! (type 'bye' to exit)\n")

while True:
    user = input("You: ").strip()

    if not user:
        continue

    reply = get_reply(user)
    print(f"Bot: {reply}\n")

    if "bye" in user.lower() or "goodbye" in user.lower():
        break
