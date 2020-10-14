# How to bash

## The purpose
...

## How does it work?
Every program you run in the command lines has 3 stream, STDIN, STDOUT and STDERR. `>`, `>>`, `2>` and `|` may be used to direct STDOUT and STDERR to other files or programs.
(How to include e.g. python ..)


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
`$ rm [folder|file]` Remove file or folder (use `-rf` flag if there are sub folders/files)<br/>
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
`$ ...`<br/>

TBD: xargs<br/>

### Pipelines (by examples)
TBD: Tutorial at the bottom.<br/>
`$ cat filename | wc -l` The `ẁc` command is typically used in pipelines to count `l`ines or `w`ords.<br/>
`$ ls | head -3 | tail -1` List all files, pass on the top 3, pass on the last 1.<br/>
`$ cat name_age_sex.txt | grep 'Male'` [grep](https://danielmiessler.com/study/grep/) is suitable to filter lines by regular expressions.<br/>
`$ cat name_age_sex.txt | sed 's/E...n/ESPEN/g'`[sed](https://www.tutorialspoint.com/sed/index.htm) is suitable to do string replacements.<br/>
`$ cat name_age_sex.txt | cut -c 4-` Cut the 4th and remaining `c`haracters from each line (alt `1,3`, `1-3`, `-4`).
`$ cat name_age_sex.txt | cut -d "," -f 1,3-4` Specify `d`elimiter and `f`ields. <br/>




`....`<br/>


Useful TBDs: 

uniq https://www.geeksforgeeks.org/uniq-command-in-linux-with-examples/?ref=lbp
filter - hvordan?<br/>
xargs<br/>
find<br/>
sort<br/>


jq<br/>
less<br/>
uniq -c  # Nyttig i pipelines <br/>
yes | apt-get update  # Send yes to any program which requires input<br/>
shell loop constructs<br/>
chmod
....` <br/>

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
