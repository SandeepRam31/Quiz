import os
import pandas as pd
import sys
import csv

if 'dataset.csv' not in os.listdir():
	data = pd.DataFrame({
		'question': [],
		'answer': [],
		'level': [],
		'subject': [],
		'topic': [],
		})
	
	data.to_csv('dataset.csv', index = False)

print('Welcome, Admin')
choice = int(input('Do you wish to add another question to the dataset? (0 for NO and 1 for YES)=> '))

if choice == 1:
	while True:
		question = input('Enter the question here =>')

		choices = []
		for choice in range(4):
			choices.append(input(f'Enter choice {choice + 1} =>'))

		for count, choice in enumerate(choices):
			question += f'\n{count+1}. {choice}'

		answer = input('Enter the correct answer (A, B, C, D)')

		level = int(input('Enter the level of this question (1, 2, 3) =>'))

		subject = input('Enter the subject =>')

		topic = input('Enter the topic')

		row = [[question, answer, level, subject, topic]]

		with open('dataset.csv', 'w+') as file:
			write = csv.writer(file)
			write.writerows(row)
                        
                
		choice = int(input('Do you wish to add another question to the dataset? (0 for NO and 1 for YES)=> '))

		if choice == 0:
			sys.exit("The changes have been saved.")
