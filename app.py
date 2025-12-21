from flask import Flask, render_template, jsonify, request
import subprocess
import random
import threading
import time
from datetime import datetime, date
import os
import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

app = Flask(__name__)

# Store for tracking commits
commit_status = {
    'running': False,
    'total_commits': 0,
    'today_commits': 0,
    'last_run': None,
    'scheduled': True,
    'auto_mode': True
}

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Track last commit date
last_commit_date_file = 'last_commit_date.json'
config_file = 'config.json'

# Load configuration
def load_config():
    """Load configuration from config.json"""
    default_config = {
        "auto_mode": True,
        "scheduled_time": {"hour": 2, "minute": 0},
        "commit_range": {"min": 7, "max": 10},
        "delay_range": {"min_seconds": 30, "max_seconds": 120},
        "auto_push": True
    }
    try:
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                return {**default_config, **config}
    except:
        pass
    return default_config

config = load_config()

def get_commit_count_today():
    """Get the number of commits made today"""
    try:
        result = subprocess.run(
            ['git', 'log', '--since', 'midnight', '--oneline'],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        return len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
    except:
        return 0

def get_last_commit_date():
    """Get the last date commits were made"""
    try:
        if os.path.exists(last_commit_date_file):
            with open(last_commit_date_file, 'r') as f:
                data = json.load(f)
                return data.get('date', None)
    except:
        pass
    return None

def save_last_commit_date():
    """Save the current date as last commit date"""
    try:
        with open(last_commit_date_file, 'w') as f:
            json.dump({'date': str(date.today())}, f)
    except:
        pass

def check_git_setup():
    """Check if git is properly configured"""
    try:
        # Check if git is initialized
        result = subprocess.run(
            ['git', 'rev-parse', '--is-inside-work-tree'],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        if result.returncode != 0:
            print("ERROR: Not a git repository. Please run 'git init' first.")
            return False
        
        # Check if remote is configured
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        if result.returncode != 0:
            print("WARNING: No remote 'origin' configured. Commits will be local only.")
            print("To push to GitHub, run: git remote add origin <your-repo-url>")
            return False
        
        return True
    except Exception as e:
        print(f"Error checking git setup: {e}")
        return False

def push_to_github():
    """Push commits to GitHub"""
    if not config.get('auto_push', True):
        return True
    
    try:
        result = subprocess.run(
            ['git', 'push'],
            capture_output=True,
            text=True,
            cwd=os.getcwd(),
            timeout=30
        )
        if result.returncode == 0:
            print("✓ Successfully pushed to GitHub")
            return True
        else:
            print(f"⚠ Push failed: {result.stderr}")
            # Try to get more info
            if "fatal: not a git repository" in result.stderr:
                print("ERROR: Not a git repository!")
            elif "fatal: No configured push destination" in result.stderr:
                print("ERROR: No remote configured. Run: git remote add origin <url>")
            return False
    except subprocess.TimeoutExpired:
        print("⚠ Push timed out")
        return False
    except Exception as e:
        print(f"⚠ Error pushing to GitHub: {e}")
        return False

def make_commit(message):
    """Make a single commit and push to GitHub"""
    try:
        # Append to activity log
        with open('activity.log', 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
            f.write(f'\n{timestamp} - {message}')
        
        # Stage and commit
        subprocess.run(['git', 'add', 'activity.log'], check=True, cwd=os.getcwd())
        subprocess.run(
            ['git', 'commit', '-m', f'{message} [skip ci]'],
            check=True,
            cwd=os.getcwd()
        )
        
        # Push to GitHub after each commit
        push_to_github()
        return True
    except Exception as e:
        print(f"Error making commit: {e}")
        return False

def run_daily_commits():
    """Make 7-10 commits with random intervals"""
    # Check if commits were already made today
    last_date = get_last_commit_date()
    today = str(date.today())
    
    if last_date == today:
        print(f"Commits already made today ({today}). Skipping.")
        return
    
    commit_status['running'] = True
    commit_status['total_commits'] = 0
    
    # Random number of commits from config
    commit_min = config.get('commit_range', {}).get('min', 7)
    commit_max = config.get('commit_range', {}).get('max', 10)
    num_commits = random.randint(commit_min, commit_max)
    commit_status['total_commits'] = num_commits
    
    commit_messages = [
        "Daily activity update",
        "Code maintenance",
        "Project progress",
        "Documentation update",
        "Code refactoring",
        "Bug fixes",
        "Feature development",
        "Testing improvements",
        "Performance optimization",
        "Code review updates"
    ]
    
    print(f"Starting to make {num_commits} commits...")
    
    for i in range(num_commits):
        if not commit_status['running']:
            break
            
        message = random.choice(commit_messages)
        if make_commit(f"{message} - Commit {i+1}/{num_commits}"):
            commit_status['today_commits'] = get_commit_count_today()
            print(f"Made commit {i+1}/{num_commits}")
            if i < num_commits - 1:  # Don't sleep after last commit
                delay_min = config.get('delay_range', {}).get('min_seconds', 30)
                delay_max = config.get('delay_range', {}).get('max_seconds', 120)
                time.sleep(random.uniform(delay_min, delay_max))
    
    # Final push to ensure everything is on GitHub
    push_to_github()
    
    # Save today's date
    save_last_commit_date()
    
    commit_status['running'] = False
    commit_status['last_run'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commit_status['today_commits'] = get_commit_count_today()
    print(f"Completed {num_commits} commits for {today}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    commit_status['today_commits'] = get_commit_count_today()
    return jsonify(commit_status)

@app.route('/api/start', methods=['POST'])
def start_commits():
    if commit_status['running']:
        return jsonify({'success': False, 'message': 'Commits are already running'})
    
    thread = threading.Thread(target=run_daily_commits, daemon=True)
    thread.start()
    return jsonify({'success': True, 'message': 'Started making commits'})

@app.route('/api/stop', methods=['POST'])
def stop_commits():
    commit_status['running'] = False
    return jsonify({'success': True, 'message': 'Stopped commit process'})

@app.route('/api/schedule', methods=['POST'])
def schedule_commits():
    data = request.json
    commit_status['scheduled'] = data.get('enabled', False)
    return jsonify({'success': True, 'message': 'Schedule updated'})

def schedule_daily_commits():
    """Schedule commits to run daily at configured time"""
    scheduled_time = config.get('scheduled_time', {'hour': 2, 'minute': 0})
    hour = scheduled_time.get('hour', 2)
    minute = scheduled_time.get('minute', 0)
    
    scheduler.add_job(
        run_daily_commits,
        trigger=CronTrigger(hour=hour, minute=minute),
        id='daily_commits',
        replace_existing=True
    )
    print(f"Scheduled daily commits at {hour:02d}:{minute:02d}")

def check_and_run_if_needed():
    """Check if commits need to be made today and run if needed"""
    last_date = get_last_commit_date()
    today = str(date.today())
    
    if last_date != today:
        print(f"No commits made today. Starting automatic commits...")
        thread = threading.Thread(target=run_daily_commits, daemon=True)
        thread.start()

if __name__ == '__main__':
    # Check git setup
    git_ok = check_git_setup()
    if not git_ok:
        print("\n⚠ WARNING: Git setup issues detected. Some features may not work.")
        print("Please ensure:")
        print("  1. Git is initialized: git init")
        print("  2. Remote is configured: git remote add origin <your-repo-url>")
        print("  3. You have push access to the repository\n")
    
    # Schedule daily commits
    if config.get('auto_mode', True):
        schedule_daily_commits()
        
        # Check if commits need to be made today (on startup)
        check_and_run_if_needed()
    
    scheduled_time = config.get('scheduled_time', {'hour': 2, 'minute': 0})
    commit_range = config.get('commit_range', {'min': 7, 'max': 10})
    
    print("=" * 60)
    print("🚀 Daily GitHub Commits - FULLY AUTOMATIC MODE")
    print("=" * 60)
    if config.get('auto_mode', True):
        print(f"✓ Commits scheduled daily at {scheduled_time['hour']:02d}:{scheduled_time['minute']:02d}")
        print(f"✓ Will make {commit_range['min']}-{commit_range['max']} commits per day")
    print("✓ Web UI available at http://localhost:5000")
    print("✓ All commits automatically pushed to GitHub")
    print("✓ No manual intervention needed!")
    print("=" * 60)
    print()
    
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)

