# How to Git

**KEEP WORKING FROM THIS POINT**<br/>
https://www.git-tower.com/learn/git/ebook/en/command-line/branching-merging/branching-workflows#start

## The purpose
The general purpose of version control is to:
* Work in parallell independence on the same project using branches and merges.
* Being able to roll back to previous commits and understand the exact changes after introducing bugs or features have become obsolete.
* Easily do pull requests and code reviews.<br/>

Generally keep independent changes in separate commits. Also doing PRs of each commit is simple and quick.

## How does it work?

Git is basically about linked commit nodes. Though one coordinating or central repository is normally used, Git is a *distributed* VCS, not *centralized*.

* The **workspace** is the project folders where you are working on files. Note that the workspace is not the same as the repo.<br/>
* A **repository** is a data structure where project files are stored in all previously committed versions, this is stored in a `.git` folder below the root folder of your project workspace. Do not directly manipulate the content of `.git`. Modifications in the workspace are committed (saved) to *local* repo and then uploaded and shared through the *central* repo (e.g. hosted on GitHub).<br/>
* The **staging area** (or index) is used to organize and review the files which have been added or modified and should be included in the next commit to the local repo.<br/>
* The **commit** save a snapshot of the files at a certain point in time to the *local* repo. It may or may not be pushed to central repo. Each has a unique commit hash of 40 chars (in most cases, using the first 7 chars is sufficient). Only commit related changes in the same commit. A good rule of thumb is to commit often, but not incomplete work.<br/> 
* To **push** is to update a remote (central) repo with the commit done in the local repo.<br/>
* To **pull** is to update your repo with files committed a remote (central) repo (needs to be done after a remote merge).<br/>
* **Branching** makes it possible to work in parallell on different context while minimizing interdependencies.<br/>
* **HEAD** is a reference to the last commit in the currently check-out branch.<br/>
* **Merging** All the commits which are not present in the working branch are added to it. Sometimes, a separate merge commit will be created.<br/> 
* **Pull request** Get feedback and possibly approval to merge your commit and branch into another branch (normally `master`). One commit/PR for each branch, then squash, merge and delete the branch (Origo Dataplatform. All merges into `master` are expected to be deployed in `prod` (while you may deploy to `dev` during individual development testing). To make reviews quick and precise, keep them small, independent and well explained.<br/>

![Image from unwiredlearning.com](git-flow.png)

## Useful commands
**TBD rebase Pri**<br/>
**TBD clone**<br/>
**TBD fork**<br/>
**TBD stash**<br/>

### Git config
`$ git config --global user.name "Espen Gunnarsen"`<br/>
`$ git config --global user.email "espen@gmail.com"`<br/>
Set up a Personal Access Tokens (PAT) as described [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)<br/>

### Initialize
`$ git init` Create a local repo from scratch, all stored in the hidden `.git` folder.<br/>
`$ git clone [repo_url]` Clone a central repo to a local (with `.git`) into a subfolder. The URL can be copied from the central repo web page<br/>
`$ git remote -v` Get the URL of the central repo from which your local repo is syncing with through `push` and `pull`.<br/>
`.gitignore` This file should keep a list of files which should not be tracked, typically built or compiled files, personal configuration files, log, cache files and similar. Provide full path from the the working directory for specific files (e.g. `folder/my_log.txt`) or all fill which matches a pattern (e.g. `*.log`).<br/>

### Stage, commit and push
`$ git status` Shows the status of your local files (untracked/modified/staged) compared to the last commit to the local repo.<br/>
`$ git add *` Stage files which have been added or modified and you want to include in your next commit.<br/>
`$ git add -u` Remove files which have been deleted in the local repo.<br/>
`$ git reset filename` Unstage file. <br/>
`$ git commit -m "commit message"` Commit the staged files and create a saved snapshot of the files in the local repo.<br/>
`$ git push` Add `òrigin master` to push to a remote he central master brach. **WIP!**

### Pull and fetch
In addition to the local repo, there is also a cached version of the central repo on your local computer.<br/>
`$ git fetch origin` Check the central repo if there has been any updates and the local cached version of it. No harm will be done.<br/>
`$ git pull origin [branch]` Check the central repo if there has been any updates and tries to merge this into your current HEAD branch and working files. Merge conflicts may occurs and it is recommended pull right after having committed.<br/>

### Looking at and possibly reverting changes (uncommitted and committed) 
`$ git checkout HEAD filename` Revert this (tracked) file in the current workspace to it's state during the *last* commit.<br/>
`$ git reset --hard HEAD` Revert all (tracked) files in the current workspace to it's state during the *last* commit.<br/>
`$ git log` This will show the history of commits up to HEAD (scroll with arrow, quit with q). Some flags: `--all` all commits (including later than HEAD), e.g. `-3` latest 3 commits, `-p` detailed changes.<br/>
`$ git checkout commit_number` Reverts your workspace to the state at the commit number (sets the HEAD to that commit), *but* you are then not on a branch(!)<br/>
`$ git revert commit_number` Creates a new commit which has reverted the changes in the specified commit (but not those done later).<br/>

### Branching and merging
`$ git branch branchname` Create a new branch.<br/>
`$ git branch` Which branches are active. `-v` for more detail. `*` indicates the HEAD branch..<br/>
`$ git checkout branchname` Switch to a branch (make it the HEAD branch) and change the content of your working directory..<br/>
`$ git merge branchname` First make the branch you want to merge into your active branch, then specify the branch which has the desired changes.  .<br/>
`$ git rebase  ....` Get latest commits from the (master) branch into your your branch


### Stashing
https://www.git-tower.com/learn/git/ebook/en/command-line/branching-merging/stashing#start


Read this for understanding - not just commands:
https://nvie.com/posts/a-successful-git-branching-model/<br/>




### Various
`$ git diff optional_filename` Show the differences between one or all tracked files between your local workspace and the local repo. 



## Useful links
[Git tutorial, focus on commands](https://unwiredlearning.com/blog/git-basic-for-beginners/)
[Atlassian: Git tutorial](https://www.atlassian.com/git/tutorials/what-is-version-control)<br/>
[Git-tower: Git tutorial](https://www.git-tower.com/learn/git/ebook/en/command-line/basics/what-is-version-control)<br/>
[Git GUI](https://medium.com/better-programming/stop-using-the-git-cli-d9cbee32cc27)<br/>
[Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)<br/>
[Markdown guide](https://ia.net/writer/support/general/markdown-guide)<br/>
[The anatomy of a perfect pull request](https://medium.com/@hugooodias/the-anatomy-of-a-perfect-pull-request-567382bb6067)
