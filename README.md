A Python tool that fetches a published Google Docs page, extracts ASCII-art data stored as table rows (x-coordinate, character, y-coordinate), and reconstructs the ASCII image in the terminal.
The script uses requests to download the HTML and BeautifulSoup (with the built-in html.parser) to navigate Google Docs’ nested table-like structure.
Coordinates are parsed into a grid and rendered top-down to produce the final ASCII art exactly as intended.

to run the code use 
python ascii_art_viewer.py <Google Doc link>
Example:- 
python ascii_art_viewer.py https://docs.google.com/document/d/e/2PACX-1vRCzUup1R8CGy3zk7DkdzJyMRvJRPI75Vl3s_9HelL7pr49bzi7-cBxg0zSKwxcWiEvNPxi4Wjj8c0n/pube>
