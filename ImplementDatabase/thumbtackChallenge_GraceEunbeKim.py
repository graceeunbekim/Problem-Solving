# Author: Grace Eunbe Kim
# Contact: eunbegracekim40@gmail.com
# Thumbtack Remote Programming Challenge
# Simple DataBase Challenge

import sys

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

class Commands:
	"""	
	Class for commands received through standard input that are
	later used for the Transaction and Data classes for the database
	execution. Transaction and Data classes overrides setVal(), getVal(),
	unsetVal(), and endProgram().
	"""

	def __init__(self, d={}):
		self.d = d

	def setVal(self, name, value):
		"""overrides setVal() function in Commands abstract class."""
		d = self.d
		d[name] = value

	def getVal(self, name):
		"""overrides getVal() function in Commands abstract class."""
		try: 
			d = self.d
			if (name in d.keys()):
				sys.stdout.write(d[name])
			else:
				sys.stdout.write(NULL)
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


class Data:
	"""
	Data class inherits from the abstract class Commands for the core
	exceutions and its own exceution 'NUMEQUALTO'.
	"""
	def __init__(self, d={}):
		self.d = d

	def runNumberQualTo(self, value):
		""" Print out the number of variables that are currently set to value. 
		    If no variables equal that value, print 0"""
		d = self.d
		count = 0
		try:
			for k,v in d.items():
				if (value == v):
					count += 1
			print count
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e

class Transaction:
	"""
	Transaction class inherits from the abstract class Commands for the core
	exceutions and its own exceutions such as 'COMMIT', 'BEGIN', and 'ROLLBACK'.
	"""
	def __init__(self, d={}):
		self.d = d

	def begin(self, stack):
		"""Open a new transaction block. Transaction blocks can be nested; 
		   a BEGIN can be issued inside of an existing block."""
		pass

	def rollback(self, dictionary, old_commands):
		"""Undo all of the commands issued in the most recent transaction block, 
		   and close the block. Print nothing if successful, 
		   or print NO TRANSACTION if no transaction is in progress."""

		if (len(old_commands.keys()) == 0):
			sys.stdout.write(NOTRANSAC)
		else:
			try:
				# UPDATE THE DATABASE TO THE OLD ONE
				dictionary = old_commands
				print old_commands
				print self.d

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


class Factory:
	""" factory of command executions. """

	def main(self):
		""" main() function to instantiate two classes for Data and Transaction commands.
			standard input is read until END is input; otherwise, program
			executes and displays the output of the commands. """

		current_command = None
		d = {}
		old_commands = {}
		old_tables = []

		while True:
			commands = Commands(d)
			dataCommand = Data(d)
			tranCommand = Transaction(d)

			userinput = sys.stdin.readline().rstrip('\n')#.split(' ')
			words = userinput.split(' ')


			# execution ends
			if userinput == END:
				break

			# detect commands for command class
			if (words[0] == SET):
				commands.setVal(words[1], words[2])

			elif (words[0] == GET):
				commands.getVal(words[1])

			elif (words[0] == UNSET):
				commands.unsetVal(words[1])

			# detect commands for data class
			elif (words[0] == NUMEQUALTO):
				dataCommand.runNumberQualTo(words[1])

			# detect commands for transaction class
			elif (userinput == BEGIN):
				old_tables.append(d.copy())				
				#old_commands = d.copy()
				print old_tables
			
			elif (userinput == ROLLBACK):
				#tranCommand.rollback(d, old_commands)
				old_commands = old_tables.pop()
				if (old_commands == d):
					sys.stdout.write(NOTRANSAC)
				else:
					d = old_commands

			elif (userinput == COMMIT):
				old_commands = d
		
			else:
				current_command = userinput
				print INCORRECT

f = Factory()
f.main()


