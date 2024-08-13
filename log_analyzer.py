# log_analyzer.py
# A simple script to parse and analyze logs for security events

import re

def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    
    suspicious_patterns = [
        r'Failed password',
        r'Invalid user',
        r'error'
    ]
    
    for line in logs:
        for pattern in suspicious_patterns:
            if re.search(pattern, line):
                print(f"Suspicious entry found: {line.strip()}")

if __name__ == "__main__":
    log_file = 'example_log.txt'  # replace with your log file
    parse_log(log_file)
