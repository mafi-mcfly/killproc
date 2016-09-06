# killproc
Every developer who just wants to write a little script that uses multiple threads
knows the pain of debugging. Often, when the script crashes, he needs to do:
- ps ax | grep *process name*
- copy the pid
- kill *pid*

This script provides a periodically refreshed numbered list of processes filter
by a specified filter string. The user can then simply enter the number in order
to kill the corresponding process, making all the steps above obsolete. The
script is tested with OS X and Ubuntu 15.10, but should work on any Unix like
system.

# Installation
This script needs no installation. However, a user might want to copy/link it to
a folder contained in the PATH variable. For example:
*ln -s killproc.py /usr/local/bin/killproc*

# Usage
Since the number of features of this script are limited, the usage is quite simple.
The following table lists the commands and their functions.


| Command | Function                                       |
| :------ | :--------------------------------------------- |
| ESC     | Quit the script                                |
| ENTER   | Enter a new process name filter                |
| 1-9     | Kill the process with the corresponding number |

A maximum of 9 processes is listed. If the process you are looking for is not
in the list refine your filter string.
