from manim import *

class HumanAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Human Figure Animation", font_size=36, color=WHITE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Define colors
        skin_color = "#FFDAB9"  # Peach for skin
        shirt_color = BLUE
        pants_color = DARK_GRAY

        # Create human components
        # Head: Circle
        head = Circle(radius=0.5, color=skin_color, fill_opacity=1).shift(UP * 2)
        
        # Torso: Rectangle
        torso = Rectangle(width=0.8, height=1.5, color=shirt_color, fill_opacity=1).shift(DOWN * 0.25)
        
        # Arms: Two lines (left and right)
        left_arm = Line(
            start=torso.get_top() + LEFT * 0.4,
            end=torso.get_top() + LEFT * 1.5 + DOWN * 1.2,
            color=skin_color,
            stroke_width=8
        )
        right_arm = Line(
            start=torso.get_top() + RIGHT * 0.4,
            end=torso.get_top() + RIGHT * 1.5 + DOWN * 1.2,
            color=skin_color,
            stroke_width=8
        )
        
        # Legs: Two lines (left and right)
        left_leg = Line(
            start=torso.get_bottom() + LEFT * 0.4,
            end=torso.get_bottom() + LEFT * 0.8 + DOWN * 1.5,
            color=pants_color,
            stroke_width=8
        )
        right_leg = Line(
            start=torso.get_bottom() + RIGHT * 0.4,
            end=torso.get_bottom() + RIGHT * 0.8 + DOWN * 1.5,
            color=pants_color,
            stroke_width=8
        )
        
        # Group all parts
        human = VGroup(head, torso, left_arm, right_arm, left_leg, right_leg)
        human.move_to(ORIGIN)

        # Animate creation step-by-step
        self.play(Create(head), run_time=0.5)
        self.play(Create(torso), run_time=0.5)
        self.play(Create(left_arm), Create(right_arm), run_time=0.5)
        self.play(Create(left_leg), Create(right_leg), run_time=0.5)
        self.wait(1)

        # Animate arm wave (right arm moves up and down)
        right_arm_wave = Line(
            start=torso.get_top() + RIGHT * 0.4,
            end=torso.get_top() + RIGHT * 1.5 + UP * 0.5,  # Raised position
            color=skin_color,
            stroke_width=8
        )
        self.play(Transform(right_arm, right_arm_wave), run_time=0.5)
        self.play(Transform(right_arm, Line(
            start=torso.get_top() + RIGHT * 0.4,
            end=torso.get_top() + RIGHT * 1.5 + DOWN * 1.2,  # Back to original
            color=skin_color,
            stroke_width=8
        )), run_time=0.5)
        self.wait(1)

        # Add label
        label = Text("Human Figure", font_size=24, color=WHITE).next_to(human, DOWN)
        self.play(Write(label))
        self.wait(1)

        # Fade out
        self.play(FadeOut(VGroup(human, label, title)))

# Configuration to ensure single MP4 output
config.flush_cache = True  # Clear cached partial files
config.write_sections = False  # Disable saving partial sections

if __name__ == "__main__":
    scene = HumanAnimation()
    scene.render()  # Render the scene to create the MP4 file
    print("Rendering complete. Check the output directory for the MP4 file.")
    # Note: The output will be saved in the default output directory of Manim.