# Utilities

This is a collection of utilities and scripts I've created.

* [run-parts](#run-parts)
* [encrypt-folder](#encrypt-folder)
* [find-wifi-network](#find-wifi-network)
* [get_password_from_keyring](#get_password_from_keyring)

<br>

# run-parts

This is a python script that works similarly to [ `run-parts` ](http://manpages.ubuntu.com/manpages/trusty/man8/run-parts.8.html) from Linux. Given a directory, `run-parts` will execute the files in that directory.

## Why?

I am familiar with `run-parts` from my Ubuntu servers and wanted something similar for my Mac to run my backups (I use [BorgBackup](https://www.borgbackup.org) for my backups).

I use `run-parts.py` on my MacBook and iMac to run my backup scripts regularly via [LaunchAgents](https://www.launchd.info). For instance, I have my own "cron.daily" folder that contains scripts that I want to run daily, such as running the borg backup.

## Usage

```bash
run-parts.py [-n/--dry-run/--test] folder
```

Files are executed in alphabetical order. So, if you want to have the files executed in order, name them as such. e.g. 001-first.sh, 010-second.sh, ..., 999-last.sh.

(I symlink `run-parts.py` to my `~/bin` folder [ `ln -s ~/Utilities/run-parts/run-parts.py ~/bin/run-parts` ] so that I can use `run-parts` rather than typing `run-parts.py` ).

## Flags

* **-n/--dry-run/--test**: will print out what files would be executed instead of running them.

## Ways to Skip Files from Executing

If you don't want all files in a folder to be executed, there are a few ways to make it skip executing the files.

### File is in the Excluded Files List

Near the top of `run-parts.py`, there is a function that returns an array of "ignored files". Currently, this is hard-coded to just .DS_Store since macOS will automatically generate that file. You could modify this to include other files you don't want included.

### Files that Aren't Files (Directories, etc.)

`run-parts` will automatically exclude directories. It should also skip things such as UNIX pipes but I haven't actually tried it on them.

### Files that Aren't Marked as Executable

Files must have the eXectuable flag (chmod +x filename) in order for `run-parts` to execute them. Without the flag, the files will be skipped.

### Specially Named Files (\_disabled)

Files containing '\_disabled' in the name will be skipped. e.g. "100-backup_disabled.sh".

### Files with Special Line (#disabled)

If the second line of a file contains the text #disabled, the file will be skipped. e.g.
```bash
#bin/sh
#disabled
...
...[rest of script here. e.g. rsync -Pav ~/data remote:data]
...
exit 0
```

## Caveats

Unlike `run-parts` from Linux, `run-parts.py` will run all files that are exectuable in the folder. That is, `run-parts.py` doesn't have the restrictions on naming of files. For example, `run-parts` from Linux doesn't support a period (.) in the filename. However, I wanted my scripts to have file extensions, such as .sh; so `run-parts.py` doesn't constrain the filenames.

<br>

# encrypt-folder

This script will take a folder, compress it, and encrypt it with GPG.

## Why?

In addition to using [BorgBackup](https://www.borgbackup.org), I make backups of folders regularly (so that I have my files backed up in more than one format). I use this script to back up and encrypt the folders for storage.

## Usage

``` bash
encrypt-folder.py filename-to-create folder-to-encrypt [gpg-key-id]
```

### Example

``` bash
encrypt-folder.py "~/GPG Backups/Documents" ~/Desktop
```

(I symlink `encrypt-folder.py` to my `\~/bin` folder [ `ln -s ~/Utilities/encrypt-folder/encrypt-folder.py ~/bin/encrypt-folder` ] so that I can use `encrypt-folder` rather than typing `encrypt-folder.py` ).

## Arguments

* **filename-to-create**: The filename to create - the extension .tar.bz.gpg will automatically be added.
* **folder-to-encrypt**: The folder to encrypt.
* **gpg-key-id**: The ID of the GPG key to use to encrypt. This is passed as a shortcut argument to the `gpg` executable. By default, this is my GPG key, josh@brownj.org.

## Caveats

The default GPG key is my key, josh@brownj.org. So, you'll want to use something different for you. :)

<br>

# find-wifi-network

This is a shell script that is an example for how to find the current Wi-Fi access point a Mac is connected to.

## Why?

I want my backups to only run when I'm connected to my home network. So, I have my backup scripts only execute when I'm connected to my home Wi-Fi network.

## Usage

``` bash
export WIFIACCESSPOINT=$(/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}')

if [ $WIFIACCESSPOINT != "<home Wi-Fi access point name>" ] 
then
	echo "not connected to home network, exiting"
	exit 1
fi

#rest of script runs here
```

<br>

# get_password_from_keyring

Gets a password from the macOS Keychain for a given account name. I use it in my backup script to get the secure password from the macOS Keychain for my backups.

## Usage

``` python
accountPassword = get_password_from_keyring("AccountName")
```

<br>

# Public Domain

This project is in the public domain. Copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/). See the LICENSE file in this directory.

All contributions to this project must be released under the same CC0 wavier. By submitting a pull request or patch, you are agreeing to comply with this waiver of copyright interest.

[![License: CC0 1.0 Universal](http://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
