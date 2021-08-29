from time import sleep

class ProgressBar:
	def __init__(self, start=0, total=100, length=20, char="=", increment_delay=1):
		self.current = start
		self.total = total
		self.char = char
		self.length = length
		self.increment_delay = increment_delay
		self.percent = float(self.current) * 100 / self.total
		self._generate_bar()

	def increment(self, val=1):
		self.current += val
		self.percent = float(self.current) * 100 / self.total
		if self.percent <= 100:
			self._generate_bar()
			print(self.bar, end='\r')
			sleep(self.increment_delay)
		else:
			raise ValueError("Increment value greater than total progress bar value")

	def show(self):
		print(self.bar, end='\r')

	def _generate_bar(self):
		self.num_chars = int((self.percent / 100) * self.length)
		self.bar = f"[{self.char * self.num_chars}{' ' * (self.length - self.num_chars)}>] {round(self.percent, 4)}%        "
		# The spaces at the end fix a bug with the carriage return

if __name__ == '__main__':
	bar = ProgressBar(length=40, start=10, total=120)
	bar.show()
	bar.increment(10)
	bar.increment(10)
	bar.increment(80)
	bar.increment(10)