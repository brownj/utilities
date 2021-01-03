#!/usr/bin/env python3

# Similar to run-parts from debian
# Executes all scripts in a given folder
# But it doesn't care if files have dots or special characters in filenames.

def excludedfilenames():
	return [ '.DS_Store' ]

def main():
	import sys, os, subprocess
	from itertools import islice

	if (len(sys.argv) < 2):
		print("Usage: run-parts.py [-n/--dry-run/--test] folder")
		sys.exit(1)

	folder = os.path.abspath(sys.argv[1])
	testmode = False
	excludedfiles = excludedfilenames()

	if (sys.argv[1] == "-n" or sys.argv[1] == "--dry-run" or sys.argv[1] == "--test"):
		if (len(sys.argv) != 3):
			print("Usage: run-parts.py [-n/--dry-run/--test] folder")
			sys.exit(2)
		testmode = True
		folder = os.path.abspath(sys.argv[2])

	if not os.path.exists(folder):
		print(f"Path [{folder}] doesn't exist.")
		sys.exit(3)

	filesarr = os.listdir(folder)
	filesarr = sorted(filesarr)
	
	for file in filesarr:
		absfile = os.path.join(folder,file)
		skip = ""

		if file in excludedfiles:
			# skip things in excluded file list
			skip = "excluded"

		elif not os.path.isfile(absfile):
			# skip things that aren't files (i.e. folders)
			skip = "not-file"

		elif not os.access(absfile, os.X_OK):
			# skip things not executable
			skip = "not-exectuable"
		
		elif ("_disabled" in absfile):
			# skip if _disabled in the filename
			skip = "disabled via filename"

		else:
			with open(absfile) as fin:
				for line in islice(fin, 1, 2):
					if ("#disabled" in line):
						skip = "disabled via line 2"
		
		if testmode:
			if (len(skip) == 0):
				print("would run:  " + absfile)
			else:
				print("would skip: " + absfile + f" [reason: {skip}]")
		else:
			if (len(skip) == 0):
				print("running: " + absfile)
				subprocess.call( [ absfile ] )
			else:
				print("skipped: " + absfile + f" [reason: {skip}]")

	sys.exit(0)


if __name__ == "__main__":
	main()
