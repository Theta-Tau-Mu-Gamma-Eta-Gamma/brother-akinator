import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout
from arcade.gui.widgets.slider import UISlider
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIAnchorLayout,
    UIView,
    UIFlatButton
)

import globals
import util.constants as constants
from util.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class SettingsView(arcade.View):
    def __init__(self, previous_view: arcade.View):
        super().__init__()

        self.previous_view = previous_view
        # self.ui_manager = UIManager()

        # # This creates a "manager" for all our UI elements
        # self.ui_manager = arcade.gui.UIManager(self.window)

        # box = arcade.gui.widgets.layout.UIBoxLayout(vertical=True, space_between=20)

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

        # Slide.
        self.vol_slider = UISlider(value=0.5, width=600, height=100, max_value=1, min_value=0, style=constants.slider_style)
        anchor.add(self.vol_slider)

        buttons_w = 700
        buttons_h = 80
        return_button = anchor.add(
            UIFlatButton(width=buttons_w,height=buttons_h,text="Return",style=constants.button_style_big),
            align_y=-150,
            align_x=0
        )

        @return_button.event("on_click")
        def on_click(event):
            self.window.show_view(self.previous_view)

        @self.vol_slider.event("on_change")
        def on_volume_change(event):
            globals.audio.set_music_volume(self.vol_slider.value)

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.bg)
        arcade.draw_sprite(self.top_bar)
        self.ui.draw()
        arcade.draw_text("Settings", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 228, constants.COLOR_LIGHT, font_size=32, anchor_x="center", anchor_y="center")

    def on_show_view(self):
        self.window.background_color = constants.COLOR_BG
        self.ui.enable()

    def on_hide_view(self):
        self.ui.disable()

def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window()

    # Create the GameView
    game = SettingsView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
