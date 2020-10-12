# How to Makefile

**TBD! Check the top TBD link at the bottom**<br/>

## The purpose
Simple automation tool, typically for compiling and setting up projects. The key difference against normal bash-shell is that it only rebuilds files which needs to be rebuilt, because other files they depend on has been updated (newer than themselves).

An example of use is to first `make build` a Docker image, run the tests **in the container** and then `make deploy` the image to some production environment. 

## How does it work?
Builds from the end output and works backwards, rebuilding any dependencies if the source is newer than the existing target file. This could save a lot of time in large projects.

A Makefile consist of a set of RULES, which generally looks like the below. The target may be a file or simply just a name for a rule, a "phoney target" (if s

All variables are strings.

If a `make something` command doesn't work, try to run commands in the terminal and recreate it there. 


## Useful commands
`target : prerequisites`  # There may be (typically) one or more targets, none or more prereq files, separated by space.
`<TAB> command`
`<TAB> command`

`.PHONY` The prerequisites will be run without checking dependencies.<br/>

`$ make`  # Runs the file<br/>
`$ make targetname`  # Makes this specific <br/>

`PYTHON := python3.7`  # How to set a variable, here which Python version should be used. May also use e.g. `python3`<br/>
`$(GLOBAL_PY) -m venv $(BUILD_VENV)`  Then use the variable for actual commands.GLOBAL_PY := python3
BUILD_VENV ?= .build_venv
BUILD_PY := $(BUILD_VENV)/bin/python

.PHONY: init
init: $(BUILD_VENV)

$(BUILD_VENV):
	$(GLOBAL_PY) -m venv $(BUILD_VENV)

`@echo ${PYTHON}`



`VARNAME ?= something`  # Assign a value to a variable if not already defined.


TBD: `is-git-clean`

## Useful links
[Start with this tutorial!](https://opensource.com/article/18/8/what-how-makefile)<br/>
[How to makefile](https://opensource.com/article/18/8/what-how-makefile)<br/>
[Introduction](http://www.gnu.org/software/make/manual/html_node/Introduction.html)<br/>
[makefiletutorial](https://makefiletutorial.com/)<br/>
https://medium.com/free-code-camp/makefiles-101-how-to-use-make-as-a-task-automation-tool-69d2ccc3f25e <br/>



# Fra Makefile til Køtid
GLOBAL_PY := python3
BUILD_VENV ?= .build_venv
BUILD_PY := $(BUILD_VENV)/bin/python

.PHONY: init
init: $(BUILD_VENV)

$(BUILD_VENV):
	$(GLOBAL_PY) -m venv $(BUILD_VENV)
