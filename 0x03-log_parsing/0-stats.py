#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {}
line_count = 0

# List of possible status codes
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
for code in status_codes:
    status_counts[code] = 0

# Regular expression to match the required log format
log_pattern = re.compile(
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(?P<date>.+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'
)

def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption signal."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Read from standard input line by line
for line in sys.stdin:
    line_count += 1
    match = log_pattern.match(line)
    if match:
        size = int(match.group('size'))
        status = int(match.group('status'))

        total_size += size
        if status in status_counts:
            status_counts[status] += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print statistics at the end of input
print_stats()
