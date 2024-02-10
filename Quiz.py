import time
# ------------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()

# ------------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
# ------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("RESULTS")
    print("------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


# ------------------------------
def play_again():
    again = input("Would you want to play again? (yes/no): ").lower()
    if again in ["yes", "y"]:
        new_game()
    else:
        print("Okay, the game will close in 3 seconds.")
        time.sleep(3)
    # ------------------------------

questions = {
    "What year was minecraft fully released in?: " : "A",
    "Is minecraft older than a 10 year old?: " : "C",
    "Who was the first president of the USA?: " : "B",
    "What year did WW2 end in?: " : "D"
}

options = [["A. 2011", "B. 2010", "C. 2008", "D. 2024"],
           ["A. No", "B. maybe?", "C. yes", "D. absolutely not"],
           ["A. George Bush", "B. George Washington", "C. Donald Trump", "D. Vladimir Putin"],
           ["A. 2000", "B. 1918", "C. 1795", "D. 1945"]]

new_game()