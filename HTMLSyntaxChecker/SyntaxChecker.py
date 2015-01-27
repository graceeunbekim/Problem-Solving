import os
import Queue

SUCCESS = "OK"
BAD_CHARATER = "bad character in tag name."
BAD_LENGTH = "too many/few characters in tag name."
NO_CLOSING_TAG = "expected </xxxxxxxxxx>"
NO_BEGIN_TAG = "no matching begin tag."
BAD_FILE_FORMAT = "bad file format. check the length"

def parse_file():
	f = open('test_case2.txt')
	l = [l for l in f.readlines() if l.strip()]
	f.close()

	if (l[0] != len(l)):
		return BAD_FILE_FORMAT

	if (len(l) == 0):
		return

	if (l == None):
		return

	q = Queue.Queue()
	for i in range(0, len(l)):
		for j in range(0, len(i)):
			if i[j] == "<":


	return brackets


def determine_error():
	q = Queue.Queue()
	brackets = parse_file()

	for i in brackets:
		q.put(i)

	return 