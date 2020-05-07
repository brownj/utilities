#!/usr/bin/env python3

# Similar to run-parts from debian
# Executes all scripts in a given folder
# But it doesn't care if files have dots or special characters in filenames.

def excludedfilenames():
	return [ '.DS_Store' ]

def main():
	import sys, os, subprocess

	if (len(sys.argv) < 2):
		print("Usage: run-parts.py [--test] folder")
		sys.exit(1)

	folder = os.path.abspath(sys.argv[1])
	testmode = False
	excludedfiles = excludedfilenames()

	if (sys.argv[1] == "--test"):
		if (len(sys.argv) != 3):
			print("Usage: run-parts.py [--test] folder")
			sys.exit(2)
		testmode = True
		folder = os.path.abspath(sys.argv[2])

	if not os.path.exists(folder):
		print(f"Path [{folder}] doesn't exist.")
		sys.exit(3)

	filesarr = os.listdir(folder)
	
	for file in filesarr:
		absfile = os.path.join(folder,file)

		if file in excludedfiles:
			# skip things in excluded file list
			continue

		if not os.path.isfile(absfile):
			# skip things that aren't files (i.e. folders)
			continue

		if not os.access(absfile, os.X_OK):
			# skip things not executable
			continue

		if testmode:
			print("would run: " + absfile)
		else:
			print("running: " + absfile)
			subprocess.call([
				absfile
			])

	sys.exit(0)


if __name__ == "__main__":
	main()
