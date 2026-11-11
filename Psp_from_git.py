"""Reconstruct PSP data (sessions, minutes, Python LOC) from a git history.

Run inside the repo:   python3 psp_from_git.py
Edit JOBS below to match how you want to group your work.

Output:
  - a table per job (commits, days, sessions, git-visible minutes, Python LOC added)
  - sessions.csv, one row per work session, ready to copy into the Daily Time Log

IMPORTANT: git only knows when you committed, not when you started. Minutes
here are a LOWER BOUND. Single-commit sessions have unknown length (start == stop);
fill those in from memory and label them "estimated".
"""

import csv
import subprocess
from datetime import datetime, timedelta

GAP_MINUTES = 90  # commits closer together than this belong to one session

# (job number, description, first date, last date), dates inclusive, YYYY-MM-DD
JOBS = [
    ("P3", "Beginner console programs", "2026-08-08", "2026-08-20"),
    ("P4", "Auction, calculator, blackjack, guessers, coffee machine", "2026-08-21", "2026-08-28"),
    ("P5", "OOP quiz app and turtle graphics", "2026-08-28", "2026-09-08"),
    ("P6", "Snake game", "2026-09-08", "2026-09-15"),
    ("P7", "Pong and Crossing road", "2026-09-16", "2026-09-18"),
    ("P8", "States quiz and NATO app", "2026-09-19", "2026-09-24"),
    ("P9", "Pomodoro and password manager", "2026-09-25", "2026-10-01"),
    ("P10", "Flashcard capstone", "2026-10-02", "2026-10-11"),
    ("P11", "Email automation", "2026-10-12", "2026-10-16"),
]

# Where one job ends and the next begins on the same day, use a time cutoff.
# Commits on a job's first date before this time go to the previous job.
# (Leave empty if your date ranges do not overlap.)
SAME_DAY_SPLITS = {
    "P5": "17:00",  # 2026-08-28 commits from 17:00 on belong to P5
    "P6": "17:00",  # 2026-09-08 commits from 17:00 on belong to P6
}


def run(*args):
    return subprocess.run(
        ["git", "--no-pager", *args], capture_output=True, text=True, check=True
    ).stdout


def load_commits():
    """Return [(datetime, python_lines_added)] oldest first."""
    out = run(
        "log", "--reverse", "--numstat",
        "--pretty=format:@@%H|%ad", "--date=format:%Y-%m-%d %H:%M",
        "--", "*.py", ":(exclude,glob)**/.venv/**",
    )
    # numstat only lists commits touching .py files; get ALL commit times separately
    times = run("log", "--reverse", "--pretty=format:%H|%ad", "--date=format:%Y-%m-%d %H:%M").split("\n")
    loc = {}
    current = None
    for line in out.splitlines():
        if line.startswith("@@"):
            current = line[2:].split("|")[0]
            loc.setdefault(current, 0)
        elif line.strip() and current:
            added = line.split("\t")[0]
            if added.isdigit():
                loc[current] += int(added)
    return [(datetime.strptime(t.split("|")[1], "%Y-%m-%d %H:%M"), loc.get(t.split("|")[0], 0)) for t in times if t]


def job_for(ts, jobs):
    d = ts.strftime("%Y-%m-%d")
    matches = [j for j in jobs if j[2] <= d <= j[3]]
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0]
    # overlapping day: later job wins from its cutoff time onward
    for j in reversed(matches):
        cutoff = SAME_DAY_SPLITS.get(j[0])
        if d == j[2] and cutoff and ts.strftime("%H:%M") < cutoff:
            continue
        return j
    return matches[0]


def main():
    commits = load_commits()
    gap = timedelta(minutes=GAP_MINUTES)
    rows = []
    print(f"{'Job':<5}{'Dates':<14}{'Commits':>8}{'Days':>6}{'Sess.':>7}{'Single':>8}{'Git min':>9}{'Py LOC':>8}")
    for job in JOBS:
        mine = [(t, l) for t, l in commits if job_for(t, JOBS) == job]
        if not mine:
            continue
        sessions, cur = [], [mine[0]]
        for item in mine[1:]:
            if item[0] - cur[-1][0] <= gap:
                cur.append(item)
            else:
                sessions.append(cur)
                cur = [item]
        sessions.append(cur)
        minutes = 0
        for s in sessions:
            mins = int((s[-1][0] - s[0][0]).total_seconds() // 60)
            minutes += mins
            single = len(s) == 1
            rows.append([
                s[0][0].strftime("%Y-%m-%d"), s[0][0].strftime("%H:%M"),
                s[-1][0].strftime("%H:%M"), "", job[0], job[1],
                "SINGLE COMMIT: duration unknown, add estimate from memory (label as estimated)"
                if single else "Reconstructed from git timestamps (lower bound)",
            ])
        n_single = sum(len(s) == 1 for s in sessions)
        days = len({t.date() for t, _ in mine})
        loc = sum(l for _, l in mine)
        span = f"{mine[0][0]:%m-%d}..{mine[-1][0]:%m-%d}"
        print(f"{job[0]:<5}{span:<14}{len(mine):>8}{days:>6}{len(sessions):>7}{n_single:>8}{minutes:>9}{loc:>8}")

    with open("sessions.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Date", "Start", "Stop", "Interruption (min)", "Job #", "Phase", "Comments"])
        w.writerows(rows)
    print(f"\nWrote sessions.csv with {len(rows)} sessions.")


if __name__ == "__main__":
    main()
