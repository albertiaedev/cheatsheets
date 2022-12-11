#GIT CHEATSHEET

#Setup
git config --global user.name #set a name that is identifiable for credit when review version history
git config --global user.email #set an email address that will be associated with each history marker
git config --global color.ui auto #set automatic command line coloring for git for easy reviewing

#Initializes a new local repository with git
git init

#Add files to the staging area
git add {file_name} #use this command to add a single file to the staging area
    ###or###
git add . #use this command to add all files to the staging area

#Check the state of the staging area
git status

#View the entire commit story
git log

#Commit files on your local repository
git commit #commit all files
   ###or###
git commit -m "message" #commit an individual file

#Download existing code from a remote repository
git clone {url}

#List all the local branches on the machine
git branch

#merge the provided branch with the current working branch
git merge {branch_name}

#Create a new branch locally
git branch {branch_name}

#Delete a branch
git branch -d {branch_name}

#Rename the current working branch
git branch -m {branch_new_name}

#Swicth from the current branch to another one
git checkout {branch_name}

#Save all commits to a remote repository
git push {url} {branch_name}

#Create a new branch and swicth to it
git checkout -b {branch_name}

#Pull down all the updates from a remote repository
git pull {url}

#Remove a file from the local directory
git rm {file_name}

#Remove uncommited chances temporarily
git stash

#Chance to the local files and restore to the last commit
git reset

#Display the difference between files in two commits or between a commit and your current repository
git diff
