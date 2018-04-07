#!/bin/python
from random import *
from string import ascii_lowercase
import random
import string

#generation ten lowercase and printout
def generate():
	return ''.join([random.choice(string.ascii_lowercase) for n in xrange(10)])

#write into a file with \n in the end
def write_files(n):
	a=0
	name=['file1.txt','file2.txt','file3.txt']
	while a < n :
		f = open(name[a],'w+')
		line = generate()
		print line
		s = str(line)
		s = s+ "\n"
		#print s
		f.write(s)
		f.close()
		a = a + 1

write_files(3)

def rand_num():

	a = randint(1,42)
	print a
	b = randint(1,42)
	print b
	c = a*b
	print c

rand_num()
