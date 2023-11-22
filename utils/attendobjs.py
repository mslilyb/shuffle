import json


class attend:
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

	 def __init__ (self, course, quarter, eventcount, scores=None, weeks=10, quota=None):
	 	"""
	 	Parameters:
		-----
	 	+ course	`str`	string containing course name
	 	+ quarter	`str`	string containing quarter for class
	 	+ events	`int`	events per week.
		+ weeks		`int` 	number of weeks in the quarter. Lower than 10 is
								less-than-weekly
		+ quota		`int`	Optional. Target number of meetings across quarter
		"""

		self.course = course
		self.quarter = quarter
		self.eventcount = eventcount
		self.scores = {}
		self.weeks = weeks