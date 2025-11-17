import arcade
import util.akinator_mnb as mnb
import copy
import numpy as np

class BrotherWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # uncomment this line when ready to use the model, 
        # it creates a deepcopy so that when using the model for questions it doenst get messed up
        self.model, self.questions = mnb.get_model(r"src\util\dataset-v1.csv")
        
        #used to keep track of answers
        self.user_answers = np.full((1, mnb.X.shape[1]), np.nan)
        self.asked_questions = set()

    def generate_guess(self):
        guess = self.model.predict_proba(self.user_answers)
        guess = guess[0]

        return guess
    

    def get_a_question(self):
        # find questions not yet asked
        remaining = [q for q in self.asked_questions if q not in self.questions]

        if not remaining:
            return None  # or handle differently (e.g., reset)

        # return one random element
        import random
        return random.choice(remaining)
        