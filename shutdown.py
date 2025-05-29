import signal
import sys

def shutdown_handler(signum, frame):
    print(f"Received signal {signum}. Shutting down gracefully...")
    # Add cleanup logic here
    sys.exit(0)

# Register the signal handler for termination signals
signal.signal(signal.SIGINT, shutdown_handler)  # Handle Ctrl+C
signal.signal(signal.SIGTERM, shutdown_handler)  # Handle termination signal
