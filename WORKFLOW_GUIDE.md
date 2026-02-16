# Git and GitHub Workflow Guide - ML Project

## Stage 1: Basic Setup (Foundation)

### Terminal Commands (in order):

```bash
# Create project directory
mkdir ml-project

# Navigate into directory
cd ml-project

# Initialize Git repository
git init

# Create project files
touch train.py predict.py utils.py README.md

# Check repository status
git status
```

---

## Stage 2: Version Control Workflow (Application)

### Git Commands with Explanations:

```bash
# Stage only train.py and utils.py
git add train.py utils.py
# Explanation: Adds specific files to staging area, preparing them for commit

# Commit with message
git commit -m "Add training script and utilities"
# Explanation: Saves staged changes to local repository with descriptive message

# Link to GitHub repository
git remote add origin https://github.com/yourusername/ml-project.git
# Explanation: Connects local repo to remote GitHub repository

# Rename branch to main (if needed)
git branch -M main
# Explanation: Ensures you're using 'main' as primary branch name

# Push to GitHub
git push -u origin main
# Explanation: Uploads commits to GitHub; -u sets upstream tracking
```

**Note:** Create the GitHub repository at https://github.com/new before running remote add command.

---

## Stage 3: Collaborative Workflow (Synthesis)

### Complete Workflow Guide:

#### Step 1: Fetch Teammate's Changes
```bash
git fetch origin
```
**Reasoning:** Downloads remote changes without modifying your working directory. Safe first step to see what's changed.

#### Step 2: Pull Remote Changes
```bash
git pull origin main
```
**Reasoning:** Merges teammate's updates (predict.py, README.md) into your local repository. Do this BEFORE committing your changes to avoid conflicts.

#### Step 3: Stage Your Local Changes
```bash
git add utils.py config.py
```
**Reasoning:** Stages your modified utils.py and new config.py file for commit.

#### Step 4: Commit Your Changes
```bash
git commit -m "Update utilities and add configuration file"
```
**Reasoning:** Saves your work with a descriptive message explaining what changed.

#### Step 5: Push to GitHub
```bash
git push origin main
```
**Reasoning:** Uploads your commits to GitHub, making them available to your team.

### Potential Issues and Solutions:

**Issue 1: Uncommitted Changes During Pull**
- **Problem:** Git won't pull if you have uncommitted changes that conflict
- **Solution:** Commit or stash changes first
```bash
git stash          # Temporarily save changes
git pull origin main
git stash pop      # Reapply your changes
```

**Issue 2: Push Rejected (Remote Ahead)**
- **Problem:** Someone pushed while you were working
- **Solution:** Pull first, then push
```bash
git pull origin main
git push origin main
```

**Issue 3: Merge Conflicts (if they occur)**
- **Problem:** Same lines modified in same file
- **Solution:** 
```bash
# After pull shows conflicts:
# 1. Open conflicted files
# 2. Resolve conflicts manually
# 3. Stage resolved files
git add <resolved-files>
git commit -m "Resolve merge conflicts"
git push origin main
```

### Best Practices for Collaborative Development:

1. **Pull Before You Push:** Always fetch/pull latest changes before starting work
2. **Commit Often:** Small, focused commits are easier to manage
3. **Descriptive Messages:** Write clear commit messages explaining WHY, not just WHAT
4. **Communication:** Coordinate with team on who's working on which files
5. **Branch Strategy:** Use feature branches for major changes, merge to main when complete
6. **Review Changes:** Use `git status` and `git diff` before committing

### Quick Reference Commands:

```bash
git status              # Check current state
git log --oneline       # View commit history
git diff                # See unstaged changes
git diff --staged       # See staged changes
git remote -v           # View remote connections
git branch              # List branches
```
