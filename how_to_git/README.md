# How to Git

## The purpose
The general purpose of version control is to:
* Being able to roll back to previous stages after messing up the code.
* Collaborate on common projects through merging of branches.
* Do pull requests and code reviews.

## How does it work?
Tracked files have be staged or commited earlier, which untracked have not. A `.gitignore` file may be added and should contain a list of files and folders which should deliberately not be tracked, normally because these are machine generated and can be derived from the repo.

A **repository** is a data structure where project files are stored and modified. People work on their own *local* repo and then sync up and share work through the *central* repo (e.g. hosted on GitHub).<br/>
The **staging area** is used to organize and review what will be commited.<br/>
The **commit** is a snapshot a the situation at a certain point in time. It may or may not be pushed to another repo.<br/> 

*Git is basically about linked commit nodes.*

## Useful commands
`$ git clone [repo_url]` Create a local repo from the central. The URL can be copied from the central repo web page<br/>
`$ git remote -v` Get the URL of th central repo from which your local repo is syncing with.<br/>
`$ git add *` Stage files which have been added or modified.<br/>
`$ git add -u` Remove files which have been deleted in the local repo.<br/>

## Useful links
[Introduction to version control with git](https://www.atlassian.com/git/tutorials/what-is-version-control)<br />
[Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)<br />
[Markdown guide](https://ia.net/writer/support/general/markdown-guide)
