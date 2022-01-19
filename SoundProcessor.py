class SoundProcessor:

    def __init__(self, pygame, gameData):
        self.mixer = pygame.mixer
        self.mixer.init()
        gameData.get("SOUND_EVENT_BUS").add_subscriber(self)

    def on_event(self, event):
        name = event.get_name()
        if name == 'START_GAME':
            self.play(0, "music.mp3")
        if name == 'WALL_CROSS':
            self.play(1, "wall_cross.mp3")
        if name == 'PLATFORM_CROSS':
            self.play(1, "platform_cross.mp3")
        if name == 'LOSE_BALL':
            self.play(2, "loose_ball.mp3")

    def play(self, ch_number, filename):
        self.mixer.Channel(ch_number).play(self.mixer.Sound(filename))