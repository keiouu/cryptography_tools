#
# Author: James Thompson
#

from etc import tess27
import random

ciphertext = "CIPHER TEXT HERE"

# Find Frequencies of the 27 letters
alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "|"]

freqs  = map(lambda x: (x, (tess27.txt.count(x) / ((len(tess27.txt) + 0.0))) * 100), alphas)
cipher_freqs  = map(lambda x: (x, (ciphertext.count(x) / ((len(ciphertext) + 0.0))) * 100), alphas)

o_freqs = sorted(freqs, key=lambda a: a[1])
o_cipher_freqs = sorted(cipher_freqs, key=lambda a: a[1])

alphabet = [x[0] for x in o_freqs]
cipherbet = [x[0] for x in o_cipher_freqs]

# Substitute
strout = ""
for l in ciphertext:
	pos = cipherbet.index(l)
	strout = strout + alphabet[pos]
print strout