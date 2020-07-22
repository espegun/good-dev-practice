# How to venv

## The purpose
Different projects may require different versions of packages. Using virtual environments such as venv gives the ability to control which packages should be included (avoid to many and specify exactly which versions). This reduces inconsistencies and increases reproducability. A good rule of thumb is to keep the global installations to a minimum, and install according to project requirements.

## How does it work?
A virtual environment is basically a directory which contains the spesifications for a Python project and overruns PATH, i.e. where to look for interpreters and packages. venv's may be activated and deactivated. Generally, don't use Anaconda outside a container.

## Useful commands
`$ sudo apt-get install python3-venv` If not installed on Ubuntu, install it<br/>
`$ pip --version` Check the version and make sure you have an updated one. VENV VERSION?? <br/> 
`$ pip install --upgrade pip` Upgrade pip if needed. VENV VERSION?? <br/>
`$ python3.X -m venv .venv` Creates the venv setup (a hidden folder, .venv is the convention folder name). Python3.X will be the Python version available in the venv (through a symlink to the global installation).<br/>
`$ source .venv/bin/activate` Activate the venv, now you can install packages inside it<br/>
`$ echo $PATH` Note that a new folder within the venv has been added first<br/>
`$ pip install numpy==1.19` Will be installed in the venv, under the python version used to run pip (or by using a symlink?)<br/>
`$ pip freeze > requirements.txt` Write all the packages installed in the venv to requirements.txt. The file may also be manually updated.<br/>
`$ pip install -r requirements.txt` Make installations from a requirements file (normally cloned from a repo), but create and acticate a venv first!<br/>
`$ python3.X main.py` Just running a script in the venv<br/>
`$ deactivate` Deactivate the venv<br/>

You should add `requirements.txt` to source control (GitHub), but not the venv itself (use `.gitignore`). You may install the venv manually or through MakeFiles or equivalents.

## Useful links
[Python docs](https://docs.python.org/3/library/venv.html)<br/>
[Not good, but BASIC.](https://medium.com/@peterchang_82818/python3-beginner-must-know-venv-fdbbd0421405)<br/> 
[TBD](https://levelup.gitconnected.com/using-venv-or-virtual-environment-for-installing-python-packages-94f93409384)<br/>
[TBD2](https://hackersandslackers.com/multiple-versions-python-ubuntu/)<br/>
