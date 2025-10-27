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


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        super().__init__()

        # Create a UIManager
        self.ui = UIManager()

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())

        self.buttons = arcade.Sprite(constants.main_men_buttons)
        self.buttons.scale = .5
        self.buttons.center_x = 3*WINDOW_WIDTH /4 
        self.buttons.center_y = WINDOW_HEIGHT /4 + 40

        self.akinator = arcade.Sprite(constants.akinator_1)
        self.akinator.scale = 1
        self.akinator.center_x = WINDOW_WIDTH /4 
        self.akinator.center_y = WINDOW_HEIGHT /2

        # Add a button switch to the other View.
        start_button = anchor.add(
            UIFlatButton(width=340,height=100, style=constants.transparent_style),
            align_y=1,
            align_x=WINDOW_WIDTH/4

        )
        settings_button = anchor.add(
            UIFlatButton(width=340,height=100, style=constants.transparent_style),
            align_y=-135,
            align_x=WINDOW_WIDTH/4
        )
        exit_button = anchor.add(
            UIFlatButton(width=340,height=100, style=constants.transparent_style),
            align_y=-275,
            align_x=WINDOW_WIDTH/4
        )

        @start_button.event("on_click")
        def on_click(event):
            print("DEBUG: moving to questions")
            #self.window.show_view(BlueView())

        @settings_button.event("on_click")
        def on_click(event):
            print("DEBUG: moving to settings")
            #self.window.show_view(BlueView())

        @exit_button.event("on_click")
        def on_click(event):
            arcade.exit()

            
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
        arcade.draw_sprite(self.akinator)
        self.ui.draw()
        arcade.draw_text("BROTHER AKINATOR", 3*WINDOW_WIDTH / 4, WINDOW_HEIGHT - 100,
                         arcade.color.GOLD, font_size=30, anchor_x="center")

   