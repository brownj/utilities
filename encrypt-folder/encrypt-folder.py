#!/usr/bin/env python3

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

	if not filename.endswith('.tar.xz'):
			filename = filename + '.tar.xz'

	if not os.path.exists(folder):
		print("path doesn't exist")
		exit

	print("making tarball of " + folder + ". . .")

	# tar args
	#    a- (--auto-compress) auto-detect compression format based on filename.
	#    c- (--create) create mode
	#    h- (--deference, also -L) follow symlinks to save files instead of symlinks
	#    f- (--file) write to file instead of stdout
	subprocess.call([
		'/usr/bin/tar',
		'acfh',
		filename,
		folder
		])

	print("tarball created.")
	print("encrypting tarball")

	subprocess.call([
		'/usr/local/bin/gpg',
		'--encrypt',
		'--sign',
		'--recipient', gpgkey,
		filename
		])

	subprocess.call([ '/bin/rm', filename ])

	print("encryption finished.")


if __name__ == "__main__":
	main()
