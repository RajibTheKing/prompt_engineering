from manim import *

class NeuralNetworkAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Neural Network Visualization", font_size=36, color=WHITE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Define colors for layers
        input_color = BLUE
        hidden_color_1 = YELLOW
        hidden_color_2 = GREEN
        output_color = RED
        
        # Create neurons (dots)
        layer_1 = Dot(radius=0.2, color=input_color)
        layer_2 = VGroup(*[Dot(radius=0.2, color=hidden_color_1) for _ in range(4)]).arrange(DOWN, buff=0.8)
        layer_3 = VGroup(*[Dot(radius=0.2, color=hidden_color_2) for _ in range(2)]).arrange(DOWN, buff=0.8)
        layer_4 = Dot(radius=0.2, color=output_color)
        
        # Arrange layers horizontally
        layers = VGroup(layer_1, layer_2, layer_3, layer_4).arrange(RIGHT, buff=2.5)
        layers.move_to(ORIGIN)
        
        # Create labels for neurons
        layer_labels = VGroup(
            Text("Input", font_size=24).next_to(layer_1, UP),
            Text("Layer 2", font_size=24).next_to(layer_2, UP),
            Text("Layer 3", font_size=24).next_to(layer_3, UP),
            Text("Output", font_size=24).next_to(layer_4, UP)
        )
        
        # Create connections (weights)
        edges = VGroup()
        weight_labels = VGroup()
        # Layer 1 to Layer 2 (4 weights)
        for i, n in enumerate(layer_2):
            edge = Arrow(layer_1.get_center(), n.get_center(), color=WHITE, buff=0.2)
            edges.add(edge)
            # Weight label (e.g., w_1, w_2, ..., w_4)
            label = MathTex(f"w_{i+1}", font_size=24).next_to(edge.get_center(), UP+RIGHT, buff=0.2)
            weight_labels.add(label)
        
        # Layer 2 to Layer 3 (4 * 2 = 8 weights)
        for i, n1 in enumerate(layer_2):
            for j, n2 in enumerate(layer_3):
                edge = Arrow(n1.get_center(), n2.get_center(), color=WHITE, buff=0.2)
                edges.add(edge)
                # Weight label (e.g., w_5, w_6, ..., w_12)
                label = MathTex(f"w_{4 + i*2 + j + 1}", font_size=24).next_to(edge.get_center(), UP+RIGHT, buff=0.2)
                weight_labels.add(label)
        
        # Layer 3 to Layer 4 (2 weights)
        for i, n in enumerate(layer_3):
            edge = Arrow(n.get_center(), layer_4.get_center(), color=WHITE, buff=0.2)
            edges.add(edge)
            # Weight label (e.g., w_13, w_14)
            label = MathTex(f"w_{12 + i + 1}", font_size=24).next_to(edge.get_center(), UP+RIGHT, buff=0.2)
            weight_labels.add(label)
        
        # Create biases for Layer 2 (4 biases), Layer 3 (2 biases), Layer 4 (1 bias)
        bias_labels = VGroup()
        # Layer 2 biases
        for i, n in enumerate(layer_2):
            bias = MathTex(f"b_{i+1}", font_size=24).next_to(n, RIGHT, buff=0.3)
            bias_labels.add(bias)
        # Layer 3 biases
        for i, n in enumerate(layer_3):
            bias = MathTex(f"b_{4 + i + 1}", font_size=24).next_to(n, RIGHT, buff=0.3)
            bias_labels.add(bias)
        # Layer 4 bias
        bias = MathTex(f"b_7", font_size=24).next_to(layer_4, RIGHT, buff=0.3)
        bias_labels.add(bias)
        
        # Animate the network creation
        self.play(Create(layers), Write(layer_labels))
        self.play(Create(edges), lag_ratio=0.1)
        self.play(Write(weight_labels), Write(bias_labels))
        self.wait(1)
        
        # Move title to top-left for parameter counting
        self.play(title.animate.to_edge(UP + LEFT))
        
        # Animate parameter counting
        param_count = VGroup()
        weight_count_text = MathTex("Weights: ", "0", font_size=36).to_edge(DOWN).shift(UP * 1.5)
        bias_count_text = MathTex("Biases: ", "0", font_size=36).next_to(weight_count_text, DOWN)
        total_count_text = MathTex("Total Parameters: ", "0", font_size=36).next_to(bias_count_text, DOWN)
        param_count.add(weight_count_text, bias_count_text, total_count_text)
        
        self.play(Write(param_count))
        
        # Count weights (14)
        weight_count = 0
        for label in weight_labels:
            self.play(label.animate.set_color(YELLOW), run_time=0.2)
            weight_count += 1
            self.play(Transform(weight_count_text[1], MathTex(f"{weight_count}", font_size=36).move_to(weight_count_text[1].get_center())))
        self.play(weight_count_text.animate.set_color(YELLOW))
        
        # Count biases (7)
        bias_count = 0
        for label in bias_labels:
            self.play(label.animate.set_color(GREEN), run_time=0.2)
            bias_count += 1
            self.play(Transform(bias_count_text[1], MathTex(f"{bias_count}", font_size=36).move_to(bias_count_text[1].get_center())))
        self.play(bias_count_text.animate.set_color(GREEN))
        
        # Show total parameters (14 + 7 = 21)
        self.play(Transform(total_count_text[1], MathTex("21", font_size=36).move_to(total_count_text[1].get_center())))
        self.play(total_count_text.animate.set_color(RED))
        
        # Final pause to show the complete network and parameter count
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(VGroup(layers, edges, weight_labels, bias_labels, layer_labels, param_count, title)))

if __name__ == "__main__":
    nn = NeuralNetworkAnimation()
    nn.construct()