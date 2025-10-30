import random
import os
import sys

JOKES_FILE = 'randomJokes.txt'
PROMPT = "Alexa tell me a Joke"

def load_jokes(filename):
    try:
        # Open file using 'with' statement 
        with open(filename, 'r') as f:
            lines = f.readlines() 
        
        jokes = []
        for line in lines: 
            parts = line.strip().split('?')
            if len(parts) == 2:
                jokes.append((parts[0].strip(), parts[1].strip()))
        return jokes
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Cannot run.")
        sys.exit(1)

def main():
    #Main program loop for the joke bot.
    jokes = load_jokes(JOKES_FILE)
    if not jokes:
        return

    print("🤖 Joke Bot is ready. Say the magic words to hear a joke!")
    
    while True: # Infinite while loop 
        user_input = input("\n> ")
        if user_input.lower() == PROMPT.lower():
            setup, punchline = random.choice(jokes)
            
            print(f"\n{setup}?")
            input("Press [Enter] to hear the punchline...")
            print(f"👉 {punchline}")
        elif user_input.lower() in ['quit', 'exit', 'bye']:
            print("🤖 Goodbye!")
            break # Break statement to exit loop 
        else:
            print(f"🤖 I didn't catch that. Try saying: '{PROMPT}' or 'quit'.")

if __name__ == "__main__":
    main()
