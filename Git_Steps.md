# <ins> Git Steps to check and push changes from Local environment to your repo </ins>



## Before you start make sure your global environment is set in your local machine and your repo connected

	1. git init
	   - Initializes a new Git repository. It starts tracking an existing directory and begins watching for changes. This adds a hidden sub-folder within the existing directory that houses the internal data structure required for version control.
	
	2. git pull
	   - Fetches the changes from the remote repository and integrates them with the current branch in your local repository. If you're working with a team, this syncs your local branch with the latest changes from others. However, using `git pull` immediately after `git init` is unusual, as there is no remote repository set up to pull from at this point.
	
	3. git branch -M main
	   - Renames the current branch to `main`. The `-M` option stands for "move/rename" and will force the rename even if a branch with the name `main` already exists. This is often used to rename the default branch from `master` to `main`, which has become a common convention.
	
	4. git remote add origin "your-git-repo-code"
	   - Adds a new remote to your local repository. `origin` is a shorthand name for your remote repository. `"your-git-repo-code"` should be the URL of the remote repository where your project will be pushed, usually something like `https://github.com/username/repo.git`.
	
	5. git add -A
	   - Stages all changes (including untracked files, modifications, and deletions) to be committed. This tells Git that you want to include updates to these files for the next commit. Unlike `git add .` which adds new and modified files only in the current directory, `-A` is shorthand for `--all` and considers the entire repository.
	
	6. git commit -m "your-message-for-the-commit"
	   - Records the staged changes to the repository with a descriptive message. The `-m` flag allows you to add a commit message inline. `"your-message-for-the-commit"` should be replaced with a brief description of what changes the commit introduces to the project.
	
	7. git push -f -u origin main
	   - Pushes the commits from your local `main` branch to the `main` branch at the remote repository defined as `origin`. The `-f` flag stands for "force" and will overwrite the history on the remote repository with your local history, which can be dangerous and is generally discouraged unless you are certain of what you are doing. The `-u` flag sets the upstream for the branch, which means that in the future, you can simply run `git push` or `git pull` without specifying the branch or remote, and Git will know what you mean.
	

