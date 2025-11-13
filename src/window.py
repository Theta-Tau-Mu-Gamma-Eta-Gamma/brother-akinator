import arcade

class BrotherWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def adjust_volume(self, vol):
        print(vol)
        #self.media_player.volume = vol