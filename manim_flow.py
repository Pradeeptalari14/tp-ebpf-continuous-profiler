from manim import *

class EBPFStackFlow(Scene):
    def construct(self):
        title = Text("eBPF Continuous Profiler & FlameGraph", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        kernel_box = Rectangle(width=4.0, height=2.0, color=CYAN).shift(LEFT * 3)
        kernel_label = Text("Linux Kernel\n(99Hz perf_event)", font_size=20).move_to(kernel_box)
        
        user_box = Rectangle(width=4.0, height=2.0, color=ORANGE).shift(RIGHT * 3)
        user_label = Text("User Space\n(FlameGraph Engine)", font_size=20).move_to(user_box)
        
        arrow = Arrow(kernel_box.get_right(), user_box.get_left(), color=YELLOW)
        arrow_label = Text("BPF RingBuffer", font_size=16).next_to(arrow, UP)

        self.play(Create(kernel_box), Write(kernel_label))
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.play(Create(user_box), Write(user_label))
        self.wait(1)
