# How to use apt, tarballs and other Ubuntu package management tools

## The purpose
APT (Advanced Package Tool) is Ubuntu's package handling system, which we interactivt with through the `apt(-get)` commands. The  apt is a simplified and more user-friendly version of apt-get, replaceing it's most commonly used commands, but not everything, so apt-get will still be needed for some cases.
You can also use the Ubuntu Software app on the Desktop __[DOES IT WRITE TO APT AND VICE-VERSA?]__

## How does it work?
It is possible to have a `README.md` in every folder, which will be displayed in the web GUI.

## Useful commands
`sudo apt update`  Update your local database about available packages at the repos.<br />
`sudo apt upgrade`  Upgrade the packages you have installed based on info from an update. Add the `-y` flag to always answer "Yes".<br />
`sudo apt full-upgrade`  Upgrades and also removed packages which needs to be removed.<br />
`sudo apt install <package_name>`  Install one or more packages (just add more package names). You may also specify `=<version_number>`. <br />
`sudo apt remove <package_name>`  Remove package (binaries).<br />
`sudo apt purge <package_name>`  Remove package (binaries) and it's config files.<br />
`sudo apt autoremove`  Free diskspace by removing obsolete dependencies.<br />
`apt show <package_name>`  Get info about the package, dependencies and more.<br />
`which program`  Get the location of the package executable, normally under `/usr/bin` or `/home/youruser`.<br />

### WIP
sudo apt install software-properties-common<br />
sudo add-apt-repository ppa:deadsnakes/ppa<br />
For tar.bz, open and read the README file, which may contain the installation instructions.<br />
Personal choice has been to install stuff at /opt/[PACKAGENAME]<br />
(sudo) tar xvzf ~/Downloads/PACKAGENAME.tar.gz # Done from /opt. If so, requires sudo.)<br />
Forstå hva som skjer her på linken under? wget laster ned til folderen du er i øyeblikket.<br />
https://github.com/Versent/saml2aws#linux<br />
Hva gjør wget kommandoen?<br />

## Useful links
[apt vs apt-get, with commands](https://itsfoss.com/apt-vs-apt-get-difference/)<br />
[apt command git](https://itsfoss.com/apt-command-guide/)<br />
### WIP
[Ubuntu file system](https://askubuntu.com/questions/138547/how-to-understand-the-ubuntu-file-system-layout/138551#138551)<br />
[Installing tarballs, e.g. tar.gz](https://sourcedigit.com/20839-extract-install-tar-gz-files-ubuntu/)<br />
