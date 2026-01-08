#!/bin/bash

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Start the python script in the background
nohup python3 "$DIR/autosync.py" > "$DIR/autosync.log" 2>&1 &

echo "Auto-Sync started in the background. Logging to autosync.log"
echo "PID: $!"
