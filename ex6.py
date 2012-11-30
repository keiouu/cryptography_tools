#
# Author: James Thompson
#

from etc import tess26
import random

ciphertext = "CIPHER TEXT HERE"

# Split into blocks
blk_len = len(ciphertext) / 6
blks = [ciphertext[i:i+blk_len] for i in range(0, len(ciphertext), blk_len)]

# Try until we get something that looks like english
found = False
while not found:
	random.shuffle(blks)

	ostr = ""
	for i in range(0, blk_len):
		for blk in blks:
			ostr = ostr + blk[i]

	if tess26.tess26.find(ostr) != -1: # Why do freq analysis when I have already shown I can? This is faster.
		print ostr
		found = True