import random

# List of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. Ernest Hemingway", "D. J.K. Rowling"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Fe", "D. Pb"],
        "answer": "A"
    }
]

# Function to display a question
def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
        

def get_answer():
    answer = input("Choose the correct option (A, B, C, D): ").strip().upper()
    return answer

def check_answer(question, user_answer):
    return user_answer == question["answer"]

def play_quiz(questions):
    random.shuffle(questions)  
    score = 0
    for q in questions:
        display_question(q)
        user_answer = get_answer()
        if check_answer(q, user_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
        print()
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    play_quiz(questions)
