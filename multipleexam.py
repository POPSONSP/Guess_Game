"""PROJECT
Write a python program that will ask user to choose subject to do exam, you are to have 5 subjects with at least
5 questions in each of the subjects, when user is done, the subject and the score for the subject should be 
stored in a dictionary, print out the subject with the maximum score.
Submission is tomorrow
"""
result = {}
def exam():    
    for i in range(2):
        student = input("Enter your student name ")
        print("NOTE!! You only have 5 trials. One for each subject")
        for i in range(5):
            subject = input("Enter the subject ").lower()
            if subject == "mathematics":
                maths(subject)
            elif subject == "english":
                english(subject)
            elif subject == "physics":
                physics(subject)
            elif subject == "geography":
                geo(subject)
            elif subject == "chemistry":
                chemistry(subject)
            else:
                print("Choose from the following options: Mathematics, English, Physics, Geography, Chemistry. Start again")
                exam()
                break
        print(result)
        print(f"{student} scored the highest in {min(result)} after writing {len(result)} subject(s)")

def maths(subject):
    score = 0
    question = ["Random Question", "Some Question"]
    options = ["a -- option", "b -- option"]
    answer = ["b", "a"]
    for i in range(2):
        print(question[i])
        print(options[i])
        user_ans = input("Enter your answer ")
        if user_ans == answer[i]:
            print("Correct")
            score += 5
        else:
            print("wrong")
    result.update({subject:score})
    
def english(subject):
    score = 0
    question = ["Random Question", "Some Question"]
    options = ["a -- option", "b -- option"]
    answer = ["b", "a"]
    for i in range(2):
        print(question[i])
        print(options[i])
        user_ans = input("Enter your answer ")
        if user_ans == answer[i]:
            print("Correct")
            score += 5
        else:
            print("wrong")
    result.update({subject:score})

def physics(subject):
    score = 0
    question = ["Random Question", "Some Question"]
    options = ["a -- option", "b -- option"]
    answer = ["b", "a"]
    for i in range(2):
        print(question[i])
        print(options[i])
        user_ans = input("Enter your answer ")
        if user_ans == answer[i]:
            print("Correct")
            score += 5
        else:
            print("wrong")
    result.update({subject:score})

def geo(subject):
    score = 0
    question = ["Random Question", "Some Question"]
    options = ["a -- option", "b -- option"]
    answer = ["b", "a"]
    for i in range(2):
        print(question[i])
        print(options[i])
        user_ans = input("Enter your answer ")
        if user_ans == answer[i]:
            print("Correct")
            score += 5
        else:
            print("wrong")
    result.update({subject:score})

def chemistry(subject):
    score = 0
    question = ["Random Question", "Some Question"]
    options = ["a -- option", "b -- option"]
    answer = ["b", "a"]
    for i in range(2):
        print(question[i])
        print(options[i])
        user_ans = input("Enter your answer ")
        if user_ans == answer[i]:
            print("Correct")
            score += 5
        else:
            print("wrong")
    result.update({subject:score})       
exam()