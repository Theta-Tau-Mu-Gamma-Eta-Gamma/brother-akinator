import arcade
import util.constants as constants
from util.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIAnchorLayout,
    UIView,
    UIFlatButton
)


class GuessView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        super().__init__()

        # Create a UIManager
        self.ui = UIManager()

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())

        self.paulanator = arcade.Sprite(constants.paulanator)
        self.paulanator.scale = .6
        self.paulanator.center_x = WINDOW_WIDTH /2
        self.paulanator.center_y = WINDOW_HEIGHT /2 + 97

        self.buttons = arcade.Sprite(constants.guess_buttons)
        self.buttons.scale = .6
        self.buttons.center_x = WINDOW_WIDTH /2
        self.buttons.center_y = WINDOW_HEIGHT /2 -150

        self.bubble = arcade.Sprite(constants.bubble)
        self.bubble.center_x = WINDOW_WIDTH /2
        self.bubble.center_y = WINDOW_HEIGHT/2 + 120

        # Add a button switch to the other View.
        yes_button = anchor.add(
            UIFlatButton(width=174,height=105,style=constants.transparent_style ), 
            align_y=WINDOW_HEIGHT/2 - 510,
            align_x=WINDOW_WIDTH/2 - 923

        )
        no_button = anchor.add(
            UIFlatButton(width=174,height=105,style=constants.transparent_style),
            align_y=WINDOW_HEIGHT/2 -510,
            align_x=WINDOW_WIDTH/2 - 737
        )
        maybe_button = anchor.add(
            UIFlatButton(width=174,height=105,style=constants.transparent_style),
            align_y=WINDOW_HEIGHT/2 -510,
            align_x=WINDOW_WIDTH/2 - 550
        )
        dont_know_button = anchor.add(
            UIFlatButton(width=178,height=105,style=constants.transparent_style),
            align_y=WINDOW_HEIGHT/2 - 510,
            align_x=WINDOW_WIDTH/2 - 360
        )

        @yes_button.event("on_click")
        def on_click(event):
            print("DEBUG: User answered yes")
            
        @no_button.event("on_click")
        def on_click(event):
            print("DEBUG: User answered no")
            
        @maybe_button.event("on_click")
        def on_click(event):
            print("DEBUG: User answered maybe")

        @dont_know_button.event("on_click")
        def on_click(event):
            print("DEBUG: User answered I dont know")
            
    def on_show_view(self):
        """ Called when switching to this view"""
        self.window.background_color = arcade.color.BLACK
        self.ui.enable()
    
    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        """ Draw the menu """
        self.clear()
        arcade.draw_sprite(self.buttons)
        arcade.draw_sprite(self.paulanator)
        self.ui.draw()
        arcade.draw_text("Does it jiggle?", 3*WINDOW_WIDTH / 4, WINDOW_HEIGHT - 100,
                         arcade.color.GOLD, font_size=30, anchor_x="center")