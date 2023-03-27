#!/usr/bin/env python3

"""
this patch is for Sublime V4 Build 4143
"""

import sys
import os
if len(sys.argv) < 2:
    print("Usage: ./sublpatcher.py <path-to-file>")
    exit(1)

input_file = sys.argv[1]
output_file = 'sublime_text'

# Open the input file for reading
with open(input_file, 'rb') as f:
    data = f.read()

# Find the hex string to replace
old_hex = b'\x80\x78\x05\x00\x0F\x94\xC1'
offset = data.find(old_hex)

if offset == -1:
    print("file already patched")
    exit(1)

# Replace the hex string
new_hex = b'\xC6\x40\x05\x01\x48\x85\xC9'
data = data[:offset] + new_hex + data[offset+len(old_hex):]

# Write the modified data to the output file
with open(output_file, 'wb') as f:
    f.write(data)
os.chmod(output_file, 0o755)

print(f"[+] sending {output_file} to its main directory")
os.rename(output_file, input_file)
