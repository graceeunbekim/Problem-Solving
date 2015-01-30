# Author: Grace Eunbe Kim
# Contact: eunbegracekim40@gmail.com
# Thumbtack Remote Programming Challenge
# Simple DataBase Challenge

How to run the file
---------------------------------------
run following commands on console:
	python thumbtackChallenge_GraceEunbeKim.py


then, start typing the database commands
BEGIN
SET a 10
GET a
10 <- results will be printed out as a standard output right after you run the GET, NUMEQUALTO.

to exit the program, please enter following:
END


Requirements
---------------------------------------
if following requirements are not followed, the program 
immediately prints out the INCORRECT error meesage that 
is defined in the class.

1. database commands are case-sensitive.
	i.e. GET is ok but get, Get, gEt, geT, GEt, gET are invalid.
2. lower case is considered as a incorrected formatted command.
3. SET requires 2 following variables, name and value.
4. GET, NUMEQUALTO, UNSET needs 1 variable following the command.
5. END, COMMIT, ROLLBACK, BEGIN don't need argument.
6. all the other commands are invalid.
