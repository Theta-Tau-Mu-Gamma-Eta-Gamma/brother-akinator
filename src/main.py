import arcade

from util.constants import WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH
from window import BrotherWindow 
from views.questions_menu import QuestionView
def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = BrotherWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = QuestionView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()

    

if __name__ == "__main__":
    main()