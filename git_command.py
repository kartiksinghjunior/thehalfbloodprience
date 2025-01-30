. Setup and Configuration
Configure Git with your username and email:

bash
Copy code
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
Check current Git configuration:

bash
Copy code
git config --list
Check if Git is installed:

bash
Copy code
git --version
2. Creating and Cloning Repositories
Initialize a new Git repository in your current directory:

bash
Copy code
git init
Clone an existing repository from GitHub or other remote source:

bash
Copy code
git clone <repository-url>
3. Checking the Status
Check the status of files (modified, untracked, etc.):
bash
Copy code
git status
4. Staging and Committing Changes
Stage a specific file (add it to the next commit):

bash
Copy code
git add <filename>
Stage all modified files (add all changed files to the next commit):

bash
Copy code
git add .
Commit staged changes with a message:

bash
Copy code
git commit -m "Your commit message"
Amend the previous commit (update the commit message or add changes):

bash
Copy code
git commit --amend
5. Branching and Switching Branches
Create a new branch and switch to it:

bash
Copy code
git checkout -b <branch-name>
Switch to an existing branch:

bash
Copy code
git checkout <branch-name>
List all branches:

bash
Copy code
git branch
Delete a local branch:

bash
Copy code
git branch -d <branch-name>
6. Merging Branches
Merge another branch into the current branch:

bash
Copy code
git merge <branch-name>
Resolve merge conflicts (edit the conflicting files, then add them):

bash
Copy code
git add <filename>
7. Remote Repositories
Add a remote repository (e.g., GitHub, GitLab):

bash
Copy code
git remote add origin <repository-url>
Check remote repository info:

bash
Copy code
git remote -v
Push changes to a remote repository:

bash
Copy code
git push origin <branch-name>
Push to remote and set the upstream branch (first push to a new branch):

bash
Copy code
git push -u origin <branch-name>
Pull changes from a remote repository (sync your local repo with the remote):

bash
Copy code
git pull origin <branch-name>
Fetch changes from a remote repository (retrieve updates without merging them):

bash
Copy code
git fetch origin
Delete a remote branch:

bash
Copy code
git push origin --delete <branch-name>
8. Viewing and Exploring Commits
View commit history:

bash
Copy code
git log
View a summary of commit history:

bash
Copy code
git log --oneline
Show changes made in a commit:

bash
Copy code
git show <commit-hash>
View a specific commit's changes in a file:

bash
Copy code
git diff <commit-hash> <filename>
9. Undoing Changes
Undo changes in a file (restore to the last committed state):

bash
Copy code
git checkout -- <filename>
Unstage a file (remove from staging area):

bash
Copy code
git reset <filename>
Undo a commit (but keep changes in your working directory):

bash
Copy code
git reset --soft HEAD~1
Undo a commit and discard changes (dangerous, irreversible):

bash
Copy code
git reset --hard HEAD~1
Undo all changes in the working directory (discard local changes):

bash
Copy code
git checkout -- .
10. Tagging
Create a tag at the current commit:

bash
Copy code
git tag <tag-name>
Push tags to a remote repository:

bash
Copy code
git push origin <tag-name>
List all tags:

bash
Copy code
git tag
11. Working with Remotes (Advanced)
Rename a remote:

bash
Copy code
git remote rename origin <new-name>
Remove a remote:

bash
Copy code
git remote remove <remote-name>
12. Clean Up Your Repository
Remove untracked files (files not staged for commit):

bash
Copy code
git clean -f
Remove untracked directories:

bash
Copy code
git clean -fd
13. Working with Stashes (Temporarily Save Changes)
Stash your changes (save changes without committing them):

bash
Copy code
git stash
List all stashes:

bash
Copy code
git stash list
Apply the latest stash:

bash
Copy code
git stash apply
Drop the latest stash:

bash
Copy code
git stash drop
Apply and drop a stash in one command:

bash
Copy code
git stash pop
14. Collaborating with Others
Fork a repository on GitHub (this is done via the GitHub website).
Create a Pull Request on GitHub to propose your changes (done on the GitHub site).
Resolve merge conflicts manually by editing the conflicting files and committing the changes.
15. Git Aliases (For Faster Workflow)
Create a Git alias for a command (e.g., shorten git status to git st):
bash
Copy code
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
