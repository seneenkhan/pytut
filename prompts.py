from Question import Question

question_prompts = [
    "What color are apples? \n(a) Red\n(b) Orange\n(c) Purple\n(d) Green\n",
    "What color are bananas? \n(a) Red\n(b) Yellow\n(c) Purple\n(d) Blue\n",
    "What color are oranges? \n(a) Red\n(b) Orange\n(c) Purple\n(d) Blue\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)
