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

red_style = {
    "normal": UIFlatButton.UIStyle(
        font_size=28,
        font_name=("calibri", "arial"),
        font_color= arcade.color.WHITE,
        bg=(200, 60, 60, 255),
        border=(120, 0, 0, 255),
        border_width=3,
    ),
    "hover": UIFlatButton.UIStyle(
        font_size=28,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=(220, 80, 80, 255),
        border=(160, 20, 20, 255),
        border_width=3,
    ),
    "press": UIFlatButton.UIStyle(
        font_size=28,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=(160, 40, 40, 255),
        border=(80, 0, 0, 255),
        border_width=3,
    ),
    "disabled": UIFlatButton.UIStyle(
        font_size=28,
        font_name=("calibri", "arial"),
        font_color=arcade.color.GRAY,
        bg=(100, 100, 100, 255),
        border=(60, 60, 60, 255),
        border_width=3,
    ),
}

main_men_buttons = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"buttons.png")
akinator_1 = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"akinator_1.jpg")
bg = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"background-pattern.png")
question_bar = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"question-bar.png")
akinator = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"akinator-placeholder.png")