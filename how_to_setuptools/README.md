# How to setuptools (and setup.py)

Purpose
-------
To more easily distribute and consistently build Python projects and packages. It can also be used to specify which packages should be included in requisites.txt (including sub dependencies).

(It is a prerequisite for using tox.)


How it works
------------
`setup.py` should be in the same folder as README.md and above subfolders containing the actual source code (also an empty __init__py file in the subfolder). 

## The minimum version of setup.py
```
from setuptools import setup, find_packages
setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),  # <-- Note, event 
)
```
Other fields to include could be:<br/>
`long_description= "..."`  # Might be good to read from README.md and set content in this field<br/>
`long_description_content_type="text/markdown"`<br/>
`include_package_data=True`<br/>
`install_requires=["boto3","numpy"]`<br/>
TBD link: https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords <br/>

`$ pip-compile` Reads `install_requires` from `setup.py` and generates an updated `requirements.txt`.<br/>


`$ setup.py sdist`  Build a distribution (tar.gz-file and a folder packagename.egg.info with dependencies)<br/>

It may be a good idea to first read README.md then assign it to setup(long_description).<br/>

Useful links and tutorials
--------------------------
https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide<br/>
https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/# How to <SOMETHING><br/>
