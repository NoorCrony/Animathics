from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService


class PlotQuadratic(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 25, 5],
            axis_config={"color": BLUE},
        )

        # Define the quadratic function
        def quadratic(t):
            return [t, t**2, 0]

        # Plot the quadratic function using ParametricFunction
        graph = ParametricFunction(quadratic, t_range=[-5, 5], color=GREEN)

        self.add(axes, graph)
        self.wait(2)

        # Applying transformations
        shifted_graph = graph.copy().shift(UP)
        scaled_graph = graph.copy().scale(0.5).shift(RIGHT)

        # Adding voiceover text
        self.add_voiceover_text("Here's the original quadratic function")
        self.wait(2)
        self.play(Transform(graph, shifted_graph))
        self.add_voiceover_text("Now we've shifted it upwards")
        self.wait(2)
        self.play(Transform(graph, scaled_graph))
        self.add_voiceover_text(
            "And finally, we've scaled it and shifted it to the right")
        self.wait(2)
        self.play(FadeOut(graph))

    # def add_voiceover_text(self, text):
    #     voiceover = Text(text).scale(0.7).to_edge(DOWN)
    #     self.play(Write(voiceover))
    #     self.wait(1)
    #     self.play(FadeOut(voiceover))
