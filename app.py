import os
import random
import search
import jsonParser
from time import sleep 
items = {}
'''if fatt == 1:
	exit(1)
sleep(4)'''
s = 0
hashes = jsonParser.jsonParser('fatt/fatt.log')
fp = open("trainingSet/trainingDataset.text","r")
lines = fp.readlines()
lines.pop(-1)
for line in lines:
	if line == '\n':
		continue
	word = line.rstrip('\n').split()
	items[word[0]] = word[1]
for hash in hashes:
	r = random.randint(0,2)
	if hash in items:
		print("%s:%s"%(hashes[hash],items[hash]))
	else:
		s = search.find(hash)
		if s == 1:
			print("%s"%(hashes[hash]))
			fp.write(hashes[hash])
		else:
			print("%s:Not a threat"%(hashes[hash]))








