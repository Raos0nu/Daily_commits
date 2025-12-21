# 🚀 Quick Start Guide

## Step 1: Start the Application

**Easiest way:** Double-click `start.bat` in this folder

**OR** open PowerShell/Command Prompt here and run:
```powershell
python app.py
```

## Step 2: Open the Web Interface

1. Wait 5-10 seconds for the server to start
2. Open your browser
3. Go to: **http://localhost:5000**

You should see a beautiful dashboard showing:
- Current status
- Today's commit count
- Auto-mode status
- Start/Stop buttons

## Step 3: What Happens Automatically

Once started, the system will:

1. ✅ **Check if commits are needed today** - If no commits were made today, it starts immediately
2. ✅ **Make 7-10 commits** - Randomly selected, with natural delays
3. ✅ **Push to GitHub** - All commits automatically pushed to update your graph
4. ✅ **Schedule daily runs** - Will run every day at 2:00 AM automatically

## Step 4: Keep It Running

- **Keep the console window open** - The app needs to stay running
- **Or use auto-start** - Run `install_autostart.bat` to make it start with Windows

## Troubleshooting

**If you see "Connection Refused":**
- Make sure the console window is open and running
- Wait a few more seconds for the server to start
- Check for any error messages in the console

**If commits aren't being made:**
- Check that Git remote is configured: `git remote -v`
- Make sure you have push access to the repository
- Check the console for error messages

## That's It!

The system is now fully automatic. Just keep it running and your GitHub graph will be beautiful! 🎉

