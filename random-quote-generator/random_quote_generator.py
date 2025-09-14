import random

def get_random_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
        "Don’t let yesterday take up too much of today. – Will Rogers",
        "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
        "If you are working on something exciting, it will keep you motivated. – Elon Musk",
        "Success is not in what you have, but who you are. – Bo Bennett",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Dream bigger. Do bigger.",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
        "Great things never come from comfort zones.",
        "Push yourself, because no one else is going to do it for you."
    ]
    return random.choice(quotes)

def main():
    print("Random Quote Generator")
    while True:
        print("\n" + get_random_quote())
        user_input = input("\nPress Enter to get another quote or type 'exit' to quit: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

# random_quote_generator.py
# A simple command-line application that displays a random motivational quote each time it is run.

