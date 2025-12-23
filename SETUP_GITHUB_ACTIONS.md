# 🔧 Setup GitHub Actions to Count on Your Contribution Graph

## Problem
By default, GitHub Actions commits are made by `github-actions[bot]` which **don't count** toward your contribution graph. This guide will fix that!

## Solution
We need to use a **Personal Access Token (PAT)** so commits are made as **you**, not the bot.

---

## Step 1: Create a Personal Access Token (PAT)

1. **Go to GitHub Settings:**
   - Click your profile picture (top right)
   - Click **Settings**
   - Scroll down and click **Developer settings** (left sidebar)
   - Click **Personal access tokens** → **Tokens (classic)**

2. **Generate New Token:**
   - Click **Generate new token** → **Generate new token (classic)**
   - Give it a name: `Daily Commits Automation`
   - Set expiration: **No expiration** (or your preferred duration)
   - Select scopes:
     - ✅ **repo** (Full control of private repositories)
     - ✅ **workflow** (Update GitHub Action workflows)

3. **Copy the Token:**
   - Click **Generate token**
   - **IMPORTANT:** Copy the token immediately (you won't see it again!)
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

## Step 2: Add Token to Repository Secrets

1. **Go to Your Repository:**
   - Navigate to: https://github.com/Raos0nu/Daily_commits

2. **Open Settings:**
   - Click **Settings** tab (top of repository)

3. **Go to Secrets:**
   - Click **Secrets and variables** → **Actions** (left sidebar)
   - Click **New repository secret**

4. **Add the Secrets:**

   **Secret 1: Personal Access Token**
   - Name: `PERSONAL_ACCESS_TOKEN`
   - Value: Paste your PAT token (the `ghp_xxxxx` you copied)
   - Click **Add secret**

   **Secret 2: Your Email (Optional but Recommended)**
   - Name: `GIT_EMAIL`
   - Value: Your GitHub email (the one associated with your account)
   - Click **Add secret**

   **Secret 3: Your Name (Optional but Recommended)**
   - Name: `GIT_NAME`
   - Value: Your GitHub username (e.g., `Raos0nu`)
   - Click **Add secret**

---

## Step 3: Verify It's Working

1. **Wait for Next Workflow Run:**
   - The workflow runs 6 times daily (2 AM, 6 AM, 10 AM, 2 PM, 6 PM, 10 PM UTC)
   - Or manually trigger it: **Actions** tab → **Daily Commits** → **Run workflow**

2. **Check Your Contribution Graph:**
   - Go to your GitHub profile
   - Check the contribution graph
   - Commits should now appear as **green squares**!

3. **Verify Commit Author:**
   - Go to your repository
   - Click on a recent commit
   - It should show **your name/username**, not `github-actions[bot]`

---

## Troubleshooting

### Commits Still Not Showing?
- ✅ Make sure the PAT has `repo` scope
- ✅ Check that secrets are named exactly: `PERSONAL_ACCESS_TOKEN`, `GIT_EMAIL`, `GIT_NAME`
- ✅ Wait a few minutes - GitHub graph updates can be delayed
- ✅ Check that commits are being made (look in repository commits)

### Token Expired?
- Create a new PAT and update the `PERSONAL_ACCESS_TOKEN` secret

### Still Using Bot Commits?
- The workflow will fall back to bot commits if PAT is not set
- This is fine for testing, but won't count on your graph

---

## Security Notes

- 🔒 **Keep your PAT secret!** Never share it or commit it to code
- 🔒 PATs stored in GitHub Secrets are encrypted
- 🔒 You can revoke the token anytime in Settings → Developer settings
- 🔒 Use a token with minimal required permissions (`repo` scope)

---

## That's It!

Once you add the `PERSONAL_ACCESS_TOKEN` secret, all future commits will count toward your contribution graph! 🎉

Your GitHub graph will show beautiful green squares every day! 📈

