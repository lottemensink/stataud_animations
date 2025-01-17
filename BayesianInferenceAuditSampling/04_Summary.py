from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class Summary(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base', model_name = "tts_models/multilingual/multi-dataset/xtts_v2"))

		# Title
		title = Text("Summary", font_size = 40)
		title.to_edge(UP)

		with self.voiceover("So, what have you learned in this clip?") as tracker:
			self.play(Write(title))

		# Take home points
		th1_sub1 = Tex("1. A sufficient sample size implies ", font_size = 40)
		th1_sub2 = Tex("$\\theta_{95}$", color = BLUE, font_size = 40)
		th1_sub2.next_to(th1_sub1, RIGHT)
		th1_sub3 = Tex("$<$", font_size = 40)
		th1_sub3.next_to(th1_sub2, RIGHT)
		th1_sub4 = Tex("$\\theta_{max}$", color = RED, font_size = 40)
		th1_sub4.next_to(th1_sub3, RIGHT)
		takehome1 = VGroup(th1_sub1, th1_sub2, th1_sub3, th1_sub4)
		takehome1.to_edge(LEFT)
		takehome1.shift(UP * 2)

		with self.voiceover("First, a sufficient sample size implies that the upper bound for the misstatement is below the performance materiality.") as tracker:
			self.play(Write(takehome1))

		takehome2 = Tex("2. The uniform prior is conservative", font_size = 40)
		takehome2.next_to(takehome1, DOWN)
		takehome2.to_edge(LEFT)

		with self.voiceover("Second, the uniform prior is conservative.") as tracker:
			self.play(Write(takehome2))

		takehome3 = Tex("3. Priors shifted to the left require a lower sample size", font_size = 40)
		takehome3.next_to(takehome2, DOWN)
		takehome3.to_edge(LEFT)

		with self.voiceover("And finally, a prior distribution that is shifted more to the left requires a lower sample size than the uniform prior to come to the same conclusion.") as tracker:
			self.play(Write(takehome3))

		self.play(
			FadeOut(title),
			FadeOut(takehome1),
			FadeOut(takehome2),
			FadeOut(takehome3)
		)
		self.wait()
