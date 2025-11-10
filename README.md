# ASCII Art Viewer – Google Docs Table Parser (Requests + html.parser Only)

This Python tool downloads a published Google Docs page, extracts ASCII-art data encoded as table rows `(x-coordinate, character, y-coordinate)`, and reconstructs the ASCII art image directly in the terminal.

The script uses **only**:
- `requests` (for fetching HTML)
- Python’s built-in `html.parser` (`HTMLParser`)  
as explicitly required.

Google Docs does not output normal `<table>` structures. Instead, table cells often appear as nested `<div role="listitem">`, `<td>`, or `<th>` elements.  
This script parses those elements manually and reconstructs the ASCII image.

---

## Features

- Fetches published Google Docs HTML
- Parses table-like data using **only** `html.parser`
- Extracts all cell text that represents ASCII art coordinates
- Groups table content into `(x, character, y)` triples
- Dynamically builds the ASCII grid based on max X/Y values
- Prints the ASCII art from top-to-bottom exactly as intended

---

## Usage

python ascii_art_viewer.py <Google Doc link>

### **Example**:- 
python ascii_art_viewer.py https://docs.google.com/document/d/e/2PACX-1vRCzUup1R8CGy3zk7DkdzJyMRvJRPI75Vl3s_9HelL7pr49bzi7-cBxg0zSKwxcWiEvNPxi4Wjj8c0n/pube>
