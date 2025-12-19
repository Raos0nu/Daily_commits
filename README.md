# Daily GitHub Commit Automation

This repository uses GitHub Actions to automatically make one commit per day, creating a daily contribution square on your GitHub profile.

## How It Works

- A GitHub Actions workflow (`.github/workflows/daily.yml`) runs daily at 00:00 UTC
- On each run, it appends the current date to `activity.log`
- The workflow makes exactly one commit per day
- Commits are authored by `github-actions[bot]`

## Manual Trigger

You can manually trigger the workflow by:
1. Going to the "Actions" tab in this repository
2. Selecting the "Daily Commit" workflow
3. Clicking "Run workflow"

## Setup

To use this in your own repository:

1. Copy `.github/workflows/daily.yml` to your repository
2. Ensure GitHub Actions is enabled in your repository settings
3. The workflow will start running on the next scheduled time (daily at 00:00 UTC)

## Notes

- The workflow uses `[skip ci]` in commit messages to prevent triggering other workflows
- Commits are only made if there are actual changes (using `git diff --staged --quiet`)
- This follows GitHub's terms of service for automated contributions

