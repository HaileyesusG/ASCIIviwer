import requests
from html.parser import HTMLParser
import sys

def fetch_html(doc_url):
    resp = requests.get(doc_url)
    resp.raise_for_status()
    return resp.text


class CellExtractor(HTMLParser):
    """
    Extracts text inside <td>, <th>, or <div role="listitem"> 
    using only html.parser.
    """

    def __init__(self):
        super().__init__()
        self.in_cell = False
        self.captured_text = []
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        # Check for <td>, <th>, or <div role="listitem">
        if tag in ("td", "th"):
            self.in_cell = True
            self.current_tag = tag

        if tag == "div":
            for k, v in attrs:
                if k == "role" and v == "listitem":
                    self.in_cell = True
                    self.current_tag = "div-listitem"

    def handle_endtag(self, tag):
        if tag == self.current_tag or (
            self.current_tag == "div-listitem" and tag == "div"
        ):
            self.in_cell = False
            self.current_tag = None

    def handle_data(self, data):
        if self.in_cell:
            text = data.strip()
            if text:
                self.captured_text.append(text)


def parse_table_cells(html):
    parser = CellExtractor()
    parser.feed(html)
    return parser.captured_text


def extract_coords_from_cells(cell_texts):
    coords = []
    i = 0
    n = len(cell_texts)

    while i + 2 < n:
        x_text = cell_texts[i]
        char_text = cell_texts[i + 1]
        y_text = cell_texts[i + 2]

        try:
            x = int(x_text)
            char = char_text
            y = int(y_text)
            coords.append((x, char, y))
            i += 3
        except ValueError:
            i += 1

    return coords


def build_and_print_grid(coords):
    if not coords:
        print("No ASCII table data found.")
        return

    max_x = max(x for x, _, _ in coords)
    max_y = max(y for _, _, y in coords)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, char, y in coords:
        if 0 <= y <= max_y and 0 <= x <= max_x:
            grid[y][x] = char

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
