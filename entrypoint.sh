#!/bin/bash

# Remove Xvfb lock file if it exists
if [ -f /tmp/.X99-lock ]; then
  rm -f /tmp/.X99-lock
fi
# Start Xvfb

Xvfb :99 -screen 0 1280x720x24 &

# Execute the CMD
exec "$@"
