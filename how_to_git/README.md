# How to Git

## The purpose
The general purpose of version control is to:
* Being able to roll back to previous stages after messing up the code.
* Collaborate on common projects through merging of branches.
* Do pull requests and code reviews.

## How does it work?
Tracked files have be staged or commited earlier, which untracked have not. A `.gitignore` file may be added and should contain a list of files and folders which should deliberately not be tracked, normally because these are machine generated and can be derived from the repo.

A **repository** is a data structure where project files are stored as all previously committed versions. Note that the repo itself is not the same as the working directories. People work on their own *local* repo and then sync up and share work through the *central* repo (e.g. hosted on GitHub).<br/>
The **staging area** is used to organize and review the files which have been added or modified and should be committed to the repo.<br/>
The **commit** save a snapshot a the situation at a certain point in time. It may or may not be pushed to central repo. Each has a unique commit number of around 40 chars.<br/> 
To **push** is to update the central repo with changes done in the local repo.

*Git is basically about linked commit nodes.*

## Useful commands
### Initialize
`$ git init` Create a local repo from scratch, all stored in the hidden `.git` folder.<br/>
`$ git clone [repo_url]` Clone a central repo to a local (with `.git`). The URL can be copied from the central repo web page<br/>
`$ git remote -v` Get the URL of the central repo from which your local repo is syncing with through `push` and `pull`.<br/>

### Stage, commit and push
`$ git status` Shows the status of your local files (untracked/modified/staged) compared to the local repo (previously committed).<br/>
`$ git add *` Stage files which have been added or modified.<br/>
`$ git add -u` Remove files which have been deleted in the local repo.<br/>
`$ git reset filename` Unstage file. <br/>
`$ git commit -m "commit message"` Commit the staged files and create a saved snapshot of the files in the local repo.<br/>
`$ git push` Add `òrigin master` to push to the central master brach. **WIP!**

### Pull and fetch
In addition to the local repo, there is also a cached version of the central repo on your local computer.<br/>
`$ git fetch origin` Check the central repo if there has been any updates and the local cached version of it. No harm will be done.<br/>
`$ git pull origin [branch]` Check the central repo if there has been any updates and tries to merge this into your current HEAD branch and working files. Merge conflicts may occurs and it is recommended pull right after having committed.<br/>

### Log and revert
`$ git log` This will show the history of commits, with a **commit number**.
`$ git checkout [commit number]` Reverts your working files to the state at the commit number.

### Branches
...



## Useful links
[Atlassian: Git tutorial](https://www.atlassian.com/git/tutorials/what-is-version-control)<br/>
[Git-tower: Git tutorial](https://www.git-tower.com/learn/git/ebook/en/command-line/basics/what-is-version-control)<br/>
[Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)<br/>
[Markdown guide](https://ia.net/writer/support/general/markdown-guide)<br/>
