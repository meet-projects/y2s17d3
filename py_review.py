class Student:
	def __init__(self, name):
		self.name = name
		self.in_lesson = False
		self.focus = False

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def go_to_lesson(self):
		if not self.in_lesson:
			self.in_lesson = True
			return "Student went to lesson"
		else:
			return "Student already in lesson"

	def focus(self):
		if self.focus:
			return "Student is already focused"
		else:
			self.focus = True
			return "Student is now focused"

			