import datetime
import random

RESPONSES = {
    "hello"         : ["Hello! I am ARIA. How can I help you today?",
                       "Hey there! ARIA here. What's on your mind?",
                       "Hi! What can I do for you?"],

    "hi"            : ["Hi! I am ARIA, your AI assistant.",
                       "Hey! How are you doing today?",
                       "Hello! Ready to chat."],

    "hey"           : ["Hey! What can I help you with?",
                       "Hey there! ARIA is listening.",
                       "Hi! What's up?"],

    "good morning"  : ["Good morning! Hope you have a wonderful day ahead!",
                       "Morning! ARIA is ready to assist you."],

    "good afternoon": ["Good afternoon! How can I assist you?",
                       "Afternoon! What can I do for you today?"],

    "good evening"  : ["Good evening! How was your day?",
                       "Good evening! ARIA is here to help."],

    "good night"    : ["Good night! Sweet dreams.",
                       "Good night! See you next time."],

    "how are you"   : ["I am just a program, but I am running perfectly!",
                       "All systems operational. Thanks for asking.",
                       "I am great! Ready to assist you anytime."],

    "how r u"       : ["Running at 100%. How about you?",
                       "All good on my end! What about you?"],

    "who are you"   : ["I am ARIA, Artificial Rule-based Intelligence Assistant, "
                       "built by a DecodeLabs AI Intern.",
                       "I am ARIA, a rule-based chatbot. I work using "
                       "programmatic logic, not machine learning."],

    "what are you"  : ["I am a Rule-Based AI Chatbot. I use dictionaries "
                       "and keyword matching to respond.",
                       "I am ARIA, a deterministic AI. Every response I give "
                       "is 100% predictable and traceable."],

    "your name"     : ["My name is ARIA, Artificial Rule-based Intelligence Assistant.",
                       "They call me ARIA. Nice to meet you."],

    "what is ai"    : ["AI stands for Artificial Intelligence. It is the ability "
                       "of a machine to simulate human thinking and decision-making.",
                       "Artificial Intelligence means teaching machines to think. "
                       "There are two types: Rule-Based like me, and ML-Based like ChatGPT."],

    "what is rule based" : ["A rule-based AI follows strict dictionary rules. "
                             "Every output is predictable. I am a great example of this.",
                             "Rule-based AI has zero hallucination risk. "
                             "Every response is hard-coded and traceable."],

    "machine learning"   : ["Machine Learning is when AI learns from data automatically. "
                             "Unlike me, I follow fixed rules defined by my creator.",
                             "ML trains on data to find patterns. "
                             "I am the opposite, pure logic and rules."],

    "time"          : ["__TIME__"],
    "date"          : ["__DATE__"],
    "today"         : ["__DATE__"],
    "what day"      : ["__DATE__"],
    "help"          : ["__HELP__"],

    "joke"          : ["Why do programmers prefer dark mode? Because light attracts bugs.",
                       "Why did the AI break up with the algorithm? Too many issues to resolve.",
                       "How many programmers does it take to change a light bulb? "
                       "None, that is a hardware problem.",
                       "Why do Python programmers wear glasses? Because they cannot C."],

    "funny"         : ["Why did the chatbot go to school? To improve its natural language processing.",
                       "I told my computer I needed a break. "
                       "Now it will not stop sending me vacation ads."],

    "thank"         : ["You are welcome! Happy to help anytime.",
                       "My pleasure! Come back if you need anything.",
                       "Glad I could help."],

    "thanks"        : ["Anytime! That is what ARIA is for.",
                       "You are welcome! Have a great day."],

    "you are great" : ["Thank you so much!",
                       "That is very kind of you."],

    "good bot"      : ["Thank you! I am trying my best.",
                       "That means a lot. Thank you."],

    "i am sad"      : ["I am sorry to hear that. Every dark night "
                       "is followed by a bright morning. You got this.",
                       "Sending virtual support your way. Things will get better."],

    "i am happy"    : ["That is wonderful! Happiness is the best energy.",
                       "Love to hear that! Keep smiling."],

    "i am bored"    : ["Ask me for a joke, or ask me about AI.",
                       "Ask me anything. I am here."],

    "bye"           : ["Goodbye! It was great chatting with you.",
                       "See you next time. Take care.",
                       "Bye! Come back anytime."],

    "goodbye"       : ["Goodbye! Have a wonderful day.",
                       "Farewell! ARIA will be here whenever you need me."],

    "see you"       : ["See you later! Take care.",
                       "Goodbye for now! Come back anytime."],
}

EXIT_COMMANDS = ["exit", "quit", "close", "stop", "end", "shutdown"]


def show_banner():
    print("=" * 60)
    print("        ARIA - Artificial Rule-based Intelligence")
    print("              Assistant  |  DecodeLabs 2026")
    print("=" * 60)
    print("  Type 'help' to see what I can do.")
    print("  Type 'exit' or 'quit' to end the session.")
    print("=" * 60)
    print()


def show_help():
    print()
    print("  ---- ARIA HELP MENU ----")
    print()
    print("  Greetings   : hello, hi, hey, good morning")
    print("  About Me    : who are you, what is your name")
    print("  About AI    : what is ai, what is rule based")
    print("  Time & Date : what is the time, what is today's date")
    print("  Jokes       : tell me a joke, say something funny")
    print("  Feelings    : i am sad, i am happy, i am bored")
    print("  Exit        : exit, quit, bye, goodbye")
    print()


def get_time():
    now = datetime.datetime.now()
    return "The current time is: " + now.strftime("%I:%M %p")


def get_date():
    now = datetime.datetime.now()
    return "Today is: " + now.strftime("%A, %d %B %Y")


def sanitize(raw_input):
    return raw_input.lower().strip()


def get_response(clean_input, user_name):
    if "time" in clean_input:
        return get_time()

    if "date" in clean_input or "today" in clean_input or "what day" in clean_input:
        return get_date()

    if "help" in clean_input:
        show_help()
        return ""

    for keyword in RESPONSES:
        if keyword in clean_input:
            reply = random.choice(RESPONSES[keyword])

            if reply == "__TIME__":
                return get_time()
            if reply == "__DATE__":
                return get_date()
            if reply == "__HELP__":
                show_help()
                return ""

            return reply

    return "I did not understand that. Type 'help' to see what I can do, " + user_name + "."


def main():
    show_banner()

    user_name = input("  Before we begin, what is your name? : ").strip()

    if user_name == "":
        user_name = "Friend"

    print()
    print("  Welcome, " + user_name + "! I am ARIA. Let's chat.")
    print()

    message_count = 0

    while True:
        raw_input = input("  " + user_name + " : ")
        clean_input = sanitize(raw_input)

        if clean_input == "":
            print("  ARIA  : Please say something. Type 'help' if unsure.")
            print()
            continue

        if clean_input in EXIT_COMMANDS:
            print()
            print("  ARIA  : Goodbye, " + user_name + "! It was great talking to you.")
            print("          We had " + str(message_count) + " exchanges in this session.")
            print("          See you next time.")
            print()
            print("=" * 60)
            break

        message_count += 1

        response = get_response(clean_input, user_name)

        if response:
            print("  ARIA  : " + response)
            print()


if __name__ == "__main__":
    main()
