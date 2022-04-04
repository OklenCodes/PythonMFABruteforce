#!/usr/bin/env python3

from hashlib import md5
from string import ascii lowercase
import itertools

counter = 1
while True:
	combinations = intertools.combinations_with_replacement(ascii_lowercase)

	for combo in combinations:
		string = "".join(combo)

		m = md5(string.encode("utf-8"))
		the_hash = m.hexidigest()
		if the_hash.endswith("001"):
			print(string, the_hash)
			exit()
	counter +=1
