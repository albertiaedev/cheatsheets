# LINUX COMMANDS

" * - use this command with extreme caution "

#file commands
1. ls #directory listing
2. ls -al #formatting listing with hidden files
3. cd {dir} #change directory to {dir}
4. cd #change to home
5. pwd #show current directory
6. mkdir {dir} #create a directory {dir}
7. rm {file} #delete {file}
8. rm -r {dir} #delete dierectory {dir}
9. rm -f {file} #force remove {file}
*10. rm -rf {dir} #force remove directory {dir}
11. cp {file1} {file2} #copy file1 to file2
12. cp -r {dir1} {dir2} #copy {dir1} to {dir2}, create {dir2} if it doesn't exist
13. mv {file1} {file2} #rename or move file1 to file2 #if {file2} is an existing directory, moves {file1} into directory {file2}
14. ln -s {file} {link} #create symbolic link {link} to {file}
15. touch {file} #create or update {file}
16. cat > {file} #places standard input into {file}
17. more {file} #output contents of {file}
18. head {file} #output the first 10 lines of {file}
19. tail {file} #output the last 10 lines of {file}
20. tail -f {file} #output the contents of {file} as it grows, starting with the last 10 lines
