# Log Analysis Script

This repository contains a Python script designed to parse and analyze server logs for security events. The script identifies suspicious entries such as failed login attempts and errors.

## How to Use

1. Place your log file in the same directory as the script.
2. Update the `log_file` variable in the script to point to your log file.
3. Run the script to see suspicious entries highlighted.

## Example

If you have a log file named `example_log.txt`, the script will output any lines containing:
- Failed password
- Invalid user
- error
