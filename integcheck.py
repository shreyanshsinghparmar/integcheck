import sys
import hashlib

def usage():
	print('''Check integrity of files
	Usage: integcheck.py [-h] [INPUT FILE] [CORRECT HASH]
	INPUT FILE: File to check the integrity of
	CORRECT HASH: File containing the correct hash of the given file
	-h or --help: Display this message
	''')

def md5(file):
	output = hashlib.md5()
	with open(file, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			output.update(chunk)
	return output.digest()


def sha256(file):
	output = hashlib.sha256()
	with open(file, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			output.update(chunk)
	return output.digest()


if __name__ == "__main__":
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		usage()
	else:
		print('''List of available hash algorithms:
			MD5
			SHA256
		Enter your choice:
		''', end=' ')
		algo = input()
		algo = algo.upper()
		file = sys.argv[1]
		hash = sys.argv[2]
		if algo == "MD5":
			out = md5(file)
		elif algo == "SHA256":
			out = sha256(file)
		ok = True
		with open(hash, 'r') as f:
			actual_hash = f.read().replace('\n', '')
		if actual_hash == out:
			print("File is original")
		else:
			print("File has been tampered")