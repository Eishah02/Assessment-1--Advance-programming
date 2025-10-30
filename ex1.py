import random
NUM_QUESTIONS = 10
POINTS_FIRST_ATTEMPT = 10
POINTS_SECOND_ATTEMPT = 5

DIFFICULTY_MAP = {
    1: (0, 9),
    2: (10, 99),
    3: (1000, 9999)
}

def displayMenu():
    print("\n DIFFICULTY LEVEL")
    print(" 1. Easy (Single-digit)")
    print(" 2. Moderate (Double-digit)")
    print(" 3. Advanced (Four-digit)")
    
    while True: #While loop 
        try:
            choice = input("Select difficulty (1,2,or3):").strip()
            level = int(choice)
            if level in DIFFICULTY_MAP: #Conditional
                return level
            else:
                print("Invalid choice. Please enter 1,2,or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def randomInt(difficulty_level):
    min_val, max_val = DIFFICULTY_MAP.get(difficulty_level, (0, 9))
    return random.randint(min_val, max_val)

def decideOperation():
    return random.choice(['+', '-'])

def calculateResult(num1, num2, operation):
    #to calculate the result 
    if operation == '+':
        return num1 + num2
    else:
        return num1 - num2

def displayProblem(num1, num2, operation):
    while True:
        try:
            question = f"{num1} {operation} {num2} = "
            user_input = input(question)
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def isCorrect(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. Try again.")
        return False

def displayResults(score):
    max_score = NUM_QUESTIONS * POINTS_FIRST_ATTEMPT
    
    if score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    else:
        rank = "D"

    print("\n--- QUIZ RESULTS ---")
    print(f"Final Score: {score} out of {max_score}")
    print(f"Your Rank: {rank}")
    print("--------------------")

def run_quiz():
    #Controls the flow of a single quiz session
    score = 0
    difficulty = displayMenu()
    
    print(f"\nStarting {NUM_QUESTIONS} question quiz...")

    for i in range(1, NUM_QUESTIONS + 1): # For loop 
        print(f"\n--- Question {i}/{NUM_QUESTIONS} ---")
        
        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        operation = decideOperation()
        correct_answer = calculateResult(num1, num2, operation)

        # First attempt
        user_answer = displayProblem(num1, num2, operation)
        if isCorrect(user_answer, correct_answer):
            score += POINTS_FIRST_ATTEMPT
            print(f"Score: +{POINTS_FIRST_ATTEMPT} points (Total: {score})")
            continue

        # Second attempt
        print("Second and final attempt:")
        user_answer = displayProblem(num1, num2, operation)
        if isCorrect(user_answer, correct_answer):
            score += POINTS_SECOND_ATTEMPT
            print(f"Score: +{POINTS_SECOND_ATTEMPT} points (Total: {score})")
        else:
            print(f"Correct answer was: {correct_answer}. No points awarded.")

    displayResults(score)

def main():
    #Initializes and loops the game.
    play_again='y'
    while play_again.lower()=='y':
        run_quiz()
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.lower()!='y':
            print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
