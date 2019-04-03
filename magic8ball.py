from random import choice
from time import sleep
# from tkinter import *

# class Magic8Ball(Frame):
# 	def __init__(self, master=None):

# 		Frame.__init__(self, master)
# 		self.grid()
# 		self.master.title('Magic 8 Ball')
# 		self.master.configure(background='black')
# 		self.master.geometry('500x400')
# 		self.master.resizable(0,0)
# 		self.createHeading()
# 		self.createQuestion()
# 		self.createShakebutton()
# 		self.eightballpic()

# 	def createHeading(self):
# 		self.heading = Label(self, text='Please ask the Magic 8 Ball a question.', font=('Times New Roman', 15))
# 		self.heading.config(bg='white', fg='blue')
# 		self.heading.grid(row=1, column=0, columnspan=3, pady=5, padx=5)

# 	def createQuestion(self):
# 		self.question = Entry(self, width=30)
# 		self.question.grid(row=1, column=0, columnspan=3, pady=5, padx=10)
# 		self.question.focus_force()
# 		return self.question

# 	def createShakebutton(self):
# 		self.shake = Button(self, text='Shake the Magic 8 Ball!', font=('Times New Roman', 15))
# 		self.shake.configure(bg='black', fg='white')
# 		self.shake.grid(row=3, column=1, pady=5, padx=5)
# 		self.shake['command'] = self.validate
# 		self.master.bind('<Return>', self.validate2)

# 	def eightballpic(self):
# 		self.picture = Label(self)
# 		self.picture.grid(row=4, column=0, columnspan=3, pady=5, padx=5)
# 		self.ball = PhotoImage(file='/Users/mass/Desktop/giphy.gif')
# 		self.picture['image'] = self.ball
# 		return self.picture

# 	def display(self, message):
# 		self.picture.grid_remove()
# 		self.picture = Label(self)
# 		self.picture.grid(row=4, column=0, columnspan=3, pady=5, padx=5)
# 		self.ball2 = PhotoImage(file='/Users/mass/Desktop/giphy.gif')
# 		answers = Text(self, width=17, height=6, bg='blue', fg='white', wrap='word')
# 		answers.config(font='bold')
# 		answers.grid(row=4, column=1, columnspan=1)
# 		answers['state'] = 'normal'
# 		answers.delete(0.0, 'end')
# 		answers.insert(0.0, message)
# 		answers['state'] = 'diabled'
# 		self.question.delete(0, 'end')

# 	def validate(self):
# 		question = self.question.get()
# 		if question == '':
# 			message = "You didn't enter anything."
# 			self.display(message)
# 		elif question.isdigit():
# 			message = "I am not a calculator! Please enter a question in words."
# 			self.display(message)
# 		elif not question.endswith("?"):
# 			message = "Was that a question? You forgot the question mark."
# 			self.display(message)
# 		elif not " " in question:
# 			message = "No one-word questions please."
# 			self.display(message)

# 	def validate2(self, event):
# 		question = self.question.get()
# 		if question == '':
# 			message = "You didn't enter anything."
# 			self.display(message)
# 		elif question.isdigit():
# 			message = "I am not a calculator! Please enter a question in words."
# 			self.display(message)
# 		elif not question.endswith("?"):
# 			message = "Was that a question? You forgot the question mark."
# 			self.display(message)
# 		elif not " " in question:
# 			message = "No one-word questions please."
# 			self.display(message)

# 	def submit_answer(self):
# 		responses = ['Yes',
# 		 'No', 
# 		 'No doubt about it', 
# 		 'It seems to be the case', 
# 		 'Absolutely', 
# 		 'Consentrate and ask again', 
# 		 'Outlook not so good', 
# 		 'It is certain', 
# 		 'Count on it', 
# 		 'It is decidedly so', 
# 		 'Dear God no!',
# 		 "Fo'sho", 
# 		 'No way',
# 		 'The outlook is bleak', 
# 		 'Not now', 
# 		 'Very likely', 
# 		 'Maybe', 
# 		 'Does the Pope shit in the woods?', 
# 		 'If that is what your heart desires', 
# 		 'The answer is yes']

# 		message = choice(responses)

# 		self.display(message)

# win = Magic8Ball()
# win.mainloop()


responses = ['Yes', 'No', 'No doubt about it', 'It seems to be the case', 'Absolutely', 'Consentrate and ask again', 'Outlook not so good', 'It is certain', 'Count on it', 'It is decidedly so', 'Dear God no!', "Fo'sho", 'No way', 'The outlook is bleak', 'Not now', 'Very likely', 'Maybe', 'Does the Pope shit in the woods?', 'If that is what your heart desires', 'The answer is yes']

def eight_ball(): 
	input('Please enter your yes/no question ...\n')
	print('... thinking ...')
	sleep(4)
	print(choice(responses))
	again()

def again():
	q=input('Do you want to ask another question?\n')
	if q.lower() == 'yes':
		eight_ball()
		# input('Please enter your question ...\n')
		# print('... thinking ...')
		# sleep(4)
		# print(choice(responses))
	elif q.lower() == 'no':
		print('Goodbye!')
		quit()
	else:
		print('Please type Yes or No')
	again()

print(eight_ball())


