import requests
from bs4 import BeautifulSoup
import sys

def fetch_html(doc_url):
    resp = requests.get(doc_url)
    resp.raise_for_status()
    return resp.text

def parse_table_cells(html):
    soup = BeautifulSoup(html, "html.parser")

    rows = [] 
    # Try to find all “table cell” like elements. Google Docs published HTML often uses <div> for tables.
    # Here we look for elements that might correspond to cells in your data table: e.g., <div role="listitem"> or <td>, etc.
    for cell in soup.select('div[role="listitem"], td, th'):
        text = cell.get_text(strip=True)
        if text:
            rows.append(text)
    return rows

def extract_coords_from_cells(cell_texts):
    """
    Given a flat list of cell texts, try to assemble them into (x, char, y) tuples.
    We assume the table is structured such that every 3 cells = one row of data.
    """
    coords = []
    i = 0
    n = len(cell_texts)
    while i + 2 < n:
        x_text = cell_texts[i]
        char_text = cell_texts[i+1]
        y_text = cell_texts[i+2]
        # Try conversion
        try:
            x = int(x_text)
            char = char_text
            y = int(y_text)
            coords.append((x, char, y))
            i += 3
        except ValueError:
            # skip an element and try again
            i += 1
    return coords

def build_and_print_grid(coords):
    if not coords:
        print("No ASCII table data found.")
        return

    max_x = max(x for x, _, _ in coords)
    max_y = max(y for _, _, y in coords)

    grid = [[" " for _ in range(max_x+1)] for _ in range(max_y+1)]
    for x, char, y in coords:
        # Ensure within bounds
        if 0 <= y <= max_y and 0 <= x <= max_x:
            grid[y][x] = char

    # Print top-to-bottom (y descending)
    for row in reversed(grid):
        print("".join(row))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <Google_Doc_Published_URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        html = fetch_html(url)
        cell_texts = parse_table_cells(html)
        coords = extract_coords_from_cells(cell_texts)
        build_and_print_grid(coords)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
