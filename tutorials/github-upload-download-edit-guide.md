# GitHub Workflow Guide: Upload, Download & Edit 📚

A complete tutorial for managing files on GitHub from start to finish. Covers the three core actions: **uploading** files to GitHub, **downloading** them to a new computer, and **editing** existing files.

---

## 🧠 Before You Start — The Mental Model

GitHub is a cloud copy of your project. Both your computers talk to GitHub, never to each other directly:

```
Desktop  ⇄  GitHub (cloud)  ⇄  Laptop
```

**The 4 commands that do 90% of the work:**

| Command | What it means |
|---------|---------------|
| `git add` | "Pay attention to these changes" |
| `git commit -m "..."` | "Save a snapshot with a description" |
| `git push` | "Upload my snapshots to GitHub" |
| `git pull` | "Download the latest snapshots from GitHub" |

**The golden rule:**
> **Pull when you sit down. Push before you leave.**

---

## 📤 PART 1: UPLOADING Files to GitHub

There are two scenarios: starting a brand new project, or adding/changing files in an existing one.

### 🆕 Scenario A: Brand new project (first upload)

Use this when your project exists on your computer but is NOT on GitHub yet.

#### Step 1: Create an empty repo on GitHub
1. Go to [github.com](https://github.com) → click **+** → **New repository**
2. Name it (e.g., `python-learning`)
3. Set to **Private**
4. ⚠️ **DO NOT** check "Add a README" — leave it completely empty
5. Click **Create repository**
6. Copy the URL it shows you

#### Step 2: Open a terminal INSIDE your project folder
- File Explorer → navigate to your project folder
- Right-click on empty space → **"Open in Terminal"**
- Verify with `dir` — you should see your project files

⚠️ **Never** run Git commands from `C:\Windows\System32` — Windows blocks file creation there.

#### Step 3: Run the first-time upload commands
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

✅ Refresh GitHub — your files should appear!

---

### 🔁 Scenario B: Adding or updating files in an existing project

Use this when the repo already exists and you just want to push new changes.

#### Step 1: Open terminal in the project folder
Verify you're in the right place — your prompt should show the project path:
```
C:\Users\YOUR-NAME\Documents\python-learning>
```

Run `git status` to confirm — if it says "On branch main," you're in a real Git repo. ✅

#### Step 2: Add new files OR edit existing ones
Just create/edit files normally in VS Code or File Explorer. Git will detect changes automatically.

To add a new folder, just create it in File Explorer and put files in it. Git tracks folders automatically as long as they have at least one file inside.

#### Step 3: Push the changes
```bash
git add .
git commit -m "describe what you did"
git push
```

That's it! Refresh GitHub to see your changes. ✨

---

## 📥 PART 2: DOWNLOADING Files from GitHub

Two scenarios here too: getting a project on a new computer for the first time, or updating files on a computer that already has the project.

### 🆕 Scenario A: First time on a new computer

Use this to set up a project on a second computer (laptop, work PC, etc.).

#### Step 1: Make sure Git is installed on the new computer
Download from [git-scm.com/downloads](https://git-scm.com/downloads). Verify with:
```bash
git --version
```

Configure your identity (use the **same** email as your other computer):
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

#### Step 2: Open a terminal in a SAFE folder
Pick where projects will live (Documents is great):
```bash
cd C:\Users\YOUR-NAME\Documents
```

⚠️ Verify the prompt — should say `Documents`, NOT `System32` or `Windows`.

#### Step 3: Get the clone URL
On GitHub: open your repo → green **`<> Code`** button → **HTTPS** → copy the URL.

#### Step 4: Clone it
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
```

The first time, GitHub will pop up a browser window for authentication. Just complete it.

When done, you'll see "100%" lines and "done." That means success. ✅

#### Step 5: Move into the project
```bash
cd YOUR-REPO
```

Open it in VS Code → done! 🎉

---

### 🔁 Scenario B: Already have the project, just want updates

Use this every time you sit down to work — to grab any changes from your other computer.

```bash
git pull
```

That's literally it. One command. It downloads anything new from GitHub and merges it into your local files automatically.

You'll see one of two things:

**Already up to date.** → Nothing changed since last time. ✅

**Updating ... files changed.** → New stuff downloaded. ✅

⚠️ **Make this the first thing you do every coding session.** Always.

---

## ✏️ PART 3: EDITING Files

This is the most common thing you'll do — and it's the simplest!

### The everyday rhythm

```
1. git pull          ← get latest from GitHub
2. ... edit files ... ← code in VS Code like normal
3. git add .         ← stage your changes
4. git commit -m "what you did"
5. git push          ← upload to GitHub
```

### A real example

Let's say you want to fix a bug in `grading_system.py`:

```bash
# Sit down, open terminal in project folder
git pull

# Now open VS Code, fix the bug, save the file
# (regular editing — nothing special)

# When done:
git add .
git commit -m "fixed average calculation bug"
git push
```

That's the whole loop. Forever. 🔄

---

### 🔄 Renaming or moving files

Use the terminal — it's more reliable than drag-and-drop when Git is involved.

**Rename a file:**
```bash
ren "old name.py" "new name.py"
```

**Move a file into a folder:**
```bash
move "filename.py" foldername
```

**Create a new folder:**
```bash
mkdir foldername
```

⚠️ **Always use quotes around names with spaces!**

After moving things around, verify with:
```bash
dir          ← see what's in current folder
dir day1     ← see what's inside a specific folder
git status   ← see what Git thinks changed
```

Then commit and push as usual.

---

### 🗑️ Deleting a file

In File Explorer or VS Code, just delete the file normally. Then in terminal:

```bash
git add .
git commit -m "removed unused file"
git push
```

Git will detect the deletion automatically and sync it to GitHub.

---

## 🔍 The Three Diagnostic Commands

Whenever something seems weird, these three commands tell you the truth:

### `dir` (or `ls` on Mac/Linux)
**Shows what's actually in the current folder.**
Use this to verify files really exist where you think they do.

### `git status`
**Shows what Git thinks is going on.**
- "On branch main" → you're in a real repo ✅
- "Changes not staged" → you have edits Git noticed
- "nothing to commit, working tree clean" → everything synced ✅
- "fatal: not a git repository" → wrong folder! ❌

### `git log --oneline`
**Shows your commit history.**
Useful for seeing what you've done lately. Press `q` to exit.

**80% of beginner Git mysteries are solved by running `dir` and `git status` first.**

---

## ⚠️ Common Errors & Fixes

### `failed to push some refs ... fetch first`
**Why:** GitHub has changes your computer doesn't have.
**Fix:**
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

If a weird editor opens asking for a merge message:
- **Vim** (black scary screen): `Esc` → type `:wq` → Enter
- **Nano** (shows `^X` at bottom): `Ctrl+X` → `Y` → Enter

---

### `could not create work tree dir ... Permission denied`
**Why:** Your terminal is in a protected folder like `System32`.
**Fix:** Move to a safe folder:
```bash
cd C:\Users\YOUR-NAME\Documents
```

---

### `fatal: not a git repository`
**Why:** You're running Git commands in a folder that isn't tracked by Git.
**Fix:** Check your prompt — make sure you're in the actual project folder:
```bash
cd C:\Users\YOUR-NAME\Documents\YOUR-REPO
```

---

### `nothing to commit, working tree clean` (when you expected changes)
**Why:** Git doesn't see any changes — usually because your edits didn't actually save, or you're in the wrong folder.
**Fix:** Check with `dir` and verify the files really changed. Make sure you saved in VS Code (Ctrl+S).

---

### Push succeeds but GitHub doesn't show the change
**Why:** Your local folder doesn't actually have the change you think it does.
**Remember:** GitHub = mirror of your local folder. If GitHub looks wrong, your local folder probably looks wrong too.
**Fix:** Run `dir` and verify reality matches your expectation. Fix locally, then push.

---

## 📝 Writing Good Commit Messages

A commit message is a note to your future self. Make it useful.

✅ Good:
- `"added grade removal feature"`
- `"fixed average calculation bug"`
- `"organized files into day1 folder"`

❌ Bad:
- `"asdf"`
- `"update"`
- `"stuff"`

**Tip:** Finish this sentence: *"If applied, this commit will ___"*. The blank is your message.

---

## 🎯 The Two Habits That Solve 99% of Problems

1. **`git pull` before you start coding** — every time, every computer
2. **`git push` before you stand up** — every time, no exceptions

Build these two habits and Git will feel effortless.

---

## 🆘 When Stuck — Read the Error!

Git almost always tells you what command to run next. Look for `hint:` lines — they're written for humans. Read first, panic later. 🙂

**Debugging checklist when something breaks:**
1. Read the full error message (not just the first line)
2. Run `dir` — is your folder structure what you think it is?
3. Run `git status` — what does Git think is happening?
4. Check your prompt — are you in the right folder?
5. If still stuck, search the exact error message online

---

## 🎓 Quick Reference Cheat Sheet

```bash
# === FIRST TIME SETUP (per computer) ===
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# === START A NEW REPO ===
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/USER/REPO.git
git push -u origin main

# === GET A REPO ON A NEW COMPUTER ===
git clone https://github.com/USER/REPO.git
cd REPO

# === DAILY WORKFLOW ===
git pull                    # at start of session
# ... do your work ...
git add .
git commit -m "what you did"
git push                    # at end of session

# === DIAGNOSTICS (when stuck) ===
dir                         # what's actually here
git status                  # what does Git think
git log --oneline           # commit history

# === FILE OPERATIONS ===
mkdir foldername            # create folder
move "file.py" foldername   # move file
ren "old.py" "new.py"       # rename file
```

---

*Created during my Git learning journey. Reference this whenever workflows feel fuzzy — the rhythm becomes second nature with practice.*
