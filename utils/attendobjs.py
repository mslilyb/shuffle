import json


class attend:
	"""
	Class representing attendance scoring schema and class metadata. Functions include:

	- addscheme: adds an additional type of possible score for attendance
	- calculate: Calculates and outputs total score. 
		Options:
			- Verbose - outputs full score details.

	- update: updates main attendance csv, fills in missing scores with default updates most recent week

	 """

	 def __init__ (self, course, quarter, weekcount, )