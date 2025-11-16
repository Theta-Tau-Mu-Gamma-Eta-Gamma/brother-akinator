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
        
        self.bar = arcade.Sprite(constants.question_bar)
        self.bar.scale = 0.8
        self.bar.center_x = WINDOW_WIDTH / 2
        self.bar.center_y = WINDOW_HEIGHT / 2 - 30
        
        self.akinator = arcade.Sprite(constants.akinator)
        self.akinator.scale = 0.7
        self.akinator.center_x = WINDOW_WIDTH / 2 - 450
        self.akinator.center_y = WINDOW_HEIGHT / 2 - 100

        yes_button = anchor.add(
            UIFlatButton(width=250,height=100, style=constants.red_style),
            align_y=-200,
            align_x=-150
        )
        
        no_button = anchor.add(
            UIFlatButton(width=250,height=100, style=constants.red_style),
            align_y=-200,
            align_x=150
        )
        
        @yes_button.event("on_click")
        def on_click(self):
            print("DEBUG: yes")

        @no_button.event("on_click")
        def on_click(self):
            print("DEBUG: no")

    def on_show_view(self):
        self.background = constants.bg
        self.ui.enable()
    
    def on_hide_view(self):
        self.ui.disable()
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(
            self.background,
            arcade.XYWH(
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2,
                WINDOW_WIDTH,
                WINDOW_HEIGHT
            ))
        arcade.draw_sprite(self.bar)
        arcade.draw_sprite(self.akinator)
        arcade.draw_text("Is your brother {name}?", WINDOW_WIDTH / 2, WINDOW_HEIGHT - 150,
                         arcade.color.GOLD, font_size=30, anchor_x="center")
        self.ui.draw()