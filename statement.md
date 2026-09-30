# Statement

## Problem Statement

Students often juggle multiple assignments across different courses, each with its own deadline and importance. Without a simple way to see everything in one place, it's easy to lose track of what's due soon and end up missing a deadline. Deadline Manager addresses this by giving the user a lightweight, offline command-line tool to record assignments and immediately see which ones need urgent attention.

## Scope of the Project

Deadline Manager is a single-user, local command-line application. It covers adding, viewing, updating, completing, and deleting assignments, and it automatically flags assignments that are due soon. It does not cover multi-user accounts, calendar syncing, notifications outside the program, or automatic date-based countdowns — the "days remaining" value is entered and updated manually by the user.

## Target Users

College students who want a quick, no-frills way to track assignment deadlines across their courses without installing a full task-management app or creating an account anywhere.

## High-Level Features

- Add an assignment with course code, title, days remaining, and priority (HIGH, MED, or LOW)
- View pending assignments, with an automatic [URGENT!] tag when 2 or fewer days remain
- View completed assignments separately from pending ones
- Mark an assignment as done
- Update an assignment's days remaining and/or priority
- Delete an assignment
- All data is saved locally and reloaded automatically the next time the program runs
