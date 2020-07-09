# .DEFAULT_GOAL := generate  # Overrides default first target
.PHONY: all say_hello generate clean  # All these are phony and will be run regardsless of wheter a file with that name exists

PYTHON := python3.7  # How to set a variable
ANIMAL := hund

all: say_hello generate

say_hello:
	@echo "Howdy!"

generate:
	@echo "Creating empty text files..."
	touch file-{1..10}.txt  # This works in command line, but not as a part of the Makefile

clean:
	@echo "Cleaning up..."
	rm *.txt

show_python_ver:
	@echo ${PYTHON}  # How to reference a variabl

set_animal:
	@echo "Setting an animal"	
	# ANIMAL := hund
	ANIMAL ?= katt
	@echo ${ANIMAL}



