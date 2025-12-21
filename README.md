# Daily GitHub Commit Automation

**FULLY AUTOMATIC** - A web-based application that automatically makes 7-10 commits per day to your GitHub repository and pushes them, making your contribution graph look beautiful with zero manual work!

## ✨ Features

- 🤖 **Fully Automatic** - Runs daily at 2:00 AM, no manual intervention needed
- 🚀 **Auto-Push to GitHub** - All commits automatically pushed to update your graph
- 🎨 **Beautiful Web UI** - Monitor status and control the system
- 📊 **Smart Scheduling** - Prevents duplicate commits, runs on startup if needed
- ⚡ **Windows Auto-Start** - Can run automatically when you log in
- 🎯 **Natural Pattern** - Random delays between commits (30-120 seconds)
- 📈 **7-10 Commits Daily** - Randomly selected for natural appearance

## 🎯 How It Works (Fully Automatic!)

1. **On Startup:** Checks if commits were made today, if not - starts immediately
2. **Daily Schedule:** Automatically runs at 2:00 AM every day
3. **Makes Commits:** Creates 7-10 commits with random intervals
4. **Auto-Push:** Pushes all commits to GitHub automatically
5. **No Manual Work:** Just run it once and forget about it!

The system:
- Makes 7-10 commits per day (randomly selected)
- Updates the `activity.log` file with timestamps
- Has random delays between commits (30-120 seconds) to appear natural
- Automatically pushes to GitHub after each commit
- Prevents duplicate commits on the same day
- Includes `[skip ci]` in all commit messages

## 🚀 Setup (One-Time Setup, Then Fully Automatic!)

### Prerequisites

- Python 3.7 or higher
- Git installed and configured
- A Git repository initialized in this directory
- GitHub remote configured

### Quick Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Git (if not already done):**
   ```bash
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   git remote add origin https://github.com/yourusername/yourrepo.git
   ```

3. **Start the application:**
   - **Windows:** Double-click `start.bat`
   - **Manual:** Run `python app.py`

4. **That's it!** The system will:
   - Check if commits are needed today and start automatically
   - Schedule daily commits at 2:00 AM
   - Run completely automatically from now on

### 🪟 Windows Auto-Start (Optional)

To make it start automatically when you log in:

1. Run `install_autostart.bat` (as Administrator if needed)
2. The application will now start automatically on Windows login
3. It runs in the background - you won't even notice it!

### Web UI

- Navigate to `http://localhost:5000` to see the dashboard
- Monitor commit status, today's commits, and system information
- Manually start/stop commits if needed (though it's fully automatic!)

## 📖 Usage

### Automatic Mode (Default)

**Just run it once and forget it!**

1. Start the application (`start.bat` or `python app.py`)
2. The system automatically:
   - Checks if commits are needed today
   - Starts making commits if needed
   - Schedules daily commits at 2:00 AM
   - Pushes everything to GitHub
3. **That's it!** Your GitHub graph will be beautiful automatically!

### Manual Control (Optional)

- Open `http://localhost:5000` in your browser
- View real-time status and statistics
- Manually start/stop commits if needed
- Monitor today's commit count and progress

## UI Features

- **Status Display:** See if commits are running or stopped
- **Today's Commits:** Track how many commits were made today
- **Progress Bar:** Visual indicator of commit progress
- **Last Run:** Timestamp of the last commit session

## ⚙️ Configuration

Edit `config.json` to customize:

```json
{
    "auto_mode": true,              // Enable/disable automatic mode
    "scheduled_time": {
        "hour": 2,                  // Hour to run (24-hour format)
        "minute": 0                  // Minute to run
    },
    "commit_range": {
        "min": 7,                   // Minimum commits per day
        "max": 10                   // Maximum commits per day
    },
    "delay_range": {
        "min_seconds": 30,          // Minimum delay between commits
        "max_seconds": 120          // Maximum delay between commits
    },
    "auto_push": true               // Automatically push to GitHub
}
```

## 📝 Notes

- ✅ Commits are made to the `activity.log` file
- ✅ All commit messages include `[skip ci]` to prevent workflow triggers
- ✅ System prevents duplicate commits on the same day
- ✅ Random intervals make commits appear natural
- ✅ All commits automatically pushed to GitHub
- ✅ Follows GitHub's terms of service for automated contributions

## 🔧 Troubleshooting

- **Port already in use:** Change the port in `app.py` (line with `app.run()`)
- **Git not found:** Ensure Git is installed and in your system PATH
- **No remote configured:** Run `git remote add origin <your-repo-url>`
- **Push fails:** Check your GitHub credentials and repository permissions
- **No commits appearing:** 
  - Verify Git is initialized: `git status`
  - Check remote: `git remote -v`
  - Ensure you have push access to the repository
- **Application not starting:** 
  - Install requirements: `pip install -r requirements.txt`
  - Check Python version: `python --version` (needs 3.7+)

## 🎉 Result

After setup, your GitHub contribution graph will automatically show 7-10 commits every day, making it look beautiful and active - all without any manual work!
