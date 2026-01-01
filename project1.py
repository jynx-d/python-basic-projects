# list the questions
# store the answers 
# randomly pick questions
# ask the questions 
# see if they are correct
# keep track of the score
# tell the user their score
# save & sort the highscores
# show the highscores at the start 

import random # to generate random questions
import json # for JSON module

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "bool",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

def display_high_scores_json():
    scores = []
    try:
        with open('highscores.json', 'r') as f:
            scores = json.load(f)
            print("\n TOP 5 HIGH SCORES: ")
            for i,s in enumerate(scores,1):
                print( f"{i}. {s['name']}: {s['score']}/5")
    except FileNotFoundError:
        print("No high scores yet!")

def save_high_score(name,score):
    scores = []
    try:
        with open('highscores.json', 'r') as f: # reads text file, converts it into JSON form & adds it to f
            scores = json.load(f) # converts JSON to  python code
    except FileNotFoundError:
        pass

    scores.append({"name": name, "score": score})
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:5] # sort on the basis of score
    with open('highscores.json', 'w') as f:  # w = write/ overwrite mode   
        json.dump(scores, f, indent=4) # convert python list back to JSON text & writes it to file
    print("High scores updated!")

def python_trivia_game():
    name = input("Enter your name: ")

    display_high_scores_json()
    input("\nPress Enter to start...\n")

    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx,question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {correct_answer}. \n") 

    print(f"Game over! Your final score is: {score}/{total_questions}")  
    save_high_score(name,score)

 

python_trivia_game()    

