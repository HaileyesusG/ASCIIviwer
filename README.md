A Python tool that fetches a published Google Docs page, extracts ASCII-art data stored as table rows (x-coordinate, character, y-coordinate), and reconstructs the ASCII image in the terminal.
The script uses requests to download the HTML and BeautifulSoup (with the built-in html.parser) to navigate Google Docs’ nested table-like structure.
Coordinates are parsed into a grid and rendered top-down to produce the final ASCII art exactly as intended.
