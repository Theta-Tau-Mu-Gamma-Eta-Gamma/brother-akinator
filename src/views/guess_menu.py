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


class GuessView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.ui = UIManager()
        anchor = self.ui.add(UIAnchorLayout())
        
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


        yes_button = anchor.add(
            UIFlatButton(width=250,height=100,text="Yes",style=constants.button_style_small),
            align_y=-200,
            align_x=-150
        )
        
        no_button = anchor.add(
            UIFlatButton(width=250,height=100,text="No",style=constants.button_style_small),
            align_y=-200,
            align_x=150
        )
        
        @yes_button.event("on_click")
        def on_click(event):
            self.window.reset()
            self.window.show_main_menu()

        @no_button.event("on_click")
        def on_click(event):
            self.window.reset()
            self.window.show_questions()


    def on_show_view(self):
        self.ui.enable()
        self.brother = self.window.generate_guess()
        self.pic = None
        if self.brother in constants.textures:
            self.pic = arcade.Sprite(constants.textures[self.brother])
            self.pic.scale = .05
            self.pic.center_x = WINDOW_WIDTH / 2
            self.pic.center_y = WINDOW_HEIGHT / 2

        
    
    def on_hide_view(self):
        self.ui.disable()

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.bg)
        arcade.draw_sprite(self.paulanator)
        arcade.draw_sprite(self.top_bar)

        if self.pic != None:
            arcade.draw_sprite(self.pic)

        arcade.draw_text("?", WINDOW_WIDTH / 2 - 372, WINDOW_HEIGHT / 2 + 218, constants.COLOR_GOLD, font_size=16, anchor_x="center")
        arcade.draw_text("Is your brother "+self.brother+"?", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 228, constants.COLOR_LIGHT, font_size=18, anchor_x="center", anchor_y="center")
        self.ui.draw()
