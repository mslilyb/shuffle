import lib.attendio as atio
import lib.attconst as attconst
import json
import warnings

class AttendError(Exception):
	pass

class attend():
	"""
	Class representing attendance scoring schema and class metadata.

	Methods:

	+ addscore: add a type of score, option to set a value. Default is 0.
	+ calculate: Calculates and outputs total score for each student. 
		Options:
			+ Verbose: outputs full score details.
	+ writeout: displays attend object in human readable format
	+ jsonOUT: serializes attend object and writes to file. Default is parameter file.
	+ jsonIN: initializes attend object using the contents of a json file.

	 """

	def __init__ (self, course, quarter, section=None, 
		scores=None, weeks=10, quota=None):
		"""
		Parameters:
		-----
		+ course    `str`   string containing course name
		+ quarter   `str`   string containing quarter for class
		+ events    `int`   events per week.
		+ weeks     `int`   number of weeks in the quarter. Lower than 10 is
								less-than-weekly
		+ quota     `int`   Optional. Target number of meetings across quarter
		"""

		self.course = course
		self.quarter = quarter
		self.section = section
		self.scores = {}
		if scores:
			if isinstance(scores, dict): self.scores = scores
			else: raise AttendError("Scores attribute must be type dict")   
		self.weeks = weeks
		self.quota = quota

	def addscore(self, typ, sco):
		if not isinstance(sco, int):
			print("Score must be an integer")
			return None

		if typ in self.scores:
			warnings.warn(f'Warning! Attendance type {typ} already exists.')
			user_choice = atio.takein(f'Reassign {typ} to {sco}? (y/n): ', 
				attconst.BOOL_CHOICE)

			if user_choice in attconst.YES_OPTS:
				self.scores[typ] = sco
			else:
				print("Aborting.")

		else:
			self.scores[typ] = sco


	def calculate(self):
		#What the fuck am I doing here.
		pass

	def jsonOUT(self):
		pass