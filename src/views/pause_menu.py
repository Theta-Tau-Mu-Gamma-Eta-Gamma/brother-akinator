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
import random
from views.settings_menu import SettingsView   

class PauseView(arcade.View):
    """ Class that manages the 'pause' view. """
    def __init__(self, game_view: arcade.View):
        super().__init__()

        # Create a UIManager
        self.ui = UIManager()
        self.game_view = game_view

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())

        self.buttons = arcade.Sprite(constants.pauseButtons)
        self.buttons.scale = 1
        self.buttons.center_x = WINDOW_WIDTH /2
        self.buttons.center_y = WINDOW_HEIGHT /2

        self.shaqanator = arcade.Sprite(constants.shaqanator)
        self.shaqanator.scale = 1
        self.shaqanator.center_x = 3*WINDOW_WIDTH /4 + 70
        self.shaqanator.center_y = WINDOW_HEIGHT /2

        self.shaqanator2 = arcade.Sprite(constants.shaqanator)
        self.shaqanator2.scale = 1
        self.shaqanator2.center_x = WINDOW_WIDTH /4 - 70
        self.shaqanator2.center_y = WINDOW_HEIGHT /2

        # Add a button switch to the other View.
        resume_button = anchor.add(
            UIFlatButton(width=350,height=100, style=constants.transparent_style),
            align_y=140,
            align_x=0

        )
        settings_button = anchor.add(
            UIFlatButton(width=350,height=100, style=constants.transparent_style),
            align_y=0,
            align_x=0
        )
        exit_button = anchor.add(
            UIFlatButton(width=340,height=100, style=constants.transparent_style),
            align_y=-140,
            align_x=0
        )

        @resume_button.event("on_click")
        def on_click(event):
            print("DEBUG: moving to questions")
            # self.window.show_view(BlueView())
            self.window.show_view(self.game_view)

        @settings_button.event("on_click")
        def on_click(event):
            print("DEBUG: moving to settings")
            settings_view = SettingsView(self)
            self.window.show_view(settings_view)

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
        arcade.draw_sprite(self.shaqanator)
        arcade.draw_sprite(self.shaqanator2)
        self.ui.draw()
        arcade.draw_text("PAUSE MENU", WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100,
                         arcade.color.GOLD, font_size=30, anchor_x="center")

   