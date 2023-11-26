# from turtle import circle
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())
        # Create a circle
        circle = Circle(radius=1, color=BLUE)
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle))
