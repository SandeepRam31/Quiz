import csv
import random
import pandas as pd
import os 
import sys

# the file has 5 columns : Q A Level Subject Topic eg(Q, A, easy, physics, COM)
# Remind Disha to store the levels as 1 2 3 and not easy intermediate hard


def create_user():
    global subject
    global topic
    global SCORE
    global COUNT

    SCORE = 0
    COUNT = 0

    subjects = data['subjects'].unique().to_list()

    for count, subject in enumerate(subjects):
        print(f'{count + 1}. {subject}')

    subject = int(input('Which subject do you want to study? '))
    subject = subjects[subject - 1]

    topics = data[data['subjects'] == subject]['topic'].unique().to_list()

    for count, topic in enumerate(topics): 
        print(f"{count + 1}. topic")

    topic = int(input('Which topic do you want to study? =>'))
    topic = topics[topic - 1]

    question_function(get_questions(subject, topic), 1)


def get_questions(subject, topic):
    question_set = data[(data['subject'] == subject and data['topic'] == topic)]
    return question_set


def question_function(question_set, LEVEL):
    question = question_set[question_set['level'] == LEVEL]
    question = question.sample(frac = 1) # shuffled questions

    for index in range(len(question)):
        print(question[index]['question'])
        data.drop(question[index]['question'], inplace = True)

        choice = str(input("Enter your answer (A, B, C, D) => "))

        if choice.strip().lower() == question['index']['answer'].lower():
            print('Correct Answer')
            SCORE += 1

            if COUNT != 2:
                COUNT += 1

            else:
                if LEVEL != 3:
                    LEVEL += 1
                    question_function(get_questions(subject, topic), LEVEL) 
        else:
            print('Wrong Answer')

            if COUNT == 1:

            if COUNT != 0:
                COUNT -= 1

                if COUNT == 0:
                    if LEVEL != 0:
                        LEVEL -= 1
                        question_function(get_questions(subject, topic), LEVEL) 

        if len(data) == 0:
            print('We have ran out of questions')

            while True:
                choice = int(input('To continue press 1\nTo quit press 0\n>> '))

                if choice == 0:
                    print(f"Your score = {SCORE}")
                    sys.exit('Thank you for playing')
                    

                elif choice == 1:
                    print(f'Your score = {SCORE}')
                    print('Reloading....')

                    data = pd.read_csv('dataset.csv')
                    data.set_index('question', inplace= True)

                    create_user()

                else:
                    print('Invalid choice\n')

    else:
        print("CONGRATS, YOU'VE SUCCESSFULLY COMPLETED ALL LEVELS")

if __name__ == '__main__':

    instructions='''
 INSTRUCTIONS TO PLAY BRAIN UP                                                                        

 1. This is a study game which will be conducted based on your level of understanding of the topic.   
 2. To finish BrainUp you have to complete 6 questions continuously.                  
 3. You can chose the topic you want to be tested on.                                  
 4. After completing BrainUp you will be rewarded with a surprise!
    '''

    print(instructions)

    if 'dataset.csv' in os.listdir():
        data = pd.read_csv('dataset.csv')
        data.set_index('question', inplace= True)

        create_user()

    else:
        print('>>> No questions found \n'.upper())

#-------------------------------------------------------------------------------------------------------------------------------#


'''
* move it all into one csv file.
* admin - adding question
* create users
* GUI
'''
