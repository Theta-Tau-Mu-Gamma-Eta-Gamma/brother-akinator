import arcade
import util.constants as constants
from util.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIAnchorLayout,
    UIView,
    UIFlatButton,
    UISlider
)

class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        super().__init__()
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.vol_slider = UISlider(value=0.5, width=600, height=150, max_value=1, min_value=0)
        self.vol_slider.event(self.on_change)

        # --- mute button
        normal_texture = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/sound_off.png"
        )
        hover_texture = arcade.load_texture(
            ":resources:onscreen_controls/shaded_dark/sound_off.png"
        )
        press_texture = arcade.load_texture(
            ":resources:onscreen_controls/shaded_dark/sound_off.png"
        )

        # Create our button
        self.mute_button = arcade.gui.widgets.buttons.UITextureButton(
            texture=normal_texture,
            texture_hovered=hover_texture,
            texture_pressed=press_texture,
        )

        ui_anchor_layout = arcade.gui.UIAnchorLayout()
        ui_anchor_layout.add(child=self.vol_slider, 
                             anchor_x="center_x", 
                             anchor_y="center_y", 
                             align_y = 150)
        
        ui_anchor_layout.add(child=self.mute_button, 
                             anchor_x="center_x", 
                             anchor_y="center_y", 
                             align_y = -150)

    def on_show_view(self):
        """ Called when switching to this view"""
        self.window.background_color = arcade.color.BLACK
        self.ui.enable()
    
    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        """ Draw the menu """
        self.clear()
       
        self.ui.draw()
       