from pwn import *
import sys

if len(sys.argv) != 2:
    print("Usage: python decoder.py <name of file.txt>")
    sys.exit(1)
  
filename = sys.argv[1]

try:
    with open(filename, 'rb') as f:
        data = f.read()
      
    data = data.replace(b'\xe2\x80\x83', b'0').replace(b' ', b'1')
    data = data.decode("ascii")
    
    print(unbits(data).decode("ascii"))

except FileNotFoundError:
    print(f"File '{filename}' not found.")
    sys.exit(1)
