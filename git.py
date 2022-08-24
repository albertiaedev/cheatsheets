#GIT CHEATSHEET

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
