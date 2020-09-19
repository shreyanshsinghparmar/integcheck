import sys
import hashlib

def usage():
	print('''Check integrity of files
	Usage: integcheck.py [-h] [INPUT FILE] [CORRECT HASH]
	INPUT FILE: File to check the integrity of
	CORRECT HASH: File containing the correct hash of the given file
	-h or --help: Display this message
	''')

def md5():

def sha256():

if __name__ == "__main__":
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		usage()
	else: