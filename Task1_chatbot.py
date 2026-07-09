print("🤖 CodSoft ChatBot: Hi! Mai tumhara assistant hu. 'bye' likh kar exit kar sakte ho")

while True:
    user_input = input("You: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! Kaise madad kar sakta hu?")
    elif "how are you" in user_input:
        print("Bot: Mai badhiya hu! Tum sunao?")
    elif "name" in user_input:
        print("Bot: Mera naam CodSoft Bot hai")
    elif "help" in user_input:
        print("Bot: Mai basic sawaalon ka jawab de sakta hu. Try karo: hello, help, name, bye")
    elif "bye" in user_input:
        print("Bot: Bye! Phir milte hain")
        break
    else:
        print("Bot: Sorry, mai ye samjha nahi. 'help' likh kar options dekho")
