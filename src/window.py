import arcade
import util.akinator_mnb as mnb
import copy
import numpy as np

import pathlib

from views.main_menu import MenuView
from views.questions_menu import QuestionView

class BrotherWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.model, self.questions = mnb.get_model(pathlib.Path(r"src")/"util"/"final-dataset.csv")
        
        # used to keep track of answers
        self.user_answers = np.full(self.questions.shape, 0)
        self.asked_questions = set()
        self.count = 0

    def generate_guess(self):

        guess = self.model.predict([self.user_answers])

        return guess[0]
    
    #returns a question (string) and its index (int)
    def get_a_question(self):
        # find questions not yet asked
        remaining = [q for q in self.questions if q not in self.asked_questions]

        # return one random element
        import random
        q = random.choice(remaining)
        self.asked_questions.add(q)
        i = np.where(self.questions == q)
        print(q,i)
        return (q, i)
    
    def answered(self, idx, answer):
        self.user_answers[idx] = answer

    def get_count(self):
        return self.count

    def set_count(self, value):
        self.count = value

    def reset(self):
        self.user_answers = np.full(self.questions.shape, 0)
        self.asked_questions = set()
        self.count = 0

    def show_main_menu(self):
        self.show_view(MenuView())

    def show_questions(self):
        self.show_view(QuestionView())



        
