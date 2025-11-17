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

        self.shaqanator = arcade.Sprite(constants.shaqanator)
        self.shaqanator.scale = 1
        self.shaqanator.center_x = 3*WINDOW_WIDTH /4 + 160
        self.shaqanator.center_y = WINDOW_HEIGHT /2

        self.shaqanator2 = arcade.Sprite(constants.shaqanator)
        self.shaqanator2.scale = 1
        self.shaqanator2.center_x = WINDOW_WIDTH /4 - 160
        self.shaqanator2.center_y = WINDOW_HEIGHT /2

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

        resume_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="Resume",style=constants.button_style_big), 
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

        @resume_button.event("on_click")
        def on_click(event):
            # self.window.show_view(BlueView())
            self.window.show_view(self.game_view)

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
        arcade.draw_sprite(self.shaqanator)
        arcade.draw_sprite(self.shaqanator2)
        self.ui.draw()
        arcade.draw_text("Pause", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 228, constants.COLOR_LIGHT, font_size=32, anchor_x="center", anchor_y="center")

   
