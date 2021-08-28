class ProgressBar:
	def __init__(self, start=0, total=100, char="="):
		self.current = start
		self.total = total
		self.char = char
		self.percent = float(self.current) * 100 / self.total
		self._generate_bar()

	def increment(self, val=1):
		self.current += val
		self.percent = float(self.current) * 100 / self.total
		if self.percent < 100:
			self._generate_bar()
			print('\r', self.bar, end='')
		else:
			raise ValueError("Increment value over total progress bar value")

	def show(self):
		print("Hello\n")
		print('\r', self.bar, end='')

	def _generate_bar(self):
		self.bar = f"[{self.char * self.current}>] {self.percent}%"
