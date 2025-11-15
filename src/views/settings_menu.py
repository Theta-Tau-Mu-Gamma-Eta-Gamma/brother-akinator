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


class SettingsView(arcade.View):
    def __init__(self, previous_view: arcade.View):
        super().__init__()

        self.previous_view = previous_view
        self.ui_manager = UIManager()
        
        

        # This creates a "manager" for all our UI elements
        self.ui_manager = arcade.gui.UIManager(self.window)

        box = arcade.gui.widgets.layout.UIBoxLayout(vertical=True, space_between=20)

        # --- Start button
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
        self.start_button = arcade.gui.widgets.buttons.UITextureButton(
            texture=normal_texture,
            texture_hovered=hover_texture,
            texture_pressed=press_texture,
        )
        

        self.vol_slider = UISlider(value=0.5, width=600, height=150, max_value=1, min_value=0)
        # Add in our element.
        box.add(self.start_button)
        box.add(self.vol_slider)
        return_button = box.add(
            UIFlatButton(width=340,height=50,text="Return")
        )

        self.ui_manager.add(
            arcade.gui.widgets.layout.UIAnchorLayout(children=[box])
        )

        @return_button.event("on_click")
        def on_click(event):
            print("DEBUG: moving to settings")
            self.window.show_view(self.previous_view)

    def on_draw(self):
        self.clear()

        # This draws our UI elements
        self.ui_manager.draw()
        arcade.draw_text("SETTINGS MENU",
                         x=0, y=self.window.height - 55,
                         width=self.window.width,
                         font_size=40,
                         align="center",
                         color=arcade.color.GOLD)

    def on_show_view(self):
        self.window.background_color = arcade.color.BLACK

        # Registers handlers for GUI button clicks, etc.
        # We don't really use them in this example.
        self.ui_manager.enable()

    def on_hide_view(self):
        # This unregisters the manager's UI handlers,
        # Handlers respond to GUI button clicks, etc.
        self.ui_manager.disable()

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