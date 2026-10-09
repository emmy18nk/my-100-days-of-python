questions = [
    "What keyword is used to create a function in Python?",
    "What does len() do?",
    "What symbol is used for comments in Python?"
]

answers = [
    "def",
    "find length",
    "#"
]

score = 0

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")

    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("You scored", score, "out of", len(questions))