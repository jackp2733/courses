# In-Class Exercise: Pipe Builder

Students work at their Codespace terminal. Each part builds on the last.

## Setup

> **Already forked from a previous assignment?** Pull the latest updates:
> ```bash
> git remote add upstream https://github.com/blkfin/courses.git   # only needed once
> git fetch upstream
> git merge upstream/main
> ```

Navigate to the exercise directory:
```bash
cd it612/exercises/pipe-builder/
```

---

## Part 1 — Build a Pipeline (5 min)

Using `/etc/passwd` (exists on every Linux system):

1. Print the contents of `/etc/passwd` (`cat`)
2. Extract just the usernames (hint: `cut` with `:` as delimiter, field 1)
3. Sort them alphabetically
4. Count how many there are (just the number)

Build it one pipe at a time — verify each stage before adding the next.

---

## Part 2 — Save It as a Script (5 min)

1. Create a file called `usercount.sh`
2. Add a shebang line (`#!/bin/bash`)
3. Add `set -e`
4. Put your pipeline from Part 1 in the script
5. Make it executable and run it
6. Modify it to take a filename as an argument (`$1`) instead of hardcoding `/etc/passwd`

---

## Part 3 — Make It Useful (3 min)

1. Run your script on `/etc/passwd` — does it still work?
2. Create a test file with some duplicate usernames and run your script on it
3. Modify the pipeline to also remove duplicates before counting

---

## Submission

```bash
git add usercount.sh
git commit -m "Pipe builder exercise complete"
git push
```

Submit the URL to your GitHub repository on Canvas.
