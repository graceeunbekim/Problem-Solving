# Author: Grace Eunbe Kim
# Contact: eunbegracekim40@gmail.com
# Thumbtack Remote Programming Challenge
# Simple DataBase Challenge

import sys
from abc import ABCMeta, abstractmethod

"""
Constant variable names for the database commands.
"""
SET        = "SET"
GET        = "GET"
UNSET      = "UNSET"
NUMEQUALTO = "NUMEQUALTO"
END        = "END"
BEGIN      = "BEGIN"
COMMIT     = "COMMIT"
ROLLBACK   = "ROLLBACK"
NULL       = "NULL"
INCORRECT  = "Incorrect Commands"

def displayOutput(result):
	"""

	"""
	sys.stdout.write(result)


class Commands:
	"""	
	Abstraction class for Commands received through standard input that are
	later used for the Transaction and Data classes for the database
	execution. Transaction and Data classes overrides setVal(), getVal(),
	unsetVal(), and endProgram().
	"""
	__metaclass__ = ABCMeta

	def __init__(self):
		pass

	@abstractmethod
	def detectCommands(self):
		"""detect command lines from the standard input."""
		pass

	@abstractmethod
	def setVal(self, name, value):
		"""Set the variable name to the value value. 
		   Neither variable names nor values will contain spaces"""
		pass

	@abstractmethod
	def getVal(self, name):
		"""Print out the value of the variable name, 
		   or NULL if that variable is not set."""
		pass

	@abstractmethod
	def unsetVal(self, name):
		"""Unset the variable name, making it just like that 
		   variable was never set."""
		pass

	@abstractmethod
	def endProgram(self):
		""" Exit the program. Your program will always receive 
		    this as its last command."""
		pass


class Data(Commands):
	"""
	Data class inherits from the abstract class Commands for the core
	exceutions and its own exceution 'NUMEQUALTO'.
	"""

	def __init__(self):
		self.database = {}

	def detectCommands(self, words):
		"""detectCommands finds which function will be executed depending
		on the command received from the standard input. """
		words = words.split(' ')

		key = words[0]

		if (key == SET):
			self.setVal(words[1], words[2])

		elif (key == GET):
			self.getVal(words[1])

		elif (key == UNSET):
			self.unsetVal(words[1])

		elif (key == NUMEQUALTO):
			self.runNumberQualTo(words[1])

		elif (key == END):
			return

		else:
			print INCORRECT


	def setVal(self, name, value):
		"""overrides setVal() function in Commands abstract class."""
		d = self.database
		vals = []

		vals.append(value)

		d[name] = vals		

	def getVal(self, name):
		"""overrides getVal() function in Commands abstract class."""
		try: 
			d = self.database
			if (d[name] in d):
				# displayOutput(d[name])
				print d[name]
			else:
				# displayOutput(NULL)
				print NULL
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e


	def unsetVal(self, name):
		"""overrides unsetVal() function in Commands abstract class."""
		d = self.database
		try:
			if (d[name] in d):
				del d[name]
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e

	def endProgram(self):
		"""overrides endProgram() function in Commands abstract class."""
		pass

	def runNumberQualTo(self, value):
		""" Print out the number of variables that are currently set to value. 
		    If no variables equal that value, print 0"""
		d = self.database
		count = 0
		for k,v in d.items():
			if (v == value):
				count += 1
		return count

class Transaction(Commands):
	"""
	Transaction class inherits from the abstract class Commands for the core
	exceutions and its own exceutions such as 'COMMIT', 'BEGIN', and 'ROLLBACK'.
	"""

	def __init__(self):
		self.database = {}

	def detectCommands(self, words):
		"""detectCommands finds which function will be executed depending
		on the command received from the standard input. """
		words.split(' ')
		key = words[0]

		if (key == SET):
			self.setVal(words[1], words[2])

		elif (key == GET):
			self.getVal(words[1])

		elif (key == UNSET):
			self.unsetVal(words[1])

		elif (key == END):
			return

		elif (key == BEGIN):
			self.begin()

		elif (key == COMMIT):
			self.commit()

		elif (key == ROLLBACK):
			self.rollback()

		else:
			return INCORRECT

	def setVal(self, name, value):
		"""overrides setVal() function in Commands abstract class."""
		d = self.database
		vals = []

		vals.append(value)

		d[name] = vals

	def getVal(self, name):
		"""overrides getVal() function in Commands abstract class."""
		try: 
			d = self.database
			if (d[name]):
				# displayOutput(d[name])
				print d[name]
			else:
				# displayOutput(NULL)
				print NULL
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e

	def unsetVal(self, name):
		"""overrides unsetVal() function in Commands abstract class."""
		d = self.database
		try:
			if (d[name] in d):
				del d[name]
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e

	def endProgram(self):
		"""overrides endProgram() function in Commands abstract class."""
		pass

	def begin(self):
		"""Open a new transaction block. Transaction blocks can be nested; 
		   a BEGIN can be issued inside of an existing block."""
		pass

	def rollback(self):
		"""Undo all of the commands issued in the most recent transaction block, 
		   and close the block. Print nothing if successful, 
		   or print NO TRANSACTION if no transaction is in progress."""
		pass

	def commit(self):
		"""Close all open transaction blocks, permanently applying the 
		   changes made in them. Print nothing if successful, 
		   or print NO TRANSACTION if no transaction is in progress."""
		pass


def main():
	""" main() function to instantiate two classes for Data and Transaction commands.
		standard input is read until END is input; otherwise, program
		executes and displays the output of the commands. """
	current_command = None
	dataCommand = Data()
	tranCommand = Transaction()
	
	while True:
		userinput = sys.stdin.readline().rstrip('\n')#.split(' ')
		dataCommand.detectCommands(userinput)
		if userinput == END:
			break
		if userinput == BEGIN:
			tranCommand.detectCommands(userinput)
		else:
			current_command = userinput

main()


