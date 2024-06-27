#!/usr/bin/env python3

"""
Sublime Patcher
"""

import sys
import os
import shutil

def main():
    if len(sys.argv) < 2:
        print("Usage: ./sublpatcher.py <path-to-sublime-executable>")
        exit(1)

    input_file = sys.argv[1]
    output_file = 'sublime_text_patched'
    
    with open(input_file, 'rb') as f:
        data = f.read()

    # Find the hex string to replace
    old_hex = b'\x80\x78\x05\x00\x0F\x94\xC1'
    offset = data.find(old_hex)

    if offset == -1:
        print("File already patched")
        exit(1)

    # Replace the hex string
    new_hex = b'\xC6\x40\x05\x01\x48\x85\xC9'
    data = data[:offset] + new_hex + data[offset+len(old_hex):]

    with open(output_file, 'wb') as f:
        f.write(data)
    
    if os.name != 'nt':
        os.chmod(output_file, 0o755)

    print(f"[+] Sending {output_file} to its parent directory")
    
    # Replace the original file with the patched file
    if os.name == 'nt':
        os.remove(input_file)
        shutil.move(output_file, input_file)
    else:
        os.rename(output_file, input_file)

if __name__ == "__main__":
    main()
