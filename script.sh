#!/bin/bash

output_file="balls.txt"

# Make sure the output file is empty
> "$output_file"

#  cleanup terminal settings on exit
cleanup() {
    stty "$saved_stty"
    echo "Exiting..."
    exit
}

# Save the current terminal settings
saved_stty=$(stty -g)

# Set terminal to raw mode to capture each keystroke
stty raw -echo

# Trap signals to restore terminal settings on exit
trap cleanup INT TERM EXIT

echo "Typing will be saved to $output_file. Press Ctrl-C to stop."

# Read input one character at a time
while true; do
    # Read one byte using `dd` and `stty` in raw mode
    char=$(dd bs=1 count=1 2>/dev/null)
    # Check if Ctrl-C is pressed
    if [[ "$char" == $'\x03' ]]; then
        cleanup
    fi
    # Append the character to the file
    printf "%s" "$char" >> "$output_file"
done
