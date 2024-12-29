#!/bin/bash
# start.sh

# Run multiple commands concurrently
python alert.py &  # Run in the background
echo "alerting has been started"

python voiceassistant.py &  # Run in the background
echo "you can start talking and add tasks"

# Keep the script running to prevent it from exiting
wait
