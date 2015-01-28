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
	Commands class implements setVal(), getVal(), and unsetVal() and after
	SET execution, it stores the name and the value into a dictionary.
	"""

	def __init__(self, d={}):
		self.d = d

	def setVal(self, name, value):
		"""Set the variable name to the value value. 
		   Neither variable names nor values will contain spaces."""
		d = self.d
		d[name] = value

	def getVal(self, name):
		"""Print out the value of the variable name, 
		   or NULL if that variable is not set."""
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
		"""Unset the variable name, making it just like that variable was never set."""
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
	Data class implements 'NUMEQUALTO', which appears only in Data Commands.
	"""
	def __init__(self, d={}):
		self.d = d

	def runNumberQualTo(self, value):
		""" standard output for the number of variables that are currently set to value. 
		    If no variables equal that value, writes 0"""
		d = self.d
		count = 0
		try:
			for k,v in d.items():
				if (value == v):
					count += 1
			sys.stdout.write(str(count))
		except KeyError, e:
			print e
		except IndexError, e:
			print e
		except Exception, e:
			print e

class Transaction:
	"""
	Transaction class implements its own exceutions such as 'COMMIT', 'BEGIN', and 'ROLLBACK'.
	"""
	def __init__(self, d={}):
		self.d = d

	def begin(self, current_table, old_tables):
		"""Open a new transaction block. Transaction blocks can be nested; 
		   a BEGIN can be issued inside of an existing block."""
		old_tables.append(current_table)


	def rollback(self, dictionary, old_commands):
		"""Undo all of the commands issued in the most recent transaction block, 
		   and close the block. Print nothing if successful, 
		   or print NO TRANSACTION if no transaction is in progress."""

		pass

	def commit(self, stack):
		"""Close all open transaction blocks, permanently applying the 
		   changes made in them. Print nothing if successful, 
		   or print NO TRANSACTION if no transaction is in progress."""
		pass


class Factory:
	""" factory of command executions. """

	def main(self):
		""" main() function to instantiate all classes for Data and Transaction commands.
			standard input is read until END is input; otherwise, program
			executes and displays the output of the commands. 

			While standard inout is not END, each execution calls the corresponding function
			to mimic the database commands. """

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
				#old_tables.append(d.copy())				
				#print old_tables
				tranCommand.begin(d.copy(), old_tables)
			
			elif (userinput == ROLLBACK):
				if (len(old_tables) == 0):
					sys.stdout.write(NOTRANSAC)
				else:
					old_commands = old_tables.pop()
					if (old_commands == d):
						sys.stdout.write(NOTRANSAC)
					else:
						d = old_commands

			elif (userinput == COMMIT):
				#old_commands = d
				old_tables = []
		
			else:
				current_command = userinput
				print INCORRECT

f = Factory()
f.main()


