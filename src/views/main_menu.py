import arcade
from util.constants import WINDOW_HEIGHT, WINDOW_WIDTH

class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show_view(self):
        """ Called when switching to this view"""
        self.window.background_color = arcade.color.BLACK

    def on_draw(self):
        """ Draw the menu """
        self.clear()
        arcade.draw_text("Main Menu", WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100,
                         arcade.color.GOLD, font_size=30, anchor_x="center")

   