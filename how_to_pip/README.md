# How to pip

## The purpose
The most commonly used tool to download and install python packages (preferably in a venv) from PyPI (Python Package Index, pypi.org).

pip-compile is helpful in separating direct and sub dependencies, but - how to uninstall obsolete sub dependencies? And even if versions are specified in requirements.in, will the list in requirements.txt be consistent over time?

## How does it work?
Start by making sure you always have an updated version of pip, setuptools and wheel. 
Remember that pip3 updates only one of your potentially many global Python-distributions or venvs, be conscious about which you target. Generally it is preferable to run pip as a module with a defined python-version, e.g. `$ python37 -m pip <something>`.
Generally keep global installations pristine and install in venvs.
pip3 is the Python3 version of pip, organized the same way as python, so `pip` may be a softlink to pip3.X. 

## Useful commands
`$ apt install python3-pip`  Install pip for python3, alternatively download and run get-pip.py
`$ pip --version`  Check version of pip
`$ which pip`  Globally or inside a venv, check where your pip is located
`$ pip install --upgrade pip setuptools wheel`  Make sure you have a recent versions of these

A `sudo` may be needed in front(?)
`$ pip install [packagename] [packagename]`  # Install one or more packages, optionally with e.g. ==1.10 to specify version 
`$ pip install --upgrade [packagename]`
`$ pip list`  Shows all the packages and versions installed (in the venv)
`$ pip show [packagename]`  More detailed info about the package (also works with "pip show pip")
`$ pip uninstall [packagename]`

`$ pip install pip-tools`
`$ pip-compile --output-file=requirements.txt requirements.in`  Where `requirements.in` has only directly dependencies, such as `pandas==1.0.1`, then subdependencies are generated in `requirements.txt`. 



`...`  .... <br />
`...`  .... <br />

## Useful links
[Description](https://packaging.python.org/tutorials/installing-packages/)<br/>
[Description](https://alysivji.github.io/python-managing-dependencies-with-pip-tools.html)<br/>

Only partially read, because beyond basics, but explores pip-tools and more:<br/>
[Description](https://www.caktusgroup.com/blog/2018/09/18/python-dependency-management-pip-tools/)<br/>


## To be done?
[ ] pip wheel
[ ] pip hash checking?


----- ENTER EVERYTHING BELOW THIS POINT -----

Purpose
-------

How it works
------------


Useful links and tutorials
--------------------------

