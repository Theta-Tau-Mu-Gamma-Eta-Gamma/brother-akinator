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
from views.questions_menu import QuestionView
from views.settings_menu import SettingsView


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        super().__init__()

        # Create a UIManager
        self.ui = UIManager()

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())

        # Bg
        self.bg = arcade.Sprite(constants.background_pattern)
        self.bg.center_x = WINDOW_WIDTH / 2
        self.bg.center_y = WINDOW_HEIGHT / 2 - 130

        # Top Bar
        self.top_bar = arcade.Sprite(constants.top_bar)
        self.top_bar.scale = .7
        self.top_bar.center_x = WINDOW_WIDTH / 2
        self.top_bar.center_y = WINDOW_HEIGHT / 2

        # Buttons
        buttons_w = 700
        buttons_h = 80
        buttons_gap = 40

        start_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="Start",style=constants.button_style_big), 
            align_y=-(buttons_h + buttons_gap) * 0,
            align_x=0

        )
        settings_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="Settings",style=constants.button_style_big),
            align_y=-(buttons_h + buttons_gap) * 1,
            align_x=0
        )
        exit_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="Exit",style=constants.button_style_big),
            align_y=-(buttons_h + buttons_gap) * 2,
            align_x=0
        )

        @start_button.event("on_click")
        def on_click(event):
            question_view = QuestionView()
            self.window.show_view(question_view)

        @settings_button.event("on_click")
        def on_click(event):
            settings_view = SettingsView(self)
            self.window.show_view(settings_view)

        @exit_button.event("on_click")
        def on_click(event):
            arcade.exit()

            
    def on_show_view(self):
        """ Called when switching to this view"""
        self.window.background_color = constants.COLOR_BG
        self.ui.enable()
    
    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        """ Draw the menu """
        self.clear()
        arcade.draw_sprite(self.bg)
        arcade.draw_sprite(self.top_bar)
        self.ui.draw()
        arcade.draw_text("Brother Akinator", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 228, constants.COLOR_LIGHT, font_size=32, anchor_x="center", anchor_y="center")

   
