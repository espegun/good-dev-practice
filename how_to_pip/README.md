# How to pip

## The purpose
The most commonly used tool to download and install python packages (preferably in a venv) from PyPI (Python Package Index, pypi.org).

pip-compile is helpful in separating direct and sub dependencies, but isn't perfect, see the link at Caktusgroup at the bottom.

## How does it work?
Start by making sure you always have an updated version of pip, setuptools and wheel. 
Remember that pip updates only one of your potentially many global Python-distributions or venvs, be conscious about which you target. Generally it is preferable to run pip as a module with a defined python-version, e.g. `$ python37 -m pip <something>`.
Generally keep global installations pristine and install in venvs.
pip3 is the Python3 version of pip, organized the same way as python, so `pip` may be a softlink to pip3.X. 

## Useful commands
`sudo` may be needed sometimes(?)<br/>

`$ apt install python3-pip`  Install pip for python3, alternatively download and run `get-pip.py`<br/>
`$ pip --version`  Check version of pip<br/>
`$ which pip`  Globally or inside a venv, check where your pip is located <br/>
`$ pip install --upgrade pip setuptools wheel`  Make sure you have a recent versions of these <br/>
`$ pip install [packagename] [packagename]`  # Install one or more packages, optionally with e.g. `==1.10` to specify version <br/>
`$ pip install --upgrade [packagename]`  Upgrade a package<br/>
`$ pip list`  Shows all the packages and versions installed (in the venv)<br/>
`$ pip show [packagename]`  More detailed info about the package (also works with `pip show pip`)<br/>
`$ pip uninstall [packagename]`<br/>

`$ pip install pip-tools`<br/>
`$ pip-compile --output-file=requirements.txt requirements.in`  Where `requirements.in` has only directly dependencies, such as `pandas==1.0.1`, then subdependencies are generated in `requirements.txt`.<br/>

## Useful links
[Tutorial installing packages](https://packaging.python.org/tutorials/installing-packages/)<br/>
[Managing dependencies with pip tools](https://alysivji.github.io/python-managing-dependencies-with-pip-tools.html)<br/>
[Caktusgroup: Only partially read, because beyond basics, but explores pip-tools and more](https://www.caktusgroup.com/blog/2018/09/18/python-dependency-management-pip-tools/)<br/>

## To be done?
pip wheel<br/>
pip hash checking?<br/>
