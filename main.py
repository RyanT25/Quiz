
#! Quiz

#* Questions, Options & Answers
quiz_data=[
    (
        "Where did the first modern Summer Olympic games take place in 1896?", 
        ["London", "Athens", "Paris", "Berlin"],
        2
    ),
    (
        "What country is Roger Federer from?", 
        ["Germany", "France", "Denmark", "Switzerland"],
        4
    ),
    (
        "Which sport do the New York Giants play?", 
        ["Ice Hockey", "Baseball", "American Football", "Basketball"],
        3
    ),
    (
        "What is the term for a score of 1 over par on a golf hole?", 
        ["Bogey", "Birdie", "Eagle", "Double Bogey"],
        1
    ),
    (
        "Which team won the FA Cup in 2013?", 
        ["Man Utd", "Portsmouth", "Wigan Athletic", "Leicester City"],
        3
    )
]

#* Display Welcome Message
print("--------------------")
print("Sports Quiz")
print("\nWelcome to the 'Sports Quiz'.")
print("Test your knowledge!")
print("--------------------")

#* Variable To Track Score
score=0

#* Display Questions
def display_quiz():
    for question, options, answer in quiz_data:
        print("\n"+ question)
        for x, option in enumerate(options, 1):
            print(f"{x}- {option}")
        
        #* User Input
        #? Data Validation
        while True:
            try:
                user_input=int(input("Answer between 1 & 4: "))
                if 1<= user_input <=4:
                    break
                else:
                    print("Invalid Input - Please Try Again!")
            except ValueError:
                print("Invalid Input - Please Try Again!")
        
        #* Calculate Score
        if user_input==answer:
            print("Correct!")
            global score
            score+=1
        else:
            print(f"Wrong! {answer}, is the correct answer.")
display_quiz()

#* Display Results
def display_results():
    print("\n--------------------")
    print("Quiz Complete!\n")
    print(f"The results are in... you got {score} out of {len(quiz_data)} questions, correct!")
    print("--------------------")
display_results()

#* Thank You Message
print("Thank you for taking part in the 'Sports Quiz'.\n")

