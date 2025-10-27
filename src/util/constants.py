import arcade
from arcade.gui import UIFlatButton, UIManager, UIAnchorLayout
import pathlib

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Brother Akinator"

transparent_style = {
            'normal'   : UIFlatButton.UIStyle(bg=[0,0,0,0]),
            'hover'    : UIFlatButton.UIStyle(bg=[0,0,0,0]),
            'press'    : UIFlatButton.UIStyle(bg=[0,0,0,0]),
            'disabled' : UIFlatButton.UIStyle(bg=[0,0,0,0])
            }

main_men_buttons = arcade.load_texture(pathlib.Path(r"src\sprites\buttons.png"))
akinator_1 = arcade.load_texture(pathlib.Path(r"src\sprites\akinator_1.jpg"))