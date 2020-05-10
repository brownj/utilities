# Utilities

This is a collection of utilities and scripts I've created.

# run-parts

I made a python script that works similarly to [run-parts](http://manpages.ubuntu.com/manpages/trusty/man8/run-parts.8.html) from Linux. 

## Why?

I am familiar with run-parts from my Ubuntu servers and wanted something similar for my Mac to run my backups (I use [BorgBackup](https://www.borgbackup.org) for my backups).

So, I use this run-parts.py utility on my MacBook and iMac to run my backup scripts regularly via [LaunchAgents](https://www.launchd.info).

## Usage

```bash
run-parts [--test] folder
```

## Flags

* --test: will print out what files would be executed instead of running them.

## Caveats

Unlike run-parts from Linux, this script will run all files that are exectuable in the folder. That is, it doesn't have the restrictions on naming of files (e.g. run-parts from Linux doesn't support a period (.) in the filename, for instance, but, I wanted my scripts to have file extensions, such as .sh; so run-parts.py doesn't constrain the filenames).

## Contributing
Pull requests are welcome.

This project is public domain (using the Unlicense [see license below]).

For anyone contributing to this, your contribution will also be public domain. If you are not comfortable with that and want something changed, please create an issue and I will try to fix it myself.

## License
[Unlicense](https://unlicense.org)