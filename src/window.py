import arcade
import util.akinator_mnb as mnb
import copy
import numpy as np

class BrotherWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # uncomment this line when ready to use the model, 
        # it creates a deepcopy so that when using the model for questions it doenst get messed up
        model = mnb.get_model("dataset-v1.csv")
        
        #used to keep track of answers
        user_answers = np.full((1, mnb.X.shape[1]), np.nan)
        asked_questions = set()

        
        

        