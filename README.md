# Utilities

This is a project containing utilities and scripts I've created.

# run-parts

I made a python script that works similarly to [run-parts](http://manpages.ubuntu.com/manpages/trusty/man8/run-parts.8.html) from Linux. 

## Why?

I am familiar with run-parts from my Ubuntu servers and wanted something similar for my Mac to run my backups (I use [BorgBackup](https://www.borgbackup.org) for my backups).

So, I use this run-parts.py utility on my MacBook and iMac to run my backup scripts regularly via [LaunchAgents](https://www.launchd.info).

## Usage

```bash
run-parts [--test] folder
```

### Flags

* --test: will print out what files would be executed instead of running them.

### Caveats

Unlike run-parts from Linux runs all the files that are exectuable in the folder will run.

## Contributing
Pull requests are welcome.

## License
[Unlicense](https://unlicense.org>)