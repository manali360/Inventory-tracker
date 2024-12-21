import random
import time

def quiz_program():
    
    questions = {
        "What is the capital of France?": (["Berlin", "Madrid", "Paris", "Rome"], "Paris", "Paris is the capital city of France."),
        "What is 2 + 2?": (["3", "4", "5", "6"], "4", "2 + 2 equals 4."),
        "What is the largest planet in our solar system?": (["Earth", "Jupiter", "Mars", "Saturn"], "Jupiter", "Jupiter is the largest planet in our solar system."),
        "What is the chemical symbol for water?": (["H2O", "O2", "CO2", "NaCl"], "H2O", "The chemical symbol for water is H2O."),
        "What is the smallest prime number?": (["0", "1", "2", "3"], "2", "2 is the smallest prime number.")
    }

    
    question_list = list(questions.keys())
    random.shuffle(question_list)

    score = 0
    time_limit = 10  

    
    for question in question_list:
        options, correct_answer, explanation = questions[question]
        print(f"\n{question}")
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")

        
        start_time = time.time()
        answer = None

        while True:
            try:
                answer = input("Your answer (1-4): ")
                elapsed_time = time.time() - start_time

                if elapsed_time > time_limit:
                    print("Time's up! You didn't answer in time.")
                    break

                answer = int(answer)
                if 1 <= answer <= 4:
                    if options[answer - 1] == correct_answer:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is: {correct_answer}")
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
 print(f"Explanation: {explanation}")
 print(f"\nYour final score is: {score}/{len(questions)}")
 quiz_program()
