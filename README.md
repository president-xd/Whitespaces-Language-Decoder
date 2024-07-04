# Whitespace Language Decoder

This Python script decodes a file encoded in Whitespace language, transforming it into readable ASCII text. Whitespace language is an esoteric programming language where only spaces, tabs, and line breaks have meaning, while other characters are ignored.

## Requirements

- Python 3.x
- Python `pwn` module (`pwntools`)

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/whitespace-decoder.git
cd whitespace-decoder

2. Install the required Python module:
pip install pwntools


## Usage

Ensure you have a file encoded in Whitespace language (`filename.txt`), then run the script as follows:


python decoder.py filename.txt


Replace `filename.txt` with the path to your encoded file.

## How It Works

1. **Argument Handling:**
   - Checks if a single argument (filename) is provided when executing the script. If not, it displays usage instructions.

2. **File Reading:**
   - Opens the specified file (`filename.txt`) in binary mode and reads its entire content into memory (`data`).

3. **Whitespace Decoding:**
   - Replaces specific byte sequences in the file:
     - `b'\xe2\x80\x83'` (representing the Unicode character ' ') is replaced with `b'0'`.
     - `b' '` (space character) is replaced with `b'1'`.
   - Decodes the modified binary data into a string assuming ASCII encoding.

4. **ASCII Conversion:**
   - Uses the `unbits` function from the `pwntools` library to convert the binary string back into its original ASCII form.

5. **Output:**
   - Prints the decoded ASCII text to the console.

6. **Error Handling:**
   - Checks for `FileNotFoundError` and displays an error message if the specified file (`filename.txt`) is not found.

## Example

Assume `encoded_file.txt` contains encoded Whitespace language data:

```plaintext
python decoder.py encoded_file.txt
```

This command will decode encoded_file.txt and print the resulting ASCII text to the console.

## Notes
Make sure the input file (filename.txt) follows the specific encoding rules (b'\xe2\x80\x83' replaced with b'0' and spaces replaced with b'1').
The pwn module (pwntools) must be installed for the script to function properly.
