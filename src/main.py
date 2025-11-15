import arcade

from util.constants import WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH
from window import BrotherWindow 
from views.pause_menu import PauseView
from views.questions_menu import QuestionView
from views.main_menu import MenuView
from views.settings_menu import SettingsView
def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = BrotherWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    # question_view = QuestionView

    # pause_view = PauseView(QuestionView())

    main_view = MenuView()
    # Show GameView on screen
    window.show_view(main_view)

    # Start the arcade game loop
    arcade.run()

    

if __name__ == "__main__":
    main()