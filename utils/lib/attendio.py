import lib.attendobjs
import lib.attconst
import warnings

def invalidinput():
	print("Invalid input.")

def verify(userin, bc):

	isbool = userin in lib.attconst.YES_OPTS or userin in lib.attconst.NO_OPTS

	isint = False

	if not bc:
		try:
			isint = int(userin)
		except:
			invalidinput()
			return(isint, userin)

	elif bc and isbool:
		return(isbool, userin)

	else:
		# It's a bool choice and an invalid input.
		invalidinput()

	return(isint, userin)



def takein(prompt, typ=None):
	while True:
		userinput = input(prompt)
		boolc = False

		if typ == None:
			return(userinput)

		elif typ == lib.attconst.BOOL_CHOICE:
			boolc = True

		valid, result = verify(userinput.lower(), boolc)

		if valid:
			return(result)



def test():
	firsttest = takein(f'Trying a yes/no prompt (yes/no): ', "yn")
	print(firsttest)
	secondtest = takein(f'Trying a number prompt: ', "integer")
	print(secondtest)
	thirdtest = takein(f'Trying generic prompt: ')
	print(thirdtest)