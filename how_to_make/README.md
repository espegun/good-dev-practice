# How to Makefile

## The purpose
Simple automation tool, typically for compiling and setting up projects. The key difference against normal bash-shell is that it only rebuilds files which needs to be rebuilt, because other files they depend on has been updated (newer than themselves).

An example of use is to first `make build` a Docker image, run the tests __in the container__ and then `make deploy` the image to some production environment. 

## How does it work?
Builds from the end output and works backwards, rebuilding any dependencies if the source is newer than the existing target file. This could save a lot of time in large projects.

A Makefile consist of a set of RULES, which generally looks like the below. The target may be a file or simply just a name for a rule, a "phoney target" (if s

All variables are strings.

## Useful commands
`target : prerequisites`  # There may be (typically) one or more targets, none or more prereq files, separated by space.
`<TAB> command`
`<TAB> command`

`.PHONY` The prerequisites will be run without , <br/>

`$ make`  # Runs the file<br/>
`$ make targetname`  # Makes this specific <br/>

`PYTHON := python3.7`  # How to set a variable<br/>
`@echo ${PYTHON}`

`VARNAME ?= something`  # Assign a value to a variable if not already defined.

## Useful links
[How to makefile](https://opensource.com/article/18/8/what-how-makefile)<br/>
[Introduction](http://www.gnu.org/software/make/manual/html_node/Introduction.html)<br/>
[makefiletutorial](https://makefiletutorial.com/)<br/>



