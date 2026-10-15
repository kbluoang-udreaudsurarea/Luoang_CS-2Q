"""
Student Performance Evaluator
Kyzen Mikko Luoang - 8-Camia
Oct. 13, 2026
"""

perf_level = "" #global variable storing the performance level as a string
def display_header(): #Displays the program header with a separator (newline)
    print("STUDENT PERFORMANCE EVALUATIOR \n")

def get_student_info(): #Gets student info (name, grades) for conversion into a performance level
    name = input("Enter student name: ") #Local variable, stores name
    scores = [] #scores for assessments, for returning
    for i in range(1, 4):
        scores.append(float(input(f"Enter Assessment {i}: ")))
    return name, scores #will be stored in the variables outside the function
    

def evaluate_performance(scores): #Evaluated the student's performance to convert it into a performance level
    average = (scores[0] + scores[1] + scores[2]) / 3 #Local variable, stores average
    perf = "" #Local variable, stores performance label
    if average >= 90:
        perf = "Outstanding"
    elif average >= 85:
        perf = "Very Satisfactory"
    elif average >= 80:
        perf = "Satisfactory"
    elif average >= 75:
        perf = "Fairly Satisfactory"
    else:
        perf = "Needs Improvement"
    return average, perf #will be stored in variables outside of the function

def display_report(): #Displays the final report
    print("STUDENT PERFORMANCE REPORT")
    print(f"Student Name: {name}")
    print(f"Assessment Scores: {scores[0]}, {scores[1]}, {scores[2]}")
    print(f"Average Score : {average:.2f}")
    print(f"Performance Level: {perf_level}")


display_header()
name, scores = get_student_info() #Global variables, stores name and scores
average, perf_level = evaluate_performance(scores) #Global variables, stores name and scores
display_report()
