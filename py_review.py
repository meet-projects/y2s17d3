class Student:
	def __init__(self, name, year):
		self.name = name
		self.year = year	
		self.finished_lab = False
		self.focus = Falsee	

	def __repr__(self):
		return '<Student(name = %s, finished_lab = %s, focus = %s)>' %	(self.name, self.finished_lab, self.focus)

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_year(self):
		return self.year

	def set_year(self, year):
		self.year = year

	def finish_lab(self):
		if not self.finished_lab:
			self.finished_lab = True
			return "Student finished lab"
		else:
			return "Student already finished"

	def focus(self):
		if self.focus:
			return "Student is already focused"
		else:
			self.focus = True
			return "Student is now focused"

			