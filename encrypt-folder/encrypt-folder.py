#!/usr/bin/env python

def main():
	import sys, os, subprocess

	if (len(sys.argv) < 3):
		print("usage: encrypt-folder.py filename-to-save folder-to-encrypt [gpg-key-id]")
		sys.exit(1)

	filename = sys.argv[1]
	folder = sys.argv[2]

	gpgkey = 'josh@brownj.org'
	if (len(sys.argv) == 4):
		gpgkey = sys.argv[3]

	if not filename.endswith('.tar.bz2'):
			filename = filename + '.tar.bz2'

	if not os.path.exists(folder):
		print("path doesn't exist")
		exit

	bz2filename = filename #folder.rstrip('/') + '.tar.bz2'

	print("making tarball of " + folder + ". . .")

	subprocess.call([
		'/usr/bin/tar',
		'cfj',
		bz2filename,
		folder
		])

	print("tarball created.")
	print("encrypting tarball")

	subprocess.call([
		'/usr/local/MacGPG2/bin/gpg',
		'--encrypt',
		'--recipient', gpgkey,
		bz2filename
		])

	subprocess.call([
		'/bin/rm',
		bz2filename
		])

	print("encryption finished.")


if __name__ == "__main__":
	main()
