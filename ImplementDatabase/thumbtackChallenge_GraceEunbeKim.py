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
NOTRANSAC  = "NO TRANSACTION"
DATABASE   = {}

class Commands:
	"""	
	Abstraction class for Commands received through standard input that are
	later used for the Transaction and Data classes for the database
	execution. Transaction and Data classes overrides setVal(), getVal(),
	unsetVal(), and endProgram().
	"""
	def __init__(self):
		self.d = DATABASE
		self.vals = []

	def setVal(self, name, value):
		"""overrides setVal() function in Commands abstract class."""
		d = self.d
		vals = self.vals

		vals.append(value)
		d[name] = vals	

	def getVal(self, name):
		"""overrides getVal() function in Commands abstract class."""
		try: 
			d = self.d
			if (name in d.keys()):
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
		d = self.d
		try:
			if (name in d.keys()):
				del d[name]
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e


class Data(Commands):
	"""
	Data class inherits from the abstract class Commands for the core
	exceutions and its own exceution 'NUMEQUALTO'.
	"""

	def __init__(self):
		self.d = DATABASE
		self.vals = []

	def runNumberQualTo(self, value):
		""" Print out the number of variables that are currently set to value. 
		    If no variables equal that value, print 0"""
		d = self.d
		count = 0
		try:
			for k,v in d.items():
				if (value in v):
					count += 1
			print count
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e

class Transaction(Commands):
	"""
	Transaction class inherits from the abstract class Commands for the core
	exceutions and its own exceutions such as 'COMMIT', 'BEGIN', and 'ROLLBACK'.
	"""

	def __init__(self):
		self.d = DATABASE
		self.vals = []

	def begin(self):
		"""Open a new transaction block. Transaction blocks can be nested; 
		   a BEGIN can be issued inside of an existing block."""
		pass

	def rollback(self, stack):
		"""Undo all of the commands issued in the most recent transaction block, 
		   and close the block. Print nothing if successful, 
		   or print NO TRANSACTION if no transaction is in progress."""
		d = self.d

		if (len(stack) == 0):
			print NOTRANSAC
		else:
			last_commend = stack.pop()
			words = last_commend.split(' ')
			print last_commend

			try:
				if (words[1] in d.keys()):
					del d[words[1]][-1]
			except KeyError, e:
				print e
			except IndexError, e:
				print e
			except Exception, e:
				print e

	def commit(self, stack):
		"""Close all open transaction blocks, permanently applying the 
		   changes made in them. Print nothing if successful, 
		   or print NO TRANSACTION if no transaction is in progress."""
		stack = []


def displayOutput(result):
	"""

	"""
	sys.stdout.write(result)

def main():
	""" main() function to instantiate two classes for Data and Transaction commands.
		standard input is read until END is input; otherwise, program
		executes and displays the output of the commands. """
	current_command = None
	dataCommand = Data()
	tranCommand = Transaction()
	stack = []

	while True:
		userinput = sys.stdin.readline().rstrip('\n')#.split(' ')
		words = userinput.split(' ')
		
		if userinput == END:
			break

		# detect commands for data class
		if (words[0] == SET):
			dataCommand.setVal(words[1], words[2])

		elif (words[0] == GET):
			dataCommand.getVal(words[1])

		elif (words[0] == NUMEQUALTO):
			dataCommand.runNumberQualTo(words[1])

		elif (words[0] == UNSET):
			dataCommand.unsetVal(words[1])

		# detect commands for transaction class
		elif (userinput == BEGIN):
			pass
		
		elif (userinput == ROLLBACK):
			tranCommand.rollback(stack)

		elif (userinput == COMMIT):
			tranCommand.commit
	
		else:
			current_command = userinput
			print INCORRECT

		stack.append(userinput)

main()


