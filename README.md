# Utilities

This is a collection of utilities and scripts I've created.

* [run-parts](#run-parts)
* [encrypt-folder](#encrypt-folder)

# run-parts

This is a python script that works similarly to [`run-parts`](http://manpages.ubuntu.com/manpages/trusty/man8/run-parts.8.html) from Linux. Given a directory, `run-parts` will execute the files in that directory.

## Why?

I am familiar with `run-parts` from my Ubuntu servers and wanted something similar for my Mac to run my backups (I use [BorgBackup](https://www.borgbackup.org) for my backups).

I use `run-parts.py` on my MacBook and iMac to run my backup scripts regularly via [LaunchAgents](https://www.launchd.info). For instance, I have my own "cron.daily" folder that contains scripts that I want to run daily, such as running the borg backup and syncing files between the MacBook and iMac.

## Usage

```bash
run-parts.py [--test] folder
```
(I symlink `run-parts.py` to my `\~/bin` folder [`ln -s ~/Utilities/run-parts/run-parts.py ~/bin/run-parts`] so that I can use `run-parts` rather than typing `run-parts.py`).

## Flags

* **--test**: will print out what files would be executed instead of running them.

## Caveats

Unlike `run-parts` from Linux, `run-parts.py` will run all files that are exectuable in the folder. That is, `run-parts.py` doesn't have the restrictions on naming of files. For example, `run-parts` from Linux doesn't support a period (.) in the filename. However, I wanted my scripts to have file extensions, such as .sh; so `run-parts.py` doesn't constrain the filenames.



# encrypt-folder

This script will take a folder, compress it, and encrypt it with GPG.

## Why?

In addition to using [BorgBackup](https://www.borgbackup.org), I make backups of folders regularly (so that I have my files backed up in more than one format). I use this script to back up and encrypt the folders for storage.

## Usage

```bash
encrypt-folder.py filename-to-create folder-to-encrypt [gpg-key-id]
```
### Example
```bash
encrypt-folder.py "~/GPG Backups/Documents" ~/Desktop
```
(I symlink `encrypt-folder.py` to my `\~/bin` folder [`ln -s ~/Utilities/encrypt-folder/encrypt-folder.py ~/bin/encrypt-folder`] so that I can use `encrypt-folder` rather than typing `encrypt-folder.py`).

## Arguments

* **filename-to-create**: The filename to create - the extension .tar.bz.gpg will automatically be added.
* **folder-to-encrypt**: The folder to encrypt.
* **gpg-key-id**: The ID of the GPG key to use to encrypt. This is passed as a shortcut argument to the `gpg` executable. By default, this is my GPG key, josh@brownj.org.

## Caveats

The default GPG key is my key, josh@brownj.org. So, you'll want to use something different for you. :)

# Contributing
Pull requests are welcome.

This project and utilities are public domain (using the Unlicense [see license below](#license)).

For anyone contributing to this, your contribution will also be public domain. If you are not comfortable with your code being public domain, please create an issue. I will fix the issue and it will be public domain.

## License
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](https://unlicense.org/)
