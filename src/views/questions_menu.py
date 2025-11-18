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
from views.pause_menu import PauseView
from views.guess_menu import GuessView

import globals


class QuestionView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        super().__init__()

        # Create a UIManager
        self.ui = UIManager()

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())

        self.window.set_count(self.window.get_count() + 1)
        self.question, self.index = self.window.get_a_question()

        # Bg
        self.bg = arcade.Sprite(constants.background_pattern)
        self.bg.center_x = WINDOW_WIDTH / 2
        self.bg.center_y = WINDOW_HEIGHT / 2 - 130

        # Akinator
        self.paulanator = arcade.Sprite(constants.paulanator)
        self.paulanator.scale = .6
        self.paulanator.center_x = WINDOW_WIDTH / 4 - 150
        self.paulanator.center_y = WINDOW_HEIGHT / 2 - 50

        # Top Bar
        self.top_bar = arcade.Sprite(constants.question_bar)
        self.top_bar.scale = .7
        self.top_bar.center_x = WINDOW_WIDTH / 2
        self.top_bar.center_y = WINDOW_HEIGHT / 2

        # Answer Buttons
        buttons_w = 600
        buttons_h = 60
        buttons_gap = 30
        buttons_y_off = 30

        yes_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="Yes",style=constants.button_style_small), 
            align_y=-(buttons_h + buttons_gap) * 0 + buttons_y_off,
            align_x=0

        )
        no_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="No",style=constants.button_style_small),
            align_y=-(buttons_h + buttons_gap) * 1 + buttons_y_off,
            align_x=0
        )
        maybe_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="Maybe",style=constants.button_style_small),
            align_y=-(buttons_h + buttons_gap) * 2 + buttons_y_off,
            align_x=0
        )
        dont_know_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="I Don't Know",style=constants.button_style_small),
            align_y=-(buttons_h + buttons_gap) * 3 + buttons_y_off,
            align_x=0
        )

        @yes_button.event("on_click")
        def on_click(event):
            self.window.answered(self.index, 1)
            self.show_next_question()
            
        @no_button.event("on_click")
        def on_click(event):
            self.window.answered(self.index, 0)
            self.show_next_question()
            
        @maybe_button.event("on_click")
        def on_click(event):
            self.show_next_question()

        @dont_know_button.event("on_click")
        def on_click(event):
            self.show_next_question()
            
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
        arcade.draw_sprite(self.paulanator)
        arcade.draw_sprite(self.top_bar)
        self.ui.draw()
        arcade.draw_text(self.window.get_count(), WINDOW_WIDTH / 2 - 372, WINDOW_HEIGHT / 2 + 218, constants.COLOR_GOLD, font_size=16, anchor_x="center")
        arcade.draw_text(self.question, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 228, constants.COLOR_LIGHT, font_size=18, anchor_x="center", anchor_y="center")
        
    def on_key_press(self, symbol:int, modifiers:int):
            if symbol == arcade.key.ESCAPE:
                pause_view = PauseView(self)
                self.window.show_view(pause_view)

    def on_close(self):
        globals.audio.stop_music()

    def show_next_question(self):
        if self.window.get_count() == 26:
            self.window.show_view(GuessView())
        else:
            self.window.show_view(QuestionView())


