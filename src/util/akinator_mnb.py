from sklearn.naive_bayes import MultinomialNB
import numpy as np
import csv
import pathlib
'''
Please read before making changes or using this file.

X will need to be a 2D array of all valuse where the row index correlates to the brothers answers in relation to Y,
EX: Mark's answers in x should be all contained in row of index 1 since his name is index 1 in Y 

When using the model please make a deepcopy first using copy.deepcopy()
'''

#TODO np array of questions
questions = []

#TODO NP array of data
X = []
y = np.array([
    "Hayden Chester", 
    "Mark Khelemskiy", 
    "William Bhuiyan",
    "Jonathan Chang",
    "Ryan Chan",
    "Francesco Aguanno",
    "Jason Colletti",
    "Jack Rzepecki",
    "Donovan Edmondson",
    "Prema Mavuleti",
    "Helena Holmes",
    "Bushra Khan",
    "Fifi Zhang",
    "Liam Boyle",
    "Zakya El Abbadi",
    "Jackson Provenzo",
    "Anne Huang",
    "Denise Corano",
    "Erika Yick",
    "Isaac Loc",
    "Shomaun Miller",
    "Holly Fici",
    "Alexander Arevalo",
    "Daniel Allone",
    "Jeremy Pineda",
    "Brian Ren",
    "Talal Hayee",
    "Charlie Jiang",
    "Nicholas Reilly",
    "Matt Kruse",
    "Kyra Ho-shing",
    "Gerard Fajarda",
    "Ishita Ramrayka",
    "Camila Kaskey",
    "Lillian Mangan",
    "Jordan Wrench",
    "Benjamin Belotser",
    "Colin Zhang",
    "Jimmy Yang",
    "Matthew Amato", 
    "Dani Dueñas",
    "Marcus Guild",
    "Alan Lee",
    "James Caporuscio",
    "Abdullah As Sami"
    ])

def get_model(csv_file):
    #DONT touch this
    with open(csv_file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == 'Brother':
                questions = np.asarray(row[1:])
            else:
                X.append([int(i) for i in row[1:]])


    x = np.asarray(X)
    return MultinomialNB().fit(x,y)

def guess(model:MultinomialNB, answers):
    return model.predict_proba(answers)


if __name__ == "__main__":
    get_model(r"src\util\dataset-v1.csv")