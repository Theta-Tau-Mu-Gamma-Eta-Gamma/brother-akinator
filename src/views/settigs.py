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
import random


class SettingsView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        super().__init__()

        # Create a UIManager
        self.ui = UIManager()