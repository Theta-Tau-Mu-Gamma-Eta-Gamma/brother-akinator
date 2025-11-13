import arcade
from typing import Dict, Optional

class Audio:
    def __init__(self,
                 musicPath: Optional[str] = None,
                 sfxPaths: Optional[Dict[str,str]] = None,
                 musicVolume: float = .5,
                 sfxVolume: float = 1):
        self.musicVolume = musicVolume
        self.sfxVolume = sfxVolume
        self.muted = False

        self._music_sound = None
        self._music_player = None
        if musicPath:
            self._music_sound = arcade.Sound(musicPath, streaming=True)
        self._sfx: Dict[str,arcade.Sound] = {}
        for name, path in (sfxPaths or {}).items():
            self._sfx[name] = arcade.load_sound(path)


    def start_music(self, loop: bool = True):
        if not self._music_sound:
            return
        self.stop_music()
        vol = 0.0 if self.muted else self.musicVolume
        self._music_player = self._music_sound.play(volume = vol, loop=loop)

    def stop_music(self):
        if self._music_player:
            self._music_player.pause()
            self._music_player = None
    
    def set_music_volume(self, volume: float):
        self.sfxVolume = max(0.0,min(1.0,volume))

    def toggle_mute(self):
        self.muted = not self.muted
        if self._music_player:
            self._music_plater.volume = 0.0 if self.muted else self.set_music_volume

