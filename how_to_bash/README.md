# How to bash

## The purpose
Do great stuff in the bash terminal!

## How does it work?
Every program you run in the command lines has 3 stream, STDIN, STDOUT and STDERR. `>`, `>>`, `2>` and `|` may be used to direct STDOUT and STDERR to other files or programs.

## Useful commands

### Generic
`$ [command] --help` Always useful TBD: WALK THROUGH SEVERAL OF THE BELOW COMMANDS - EXPLAINS IT QUITE WELL! E.g. `touch cat`<br/>
`$ [command] -flag` Set flag true, default is false <br/>
`$ sudo` super user do <br/>
*Ctrl + C*  Terminate the running program<br/>
*Ctrl + Shift + C|V* Copy/Paste

### Folders and paths
`$ pwd` Print working directory
`$ ls [option] [file|dir]` List folder content. For details, see [ls command](https://www.rapidtables.com/code/linux/ls.html)<br/>
`$ cd [dir]` Examples `/abs/folder`, `rel/folder`, `~` (home), `-` (previous dir). For details, see [cd command](https://www.rapidtables.com/code/linux/cd.html)<br/>
`$ mkdir my_dir` Create a directory.<br/>
`$ rm [folder|file]` Remove file or folder (use `-rf` flag if there are sub folders/files. Useful to clean up test and build environments for a clean start, e.g. `rm -rf .build_venv .tox`)<br/>
`$ ....` <br/>
`$ cp source destination` Copy a file.<br/>
`$ mv source destination` Move (and/or rename) a file.<br/>

### Various basic
`$ clear` Clear screen.<br/>
`$ echo text` Print string.<br/>
`$ touch filename` Initiate an empty file.<br/>
`$ cat filename1 (filename2)` The content of one or more file sent to the standard output.<br/>
`$ less filename` Displays file content, but always you to scroll forwards using **space** or backwards using **b**.<br/>
`$ [cmd] > filename` Redirect output from STDOUT (printing) to a file (use `>>` to append). The format is typically changed to by line.<br/> 
`$ export ENVVAR=100` Temporary environment varible. Use `~/.bashrc` or `~/.profile` to set as persistant.<br/>
`$ echo $ENVVAR` How to read (and in this case print) an environment variable.<br/>
`$ seq 1 10` Prints `1` to `10`. Input to pipeline?<br/>
`$ find . -name "*.py"` Recursively search from a starting folder. See [examples](https://www.geeksforgeeks.org/find-command-in-linux-with-examples/).<br/>
*TBD* `jq` parse json lines and files.<br/>

### Pipelines (by examples)
TBD: Tutorial at the bottom.<br/>
`$ cat filename | wc -l` The `ẁc` command is typically used in pipelines to count `l`ines or `w`ords.<br/>
`$ ls | head -3 | tail -1` List all files, pass on the top 3, pass on the last 1.<br/>
`$ cat name_age_sex.txt | grep 'Male'` [grep](https://danielmiessler.com/study/grep/) is suitable to **filter** lines by regular expressions.<br/>
`$ cat name_age_sex.txt | sed 's/E...n/ESPEN/g'`[sed](https://www.tutorialspoint.com/sed/index.htm) is suitable to do string replacements.<br/>
`$ cat name_age_sex.txt | cut -c 4-` Cut the 4th and remaining `c`haracters from each line (alt `1,3`, `1-3`, `-4`).
`$ cat name_age_sex.txt | cut -d "," -f 1,3-4` Specify `d`elimiter and `f`ields (or `-b` for bytes/chars). <br/>
`$ cat name_age_sex.txt | cut -d "," -f 3 | uniq -u` Return only `u`nique entries.<br/>
`$ cat name_age_sex.txt | cut -d "," -f 3 | sort | uniq -c` Count number of time an entry is repeated *in sequence*, pre-sort to count total.<br/>
`$ cat name_age_sex.txt | cut -d "," -f 1 | xargs touch` xargs can be used with functions which requires arguments, not just input.<br/>
`$ find *.txt | xargs cat` Dump all the content of the test files.<br/>
`$ cat name_age_sex.txt | xargs -n 2 echo` Use `-n` to specify number of arguments passed. `echo` may take any number, but will now print the *two first input lines* in *one line*.<br/>
`cat name_age_sex.txt | cut -d "," -f 2 | xargs -n 1 sh -c 'python add_years.py "$@" 10' sh` Combine `xargs` with `sh -c 'some_command' sh` to make advanced inputs.`<br/>

## Useful links
[Ubuntu command line at Tutorialspoint](https://www.tutorialspoint.com/ubuntu/ubuntu_command_line.htm)<br/>
https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)<br/> 
[Great overview of commands](https://medium.com/@duruldalkanat/bash-commands-guide-129c81cbfe87)<br/>
TBD: Also see various commands at DS123<br/>
Pipelines https://ryanstutorials.net/linuxtutorial/piping.php<br/>
TBD: jq in commandline (sed for json) [jq](https://stedolan.github.io/jq/)<br/>
TBD: https://shapeshed.com/jq-json/
[Python and pipelines](https://docs.python.org/3/library/pipes.html)<br/>
https://pymotw.com/3/subprocess/<br/>
https://www.tutorialspoint.com/python3/os_popen.htm<br/>
