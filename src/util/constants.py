import arcade
from arcade.gui import UIFlatButton, UIManager, UIAnchorLayout, UISlider
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

main_men_buttons = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"buttons.png")
akinator_1 = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"akinator_1.jpg")
pauseButtons = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"PauseButtons.png")
shaqanator = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"shaqanator.png")
paulanator = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"paul.png")
guess_buttons = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"guess_buttons.png")


# Game assets.
background_pattern = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"background-pattern.png")
question_bar = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"question-bar.png")
top_bar = arcade.load_texture(pathlib.Path(r"src")/"sprites"/"top-bar.png")

# Game colors.
COLOR_BG = (40, 40, 40)
COLOR_GOLD = (255, 215, 0)
COLOR_DARK_RED = (165, 0, 0) 
COLOR_DARK = (30, 30, 30) 
COLOR_LIGHT = (180, 180, 180) 

# Game button style.
button_style_small = {
        "normal": UIFlatButton.UIStyle(
            bg=COLOR_DARK,
            font_color=COLOR_LIGHT,
            font_size=16
            ),
        "hover": UIFlatButton.UIStyle(
            bg=COLOR_LIGHT,
            font_color=COLOR_DARK,
            font_size=16
            ),
        "press": UIFlatButton.UIStyle(
            bg=COLOR_LIGHT,
            font_color=COLOR_DARK,
            font_size=16
            ),
        "disabled": UIFlatButton.UIStyle(
            bg=COLOR_DARK,
            font_color=COLOR_LIGHT,
            font_size=16
            ),
        }

button_style_big = {
        "normal": UIFlatButton.UIStyle(
            bg=COLOR_DARK,
            font_color=COLOR_LIGHT,
            font_size=24
            ),
        "hover": UIFlatButton.UIStyle(
            bg=COLOR_LIGHT,
            font_color=COLOR_DARK,
            font_size=24
            ),
        "press": UIFlatButton.UIStyle(
            bg=COLOR_LIGHT,
            font_color=COLOR_DARK,
            font_size=24
            ),
        "disabled": UIFlatButton.UIStyle(
            bg=COLOR_DARK,
            font_color=COLOR_LIGHT,
            font_size=24
            ),
        }

slider_style = {
        "normal": UISlider.UIStyle(
            bg=COLOR_DARK,
            filled_track=COLOR_DARK,
            unfilled_track=COLOR_DARK,
            filled_step=COLOR_DARK,
            unfilled_step=COLOR_DARK,
            border_width=0,
            ),
        "hover": UISlider.UIStyle(
            bg=COLOR_LIGHT,
            filled_track=COLOR_DARK,
            unfilled_track=COLOR_DARK,
            filled_step=COLOR_DARK,
            unfilled_step=COLOR_DARK,
            border_width=0
            ),
        "press": UISlider.UIStyle(
            bg=COLOR_LIGHT,
            filled_track=COLOR_DARK,
            unfilled_track=COLOR_DARK,
            filled_step=COLOR_DARK,
            unfilled_step=COLOR_DARK,
            border_width=0
            ),
        "disabled": UISlider.UIStyle(
            bg=COLOR_DARK,
            filled_track=COLOR_DARK,
            unfilled_track=COLOR_DARK,
            filled_step=COLOR_DARK,
            unfilled_step=COLOR_DARK,
            border_width=0
            ),
        }
