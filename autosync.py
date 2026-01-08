import os
import time
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = os.path.dirname(os.path.abspath(__file__))
SYNC_INTERVAL = 30  # Seconds
EXTENSIONS = {'.md', '.py', '.java'}

def run_git(args):
    try:
        subprocess.run(["git"] + args, cwd=REPO_PATH, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[{datetime.now()}] Git error: {e.stderr.decode().strip()}")
        return False

def sync():
    # Check for changes
    status = subprocess.run(["git", "status", "--short"], cwd=REPO_PATH, capture_output=True, text=True).stdout.strip()
    
    if not status:
        return

    print(f"[{datetime.now()}] Changes detected. Syncing...")
    
    # Add all changes
    if run_git(["add", "."]):
        # Commit
        commit_msg = f"Auto-sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        if run_git(["commit", "-m", commit_msg]):
            # Push
            if run_git(["push"]):
                print(f"[{datetime.now()}] Successfully pushed to GitHub.")

if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting Auto-Sync monitor in {REPO_PATH}...")
    print(f"Watching for: {', '.join(EXTENSIONS)}")
    
    try:
        while True:
            sync()
            time.sleep(SYNC_INTERVAL)
    except KeyboardInterrupt:
        print(f"\n[{datetime.now()}] Auto-Sync stopped.")
